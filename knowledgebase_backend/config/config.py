from dotenv import dotenv_values
import os

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Access your variables
OPEN_AI_API_KEY = env_vars.get("OPEN_AI_API_KEY")
AWS_ACCESS_KEY = env_vars.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = env_vars.get("AWS_SECRET_KEY")
AWS_BUCKET_NAME = env_vars.get("AWS_BUCKET_NAME")
SECRET_KEY = env_vars.get("SECRET_KEY")
MONG0_URI = env_vars.get("MONG0_URI")
GOOGLE_CLIENT_ID = env_vars.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = env_vars.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = env_vars.get("GOOGLE_REDIRECT_URI")
AWS_S3_URL = env_vars.get("AWS_S3_URL")

# Print one of the variables to verify
print(OPEN_AI_API_KEY)
