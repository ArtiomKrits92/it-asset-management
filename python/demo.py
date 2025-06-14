### This is a file which contains db pre-created dummy data for project demonstration. 
### Those values will be imported to the project.
### New data added using project functions will be added/modified as well to the existing db with the pre-created and earlier added data from this file.
from functions import db    # Import database data from functions.py file
def dummie_data():
    # Pre-loaded users section
    db["user"]["9998"] = "Desmond Coacher"
    db["user"]["9999"] = "Artiom Krits"