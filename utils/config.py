import os
from dotenv import load_dotenv

# Loads the variables from .env
load_dotenv()

# Retrieving login information from the environment
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LINKEDIN_LOGIN_URL = "https://www.linkedin.com/login"

# print(f"Email: {LINKEDIN_EMAIL}")
# print(f"Password: {LINKEDIN_PASSWORD}")
