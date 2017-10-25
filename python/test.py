"""

Test Script

The following script has been made in order to test Onshape API features

Fluvio L Lobo Fenoglietto
Sam Drucker
10/25/2017
"""

# Import Libraries and/or Modules

from    apikey.client   import Client

# Set-Up Stacks
stacks = {
    'cad': 'https://cad.onshape.com'
}

# Create Instance for Onshape Stack
c = Client(stack=stacks['cad'], logging=True)

# Generate New Onshape Document
new_doc = c.new_document(name="input",public=True).json()
did = new_doc['id']
wid = new_doc['defaultWorkspace']['id']

# Get Document Information
details = c.get_document(did)
print 'Document name: ' + details.json()['name']

# Import Dataset
input_file_path = "data/demo_rand_array.csv"
details = c.upload_blob(did, wid, filepath=input_file_path)
