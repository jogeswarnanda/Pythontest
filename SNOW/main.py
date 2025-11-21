from servicenow_client import ServiceNowClient
import csv
import os

def resolve_single_incident():
    """Example: Resolve a single incident"""
    client = ServiceNowClient()
    
    incident_number = input("Enter incident number (e.g., INC0010001): ")
    resolution_notes = input("Enter resolution notes: ")
    
    success = client.resolve_incident(incident_number, resolution_notes)
    
    if success:
        print("✓ Incident resolved successfully!")
    else:
        print("✗ Failed to resolve incident")

def resolve_bulk_incidents_from_csv(csv_file):
    """
    Resolve multiple incidents from a CSV file
    CSV format: incident_number,resolution_notes,close_code
    """
    client = ServiceNowClient()
    
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                incident_number = row['incident_number']
                resolution_notes = row['resolution_notes']
                close_code = row.get('close_code', 'Solved (Permanently)')
                
                print(f"\nProcessing {incident_number}...")
                client.resolve_incident(incident_number, resolution_notes, close_code)
                
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")
    except Exception as e:
        print(f"Error processing CSV: {e}")

def resolve_incidents_from_list():
    """Resolve multiple incidents from a predefined list"""
    client = ServiceNowClient()
    
    # Define your incidents here
    incidents_to_resolve = [
        {
            'incident_number': 'INC0010001',
            'resolution_notes': 'Issue resolved by restarting the service',
            'close_code': 'Solved (Permanently)'
        },
        {
            'incident_number': 'INC0010002',
            'resolution_notes': 'User error - provided training',
            'close_code': 'Solved (Permanently)'
        }
        # Add more incidents as needed
    ]
    
    for incident in incidents_to_resolve:
        print(f"\nResolving {incident['incident_number']}...")
        client.resolve_incident(
            incident['incident_number'],
            incident['resolution_notes'],
            incident.get('close_code', 'Solved (Permanently)')
        )

def add_work_notes_example():
    """Example: Add work notes to an incident"""
    client = ServiceNowClient()
    
    incident_number = input("Enter incident number: ")
    work_notes = input("Enter work notes: ")
    
    if client.add_work_notes(incident_number, work_notes):
        print("✓ Work notes added successfully!")
    else:
        print("✗ Failed to add work notes")

def list_open_incidents():
    """List all open incidents"""
    client = ServiceNowClient()
    
    print("\nFetching open incidents...")
    incidents = client.get_open_incidents()
    
    if incidents:
        print(f"\nFound {len(incidents)} open incidents:\n")
        for inc in incidents:
            print(f"Number: {inc.get('number')}")
            print(f"Short Description: {inc.get('short_description')}")
            print(f"State: {inc.get('state')}")
            print(f"Priority: {inc.get('priority')}")
            print("-" * 50)
    else:
        print("No open incidents found")

def main_menu():
    """Interactive menu for the automation app"""
    client = ServiceNowClient()
    
    while True:
        print("\n" + "="*50)
        print("ServiceNow Incident Automation")
        print("="*50)
        print("1. Resolve a single incident")
        print("2. Resolve bulk incidents from CSV")
        print("3. Resolve incidents from predefined list")
        print("4. Add work notes to incident")
        print("5. List open incidents")
        print("6. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            resolve_single_incident()
        elif choice == '2':
            csv_file = input("Enter CSV file path: ")
            resolve_bulk_incidents_from_csv(csv_file)
        elif choice == '3':
            resolve_incidents_from_list()
        elif choice == '4':
            add_work_notes_example()
        elif choice == '5':
            list_open_incidents()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()