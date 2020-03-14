import numpy as np 
import pandas as pd 
import folium 


def listings_count_neighborhood(listings):
    """
    Group by listings count on neighborhood
    Returns: DataFrame
    """
    try:
        series =  listings.groupby('neighborhood')['rent'].count()
        nhood_listings_count = series.to_frame('count').sort_values(by='count', ascending = False)
        nhood_listings_count.reset_index(inplace=True)
        nhood_listings_count.index = pd.RangeIndex(start=1, stop=len(nhood_listings_count) + 1, step=1)
        nhood_listings_count.head(10)
        return nhood_listings_count
    except:
        print('Something went wrong')
        
        
def add_map_properties(cols,dataset,the_map):
    try:
        folium.Choropleth( 
                geo_data=open(r'data\nyc-zip-code.geojson').read(), 
                data=dataset, 
                columns=cols, 
                key_on='feature.properties.postalCode', 
                fill_color='YlOrRd', 
                fill_opacity=0.7, 
                line_opacity=0.2,
                    legend_name='Average Rent'

                ).add_to(the_map) 
    except:
        print('Something went wrong')
        
def percentage_difference(new,old):
    diff =  (( new - old ) / old )* 100
    return print (str(round(diff,1)) + '%' )