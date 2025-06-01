import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
from django.conf import settings

#  Token validation function
def is_token_valid(access_token):
    userinfo_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(userinfo_url, headers=headers)
    return response.status_code == 200

@api_view(['POST'])
def oauth_login(request):
    """Exchange authorization code for tokens"""
    code = request.data.get("code")
    redirect_uri = "https://oauth.pstmn.io/v1/callback"

    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }
    
    res = requests.post(token_url, data=payload)
    return Response(res.json())

@api_view(['POST'])
def add_item(request):
    # Get and validate access token
    access_token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not is_token_valid(access_token):
        return Response({"error": "Unauthorized"}, status=401)

    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_items(request):
    #  Get and validate access token
    access_token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not is_token_valid(access_token):
        return Response({"error": "Unauthorized"}, status=401)

    title = request.query_params.get('title')
    items = Item.objects.filter(title__icontains=title) if title else Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
