# Django Backend Assignment - Order Management System Framework

This project implements a foundational backend template using Django REST Framework, integrating Google OAuth 2.0 API Authentication and a secure Data Entry & Retrieval API, suitable for an Order Management System framework.

## Features

* **Google OAuth 2.0 API Authentication:** Secure user authentication using Google's OAuth 2.0. Users can log in/sign up using their Google accounts.
* **Access and Refresh Tokens:** The authentication process handles obtaining these tokens. `djangorestframework.authtoken` is integrated to provide unique API tokens for authenticated users.
* **Data Entry API:** Provides a `POST` endpoint to add structured data (e.g., `title`, `description`) to the database, automatically associating the data with the authenticated user.
* **Data Retrieval API:** Offers a `GET` endpoint to fetch data. This endpoint is protected and automatically filters results to show only data relevant to the authenticated user. It also supports filtering by `title` using a query parameter.
* **Robust Database:** Configured to use PostgreSQL for production environments (defaults to SQLite for local development if PostgreSQL is not configured).
* **Secure Handling of Sensitive Keys:** All sensitive credentials are managed via environment variables using `python-dotenv`.
* **Static File Handling:** Configured with `whitenoise` for serving static files in production.

## Setup Requirements

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-link>
    cd your_project_name
    ```
2.  **Create a Python virtual environment (highly recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up Environment Variables:**
    * Create a `.env` file in the root directory of the project (`your_project_name/`).
    * Add the following variables, replacing the placeholders with your actual credentials:
        ```
        DJANGO_SECRET_KEY=your_very_strong_django_secret_key_here
        GOOGLE_OAUTH_CLIENT_ID=your_google_cloud_client_id_here
        GOOGLE_OAUTH_CLIENT_SECRET=your_google_cloud_client_secret_here
        # For PostgreSQL deployment, use your database connection string:
        # DATABASE_URL=postgres://user:password@host:port/dbname
        # For local development with SQLite, you can omit DATABASE_URL or set it to:
        # DATABASE_URL=sqlite:///db.sqlite3
        ALLOWED_HOSTS=localhost,127.0.0.1,<your-deployed-domain.com>
        DJANGO_DEBUG=True # Set to False for production deployments
        ```
    * **`DJANGO_SECRET_KEY`**: Generate a strong, random string.
    * **Google OAuth Credentials**:
        * Go to [Google Cloud Console](https://console.cloud.google.com/).
        * Navigate to "APIs & Services" > "Credentials".
        * Click "Create Credentials" > "OAuth client ID" > "Web application".
        * Add your local development redirect URI under **"Authorized redirect URIs"**:
            `http://localhost:8000/auth/social/complete/google-oauth2/`
        * For deployment, you will need to add your deployed application's redirect URI (e.g., `https://your-app-name.onrender.com/auth/social/complete/google-oauth2/`).
        * Your Client ID and Client Secret will be displayed; use these for `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET`.

5.  **Run Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    *(Note: If you switch from SQLite to PostgreSQL, ensure you set up your PostgreSQL database first, update `DATABASE_URL` in `.env`, and then run `python manage.py migrate`.)*

6.  **Create a Django Superuser (for Django Admin access):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Collect Static Files (for production readiness):**
    ```bash
    python manage.py collectstatic
    ```

### Running the Project Locally

```bash
python manage.py runserver
