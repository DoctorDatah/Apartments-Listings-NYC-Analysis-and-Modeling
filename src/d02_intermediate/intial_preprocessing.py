import numpy as np 
import pandas as pd 

def fix_beds_feature(listings):
    """
    Fixes format and duplication issues from beds feature in listings data
    Finally converts to integer
    """
    try:
        if(listings['beds'].dtype != 'int64'):
            # Removindg stating '_'
            listings['beds'] = listings['beds'].map(lambda x: x[1:] if x.startswith('_') else x)

            # Futher Fixing - Setting other Categoris to 0-Beds
            listings['beds'] = listings['beds'].map(lambda x: x.replace('_Bed', '')) 
            listings['beds'] = listings['beds'].map(lambda x: x.replace('Studio', '0')) 
            listings['beds'] = listings['beds'].map(lambda x: x.replace('Loft', '0'))
            listings['beds'] = listings['beds'].map(lambda x: x.replace('Room', '0'))

            # Contering to Numeric
            listings['beds'] = pd.to_numeric(listings['beds'])
            listings['beds'].unique()

        return listings
    except:
        print('Something went wrong')
        

def fix_baths_feature(listings):
    """
    Fixes format issues from baths feature in listings data
    Finally, converts to integer data type
    """
    try:
        if(listings['baths'].dtype != 'int64'):
            # Removindg stating '_'
            listings['baths'] = listings['baths'].map(lambda x: x[1:] if x.startswith('_') else x) 
            listings['baths'] = listings['baths'].map(lambda x: x.replace('_Bath', '')) 
            
            # Contering to Numeric
            listings['baths'] = pd.to_numeric(listings['baths'])
            listings['baths'].unique()
        return listings
    except:
        print('Something went wrong')
        
        
def fix_flex_feature(listings):
    """
    Fixes format issues from flex feature in listings data
    Finally, converts to integer data type
    """
    try:
        if(listings['flexs'].dtype != 'int64'):
            # Removindg  '_' and 'flex' strings
            listings['flexs'] = listings[listings['flexs'].notnull()]['flexs'].map(lambda x: x[1:] if x.startswith('_') else x)
            listings['flexs'] = listings[listings['flexs'].notnull()]['flexs'].map(lambda x: x[1:] if x.endswith('_') else x)
            
            listings['flexs'] = listings[listings['flexs'].notnull()]['flexs'].map(lambda x: x.replace('_Flex_', '')) 
            listings['flexs'] = listings[listings['flexs'].notnull()]['flexs'].map(lambda x: x.replace('_', '')) 
            
            # Filling missing values as 0. None here means no flex in appartment. 
            listings['flexs'] = listings['flexs'].fillna(0) 
            
            # Contering to Numeric
            listings['flexs'] = pd.to_numeric(listings['flexs'])
            

            
        return listings
    except:
        print('Something went wrong')
        
def fix_rent_feature(listings):
    """
    Fixes format issues from rent feature in listings data
    Removes $ and ,
    Finally, converts to integer data type
    """
    try:
        if(listings['flexs'].dtype != 'int64'):
            # Removindg  '$' and ',' from strings and convert to int
            listings['rent'] = listings['rent'].map(lambda x: str(x).replace('$','').replace(',','')).astype('int')  
            
        return listings
    except:
        print('Something went wrong')