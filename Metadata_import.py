# Importing metadata to dhis2 instance through the API
import requests
import json

#dhis2 Auth
dhis2_url = 'dhis2 instance url'
username = 'username'
password = 'password'

#file path
metadata_file = 'path/'

# Read metadata from file
with open(metadata_file, 'r') as file:
    metadata = json.load(file)

# API endpoint for metadata import
url = f'{dhis2_url}/api/metadata'

# Send the import request
response = requests.post(url, auth=(username, password), json=metadata)

#response status

if response.status_code == 200:
    print('Metadata imported succesfully')
else:
    print(f'error: {response.status_code}')    
    print(response.json)