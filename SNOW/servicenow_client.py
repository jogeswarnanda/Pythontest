import requests
from requests.auth import HTTPBasicAuth
from config import Config
import json

class ServiceNowClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        print(f"ServiceNowClient initialized for instance: {self.base_url}")
        self.auth = HTTPBasicAuth(Config.SERVICENOW_USERNAME, Config.SERVICENOW_PASSWORD)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'

           
                  
        }

    def get_incident(self, incident_number):
        """Retrieve incident details by incident number"""
        url = f"{Config.INCIDENT_API}"
        params = {'sysparm_query': f'number={incident_number}'}

        print( f"Retrieving incident {incident_number} from {url} with params {params}" )
        
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            if data.get('result'):
                return data['result'][0]
            else:
                print(f"Incident {incident_number} not found")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving incident: {e}")
            return None
    
    def update_incident(self, sys_id, update_data):
        """Update incident with provided data"""
        url = f"{Config.INCIDENT_API}/{sys_id}"
        
        try:
            response = requests.patch(url, auth=self.auth, headers=self.headers, 
                                     data=json.dumps(update_data))
            response.raise_for_status()
            
            print(f"Successfully updated incident (sys_id: {sys_id})")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating incident: {e}")
            return None
    
    def resolve_incident(self, incident_number, resolution_notes, close_code='Solved (Permanently)'):
        """
        Resolve an incident with resolution details
        
        Args:
            incident_number: The incident number (e.g., 'INC0010001')
            resolution_notes: Resolution notes/comments
            close_code: Close code for the incident
        """
        # First, get the incident to retrieve its sys_id
        incident = self.get_incident(incident_number)
        
        if not incident:
            return False
        
        sys_id = incident['sys_id']
        
        # Prepare update data
        update_data = {
            'state': Config.STATE_RESOLVED,
            'close_notes': resolution_notes,
            'close_code': close_code,
            'resolved_at': 'now'  # ServiceNow will convert 'now' to current timestamp
        }
        
        # Update the incident
        result = self.update_incident(sys_id, update_data)
        
        if result:
            print(f"Incident {incident_number} has been resolved")
            return True
        return False
    
    def add_work_notes(self, incident_number, work_notes):
        """Add work notes to an incident"""
        incident = self.get_incident(incident_number)
        
        if not incident:
            return False
        
        sys_id = incident['sys_id']
        update_data = {'work_notes': work_notes}
        
        result = self.update_incident(sys_id, update_data)
        return result is not None
    
    def get_open_incidents(self, assignment_group=None):
        """Get list of open incidents, optionally filtered by assignment group"""
        url = Config.INCIDENT_API
        
        # Build query for open incidents (state < 6 means not resolved/closed)
        query = 'state<6'
        if assignment_group:
            query += f'^assignment_group.name={assignment_group}'
        
        params = {
            'sysparm_query': query,
            'sysparm_limit': 100  # Limit to 100 results
        }
        
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get('result', [])
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving incidents: {e}")
            return []