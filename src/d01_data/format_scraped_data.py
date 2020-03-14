import numpy as np 
import pandas as pd 


def build_data_frame(all_pages_parsed):
    """
    Convert parsed data to Dataframe with appropriate column names. 
    Replces 'None' as np.nan
    """
    try:
        listings  = pd.DataFrame(all_pages_parsed, columns=['url', 'address', 'neighborhood', 'rent', 'beds', 'baths', "flexs"],) 
        listings.replace('None', np.nan, inplace=True)
        return listings
    except:
        print('Something went wrong')


def fix_baths_and_flexes(listings):
    """
    We have few flex rooms values, thats why some of bath is skewed to next column.
    This functions fixes this problem.
    """
    try:
        listings["flexs"], listings["baths"] = np.where(listings["flexs"].notnull() , 
                                                      [listings["baths"], listings["flexs"]], 
                                                      [listings["flexs"], listings["baths"]])
        return listings
    except:
        print('Something went wrong')