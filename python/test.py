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
input_file = c.upload_blob(did, wid, filepath=input_file_path)
eid = details.json()['id']
print(eid)

details = c.evaluate_featurescript(did, wid, eid, script_name='import_data')

"""
# Delete Document
c.del_document(did)

# tCheck for Trashed Document
trashed_doc = c.get_document(did)

if trashed_doc.json()['trash'] is True:
    print 'Document now in trash'
else:
    print 'Error: Document not trashed'

"""
