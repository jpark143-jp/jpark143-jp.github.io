# Business Question
How the COVID-19 outbreak affected airline industries on many grounds? 

# Dataset
Several datasets have been handled. S&P 500 stock data was retrieved from Yahoo Finance using Shiny App which scrapes all 
the stock prices with tickers and generates a dataframe.  Hence, 'industrial ticker' datasets consists of 'symbol' of each 
company's ticker and corresponding close stock price for a certain period of time, 2019-12-05 through 2020-05-04. 

variable | meaning | value
-------- | ------- | -----
symbol | ticker of company | MMM, ALK, ... 
date | date | One of 2019-12-05 through 2020-05-04 
close | close stock price | numeric
<br/>
'mobility' dataset consists of 11 columns, but we have used only the dates and mean mobility values(represented by percent
change in mobility in each sector) to compare with the stock prices joining by the dates. <br/>

variable | meaning | value
-------- | ------- | -----
country_region_code | Abbreviation of Country | AE(Arab Emirates), ZW(Zimbabwe), ... 
country_region | Country's full name | United Arab Emirates, ...
date | date | One of 2020-2-15 through 2020-05-02
grocery_and_pharmacy_percent_change_from_baseline | grocery and pharmacy percent change in mobility| numeric
retail_and_recreation_percent_change_from_baseline | retail and recreation percent change in mobility | numeric
parks_percent_change_from_baseline | park percent change in mobility | numeric
transit_stations_percent_change_from_baseline | statation percent change in mobility | numeric 
workplaces_percent_change_from_baseline | workplaces percent change in mobility | numeric
residential_percent_change_from_baseline | residential percent change in mobility | numeric
<br/>
Just like S&P 500 Stock tickers dataset, airline companies stock prices datasets were handled, and there are more detailed
prices such as adjusted return prices and volume other than open and close prices.

variable | meaning | value
-------- | ------- | -----
symbol | ticker of company | AAL(American Airline),...  
date | date | One of 2019-12-06 through 2020-05-05  
open | open stock price | numeric
high | highest daily stock price | numeric
low | lowest daily stock price | numeric 
close | close stock price | numeric
volume | stock volume | numeric
adjusted | adjusted stock return | numeric

'airfreight' dataset was retrieved from a Yahoo finance() ticker of Fedex, UPS, C.H. Robinson, Expeditors International of Washington, with S&P 500.

variable | meaning | value
-------- | ------- | -----
date | date | One of 2010-01-01 through 2020-05-02
^GSPC | stock price of S&P 500 | numeric
CHRW | stock price of C.H. Robinson Worldwide, Inc. | numeric
EXPD | stock price of Expeditors International of Washington | numeric
FDX | stock price of FedEx | numeric
UPS | stock price of UPS | numeric

# Methodology
### Data Processing 
 We used web scraping technique to retrieve the data using Shiny App(http://shiny.stat.ucla.edu:3838/c183c283/) as well.
The raw data retrieved from all over the web was at first very messy so we needed to handle with missing values, and date
time components were not in a correct form so we needed to work on feature engineering. It was very important as our primary
methodology was time series analysis on the stock price.
  
### Exploratory Data Analysis
 We first started to take a look with its stock data. We retrieved the daily stock price data of S&P 500 companies from 
Yahoo Finance and calculated how much return of investment each industry had on average. As we can see, the airline industries 
had a huge negative return of investment, while having a small variance compared to other industries for which we suspected 
to be correlated with physical distancing and reduced mobility. On the graph on the left hand side, we plotted how the 
mobility and stock prices had been changing in the last three months, and we figured that they had a very similar trend.
<br/>![Figure1](/Datafest/image/image01.png)
<br/>![Figure2](/Datafest/image/image02.png)
<br/>![Figure3](/Datafest/image/image03.png)

### Model Approach : Time Series Analysis on airline stock price, social distancing, and air-freight data 
 Most of the airline companies are acting in the same way, so we picked United Airline which has the highest correlation 
with COVID impact. We predicted its stock price and revenue and observed unnatural depreciation as soon as it became 2020. 
Google trend data revealed international travel has decreased for 70% and domestic flight has decreased for average 40%, 
obviously due to the social distancing and rapid worldwide spread of COVID-19. After investigating COVID impact on 
airline companies and LAX, we sought for alternative strategies on how airline companies make profit.
<br/>![Figure4](/Datafest/image/image04.png)
<br/>![Figure5](/Datafest/image/image05.png)
<br/> To clarify, we simplified the total passenger count of the left hand side. Middle plot illustrates the scaled 
count of cargo transported and aircraft operations in total. Due to the seasonality, cargo has its lowest points in February, 
but it bounced back to it's usual routine in March. From the effect of social distancing and decreased industrial activities, 
cargo also somewhat decreased compared to previous years. But for the aircraft operations, counts have drastically decreased 
ever since the pandemic arises. This made air-freight fees to be more expensive than usual. Oil prices are currently at 
their lowest point, so airline companies are using passenger aircraft as a cargo carrier to make some profit but this is 
still not enough for them.
<br/>![Figure5](/Datafest/image/image06.png)

# Conclusion
 Our analysis suggests that the biggest collapse in terms of stock return and revenue was airline industry 1 with showing 
the large gap between its actual and predicted values.  The high correlation between workplace mobility and stock price 
of airline industries has led the further analysis of the airport passenger count and social distancing. A strong negative 
correlation between the airport passenger count and social distancing value at its peak point 1 proposes that travel count 
as explained by the airport passenger count 1 increases as the social distancing value shows its decreasing trend after 
its peak.  The rise in the demand in cargo with the reduction in the flight operation and its passenger count implies the 
airline companies are replacing the passengers with the air-freights. 

# References
yfinance: https://pypi.org/project/yfinance/  <br/>
covid19py: https://pypi.org/project/COVID19Py/  <br/>
Google trend: https://trends.google.com/trends/?geo=US  <br/>
Cargo & Aircraft Operations: https://www.lawa.org  <br/>
Stock Data: http://shiny.stat.ucla.edu:3838/c183c283/  <br/>
Jet Fuel Price: https://www.iata.org/en/publications/economics/fuel-monitor/  <br/>
10-Q: https://www.sec.gov  <br/>
Mobility: https://www.google.com/covid19/mobility/  <br/>
COVID-19 data:https://coronavirus.jhu.edu/map.html