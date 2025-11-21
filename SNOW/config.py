import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    SERVICENOW_INSTANCE = os.getenv('SERVICENOW_INSTANCE')
    SERVICENOW_USERNAME = os.getenv('SERVICENOW_USERNAME')
    SERVICENOW_PASSWORD = os.getenv('SERVICENOW_PASSWORD')
    
    # ServiceNow API endpoints
    BASE_URL = f"https://{SERVICENOW_INSTANCE}"
    INCIDENT_API = f"{BASE_URL}/api/now/table/incident"
    
    # Incident states
    STATE_RESOLVED = 6  # Resolved state in ServiceNow
    STATE_CLOSED = 7    # Closed state in ServiceNow