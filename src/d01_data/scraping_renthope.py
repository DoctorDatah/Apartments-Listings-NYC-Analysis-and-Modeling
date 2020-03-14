import requests 
import html5lib
import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup 
from IPython.display import clear_output



def scrap_pages(number_pages = 100):
    """
    Scrapes data from renthop.com
    """
    try:
        url_prefix = "https://www.renthop.com/search/nyc?max_price=50000&min_price=0&page=" 
        page_no = 1 
        url_suffix = "&sort=hopscore&q=&search=0" 
        all_pages_parsed = []

        for i in range(number_pages):

            target_page = url_prefix + str(page_no) + url_suffix

            # Cleart the ouput and then print new one
            print(target_page)
            clear_output(wait=True)

            r = requests.get(target_page)

            soup = BeautifulSoup(r.content, 'html5lib')

            listing_divs = soup.select('div[class*=search-info]')

            one_page_parsed = parse_data(listing_divs)

            all_pages_parsed.extend(one_page_parsed)

            page_no += 1

        print("Completed")
        return all_pages_parsed
    except:
        print('Something went wrong')
        
        
def parse_data(listing_divs): 
    """
    Helper Function for scrap_pages()
    """
    try:
        listing_list = [] 
        for idx in range(len(listing_divs)): 
            indv_listing = [] 
            current_listing = listing_divs[idx] 
            href = current_listing.select('a[id*=title]')[0]['href'] 
            addy = current_listing.select('a[id*=title]')[0].string 
            hood = current_listing.select('div[id*=hood]')[0].string.replace('\n','') 

            indv_listing.append(href) 
            indv_listing.append(addy) 
            indv_listing.append(hood) 

            listing_specs = current_listing.select('table[id*=info] tr') 
            for spec in listing_specs: 
                try: 
                    values = spec.text.strip().replace(' ', '_').split() 
                    clean_values = [x for x in values if x != '_'] # Not getting  '_' these values 
                    indv_listing.extend(clean_values) 
                except: 
                    indv_listing.extend(np.Unknownn) 
            listing_list.append(indv_listing) 
        return listing_list 
    except:
        print('Something went wrong')