# Apartments-Listings-NYC-Analysis-and-Modeling

**IN PROGRESS!** 

### Background

For international students it is hard to manage their finances is USA. Especially, when your parents are not super rich and your are not allowed to work more then 20 hours a week. 

Affordable and convenient accommodation is a basic requirement to live in States. As my university is in NJ (Drew University, Madison NJ) and I planing to do summer internship in New York City. It would require me to move to NYC, as commuting from NJ would be a time consuming and less effective. Obviously, am a student and I don't want to spend too much on accommodation. Hence, I decided to support my decision for apartment hunt with data analysis and machine learning molding. 


### Data Source

My first concern was how can I get the data for such analysis?
Well, I decided to scrap web for gathering relevant data. Most websites (like listed below) have strict rules for web scarping. Obviously, because of the reason that they don't others to take competitive advantage from data.  
-	streeteasy.com <br>
-	cityrealty.com <br>
-	zillow.com<br>

Many popular websites have their APIs avalible. <br>
- [zillow.com](zillow.com/howto/api/faq.htm)<br>
It impose some limitations like: access to only historical data and limited number of API calls. <br>
- [realtor.com](https://www.realtor.com/) <br>
Also a good source for the data with different paid plans.

Anyways, if its on the web then its accessible either easily or a hard way. Moreover,I found a real estate website [renthop.com](renthop.com) who's design is simple enough for web scraping without violating their TOS (Term of services). 


##### Data Scraped:
- Url 
- Address
- Neighborhood 
- Number of Beds
- Number of Baths 
- Rent in dollars

More Data
- Zip codes of areas are acquired using **Google maps API** calls. 

##### Website Inference:

![renthopes.com](Images/renthopes.com.png)

#### Outliers:
Most of the Observations are between $2000 to $4200 range. Average rent by zip:<br>
![Outliers](Images/boxenplot_outliers_zip_avg.png)

#### Map of average rent in differnt areas:

Areas with average above 6000 are excluded from the map. As they are outliers and more expensive then usual.

![NYC Map](Images/map1.png)

We can observe that Manhattan is Expensive then other boroughs.

Let's spcecifilly Map on **Manhattan** (neighborhoods):

![Manhattan Map](Images/manhattan_map1.png)

Midtown Manhattan and Upper East Side are expensive as compare to Upper Manhattan.

*BLACK SHADED REGIONS MEANS WE DON'T PLOT ON THAT OR WE DON'T HAVE RELATED DATA.*




