# Project_1 : consistency score
One of the brand safety metrics is called ‘consistency score’ and it measures how
consistent the influencer posts the postings including photos and videos. Given the list
of client influencers, I was given a task to get the consistency scores out of those
influencers’ instagram pages. Using python webscraping with some libraries such as
bs4, selenium, I was able to develop automatizing retrievals of consistency scores from
the influencer’s 12 most recent posts.

# Project_2 : payrate calculator
I was given raw data which is not yet cleaned, so I cleaned the data from the raw post
including the information such as race, sexual orientation, engagement rate, industry
focus, follower count, page views with the following pay rates. 
My task was to develop a pay rate calculator which inputs engagement rate, follower counts and page views
then outputs a fee range.
With my professor’s support, I was able to develop a module which generates fee out of
a new data point. One issue was that there were a lot of n/a values, but using mean
correlations, I was able to fill in those missing values with the mean estimations. Also,
the model was multivariate linear regression with a good RMSE.