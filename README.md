# GitHub OAuth Authentication using FastAPI

## Project Overview

This project demonstrates GitHub OAuth 2.0 Authorization Code Flow using FastAPI.

Users can log in with their GitHub account, authorize the application, and receive an access token through the callback endpoint.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Requests
- Python-dotenv
- GitHub OAuth 2.0

## Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## GitHub OAuth Configuration

1. Create an OAuth App in GitHub Developer Settings.
2. Set the Homepage URL:

   `http://localhost:8000/`

3. Set the Authorization callback URL:

   `http://localhost:8000/callback`

4. Copy your Client ID and Client Secret.

## Environment Variables

Create a `.env` file in the project folder:

```env
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
```

Do not upload the `.env` file to GitHub.

## Run the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload --port 8000
```

Open the homepage:

`http://localhost:8000/`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Homepage |
| GET | `/login` | Redirects to GitHub login |
| GET | `/callback` | Exchanges authorization code for access token |

## API Documentation

FastAPI Swagger documentation:

`http://localhost:8000/docs`

## Learning Outcomes

- Understanding OAuth 2.0 Authorization Code Flow
- Creating FastAPI routes
- Redirecting users to GitHub
- Handling OAuth callback requests
- Exchanging authorization codes for access tokens
- Managing environment variables securely

## Author

GitHub: [shivaranjaniYoho](https://github.com/shivaranjaniYoho)
