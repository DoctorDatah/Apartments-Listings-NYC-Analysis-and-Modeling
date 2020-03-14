import re 
import os
import sys
import googlemaps
import numpy as np 
import pandas as pd 
from IPython.display import clear_output

PROJECT_ROOT = os.getcwd()
SECRETS_DIR = os.path.join(PROJECT_ROOT, "secrets")
SECRET_KEY_PATH = os.path.join(SECRETS_DIR, "Key.txt")

def get_key():
    """
    Fetchs the secret Google API key from secrets folder
    """
    try:
        with open(SECRET_KEY_PATH, 'r') as file: 
              return file.read()
    except: 
        print('Something went wrong')
        


def get_zips(row): 
    """
    Makes API calls of Google maps API. 
    Retrives corresponding zip codes for addresses.
    ---------------------------
    key idea from ML Blueprints
    """
    loading_bar()
    
    try: 
    
        # removing ',' from a record | So, we can get the cleaned string to get zipcode
        addr = row['address'] + ' ' + row['neighborhood'].split(', ')[-1]     
            
        # Fetching Related data 
        if re.match('^\d+\s\w', addr): 
            # geocode returns json formated data, we are only intersed in zip codes
            geocode_result = gmaps.geocode(addr) 
            
            # Iterating every json record to get corrsponding zip-code
            for piece in geocode_result[0]['address_components']: 
                if 'postal_code' in piece['types']: 
                    return piece['short_name'] 
                else: 
                    # we are not able to fetch zip
                    pass 
        else: 
            return np.nan 
    except: 
        return np.nan
    
    
def loading_bar():
     # Remove Previous Print and add new
    clear_output(wait=True)
    print("......10%")
    clear_output(wait=True)
    print("..................40%")
    clear_output(wait=True)
    print("..................................70%")
    clear_output(wait=True)
    print("....................................................... 100%")
