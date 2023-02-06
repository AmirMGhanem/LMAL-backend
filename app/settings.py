import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = "TestKey123"

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = False
# Connect to the database

MONGO_URL = os.environ.get("MONGO_URL")
ATLAS_URI=os.environ.get("ATLAS_URI")
DB_NAME=os.environ.get("DB_NAME")

#CORS Policy
CORS_HEADERS = 'Content-Type'
