from typing import Dict, Any
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Microsoft Graph API settings
MSGRAPH_CLIENT_ID = os.getenv("MSGRAPH_CLIENT_ID")
MSGRAPH_CLIENT_SECRET = os.getenv("MSGRAPH_CLIENT_SECRET")
MSGRAPH_TENANT_ID = os.getenv("MSGRAPH_TENANT_ID")

# Airtable settings
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

# Mistral AI settings
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Logging settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO") 