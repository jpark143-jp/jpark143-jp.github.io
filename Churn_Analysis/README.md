# Business Question 
How to best predict who(customer) is going to churn so that the bank can proactively go to him and provide them better services beforehand

# Dataset
Data has been retreived from Kaggle(https://www.kaggle.com/sakshigoyal7/credit-card-customers) and it is orginated from the URL(https://leaps.analyttica.com/home).
This dataset consists of 10271 customer data including their Attrition Status(Attrited/Existing) which I have used for response variable, and eighteen features describing their salary, age, transaction amount, and etc.

# Methodology
### Data Pre-processing 
![EDA](/Churn_Analysis/image/EDA.PNG)
<br/>After implementing the checking of missing data, what I have found out was there is no missing values in this dataset.
Among 18 features, 5 were categorical and 14 were numerical variables. Plotting the numerical variables, some of those features such as Customer’s age and Months_on_book were nearly normally distributed, and some of them were skewed, 
but I have decided not to make any transformation or manipulation since they were good enough. 
Constructing heatmap for the numerical variables, what was observed is that there was not a significant multicollinearity between the variables, because the plot was filled mostly violet except diagonal. 
For the feature engineering, we first needed to encode categorical variables to better represent the data and so the machine can understand and interpret. 
Slightly different methods of categorical encoding, label encoding and one-hot-encoding, were used for the response variable and other categorical variables.

# Assumptions/Simplifications
The primary assumptions made in our analysis is that we reduce the dimension by removing three columns regarding client number, Naive bayes ratios(two of them). We can assume that those are unnecessary for the prediction and analysis.
Also, while the pre-processing we found out that some of our numerical features are skewed, but we can assume that random forest can handle those as well as categorical features that are ordinal or nominal. 
Here, we also assumed that we are given $200K of budget spending on purpose of boosting up our Return On Investment, as a result of predicting churning customers.

### Modeling Approach
Splitting the encoded data into two parts, train and test datasets, train dataset was fit to the baseline model which is logistic regression. 
Logistic regression was chosen just because of the binary repsonse variable, as it is useful in explaining the relationship between binary response variable and nominal/ordinal independent variables.
Fitting trainset to logistic regression using 'LogisticRegression()' using sklearn package and scoring testset from that model, AUC ROC, recall and specificity are showed as a result.
![Figure1](/Churn_Analysis/image/Figure1.PNG)
<br/>Figure1 shows a confusion matrix which indicates true negative, true positive, false negative, and false positive values that are 165, 1637, 165, 59, respectively. 
Calculated with those values, area under ROC curve is 0.73, recall is 0.96, and specificity is 0.5.
Having specificity as low as 0.5, even though having recall as high as 0.96, logistic regression is not a perfect model for the prediction and not suitable especially in this business case.
The reason why it is best to u se specificity(TN/TN+FP) is best explained by the fact that predicting churning customers as non-churning critically matters in the business. 
Meanwhile, recall(TP/TP+FN) is relatively less important in this project in that predicting non-churning customers as churning does not critically affects the business.
<br/>
![Figure2-1](/Churn_Analysis/image/Figure2-1.PNG)
<br/>As can be seen in Figure 2-1, coefficient values for each feature generated from logistic regression provide a basis for a feature importance score. 
The positive scores indicate a feature which predicts Exisiting customers, whereas the negative scores indicate a feature that predicts churning customers. <br/>
![Figure2-2](/Churn_Analysis/image/Figure2-2.PNG)
<br/>Figure 2-2 shows the sorted coefficients for each features. 
Change in transaction count (Total_Ct_Chng_Q4_Q1), total number of products held by the customer(Total_Relationship_Count), 'Gender_Male' are the primary features which has high positive coefficients, explaining the existing customers. 
On the other hand, the number of months inactive in the last 12 months(Months_Inactive_12_mon), the number of contacts in the last 12 months(Contacts_Count_12_mon), and 'Gender_Female’ are also primary features which has negative cofficients explaining churning customers.
Furthermore, a probability of churning can be calculated from the logistic transformation of added effects.
For example, for a certain customer who is a woman, who has three change in transaction count, two contracts, and so on, an added effects is -0.49(Gender_F)+3*0.74(change in_trans_count)-2*0.57(Contacts_Count)+… and so on.
If the added effect is 2, log transformation gives a probability = 1/(1+exp(-2))=0.88 which means that customer having those features has 88% chance of "Existing".
Nonetheless, again, logistic regression performs risky from its low true negative rate(specificity).

Random Forest has been performed next, as having many incidental features after the categorical encoding and as it can deal with nonlinearities better than logistic regression.
Also, it has been chosen for the ranking of the feature importance in that it is easy to measure the relative importance of each feature on the prediction. 
Using built-in function from sklearn package, Random Forest showed 0.96 accuracy, 0.93 cross-validation score, AUC ROC(Area under ROC curve) 0.89, 0.97 F-1 score, 0.98 recall score, and 0.79 specificity.
The new model has been improved compared to the baseline model not only having higher AUR ROC, F-1 score, and recall, but also having greater increase in true negative rate.<br/>
![Figure3](/Churn_Analysis/image/Figure3.PNG)
<br/>Figure3 shows a confusion matrix which indicates true negative, true positive, false negative, and false positive values that are 258, 1675, 72, 21, respectively. 
Calculated with those values, specificity, as increased to 0.79, suggests that correctly predicting churning customers among the ones who is, in fact, churning is as high as 0.79.
![Figure4](/Churn_Analysis/image/Figure4.PNG)
<br/>Figure 4 shows the feature importance of Random Forest model, presenting its top fifteen features. 
Total transaction amount for last 12 months(Total_Trans_Amt), total transaction count for last 12 months(Total_Trans_Ct), and total revolving balance on the credit card(Total_Revolving_Bal) are the primary features for the model prediction.
Change in transaction count(Total_Ct_Chng_Q4_Q1) and total number of products held by the customer(Total_Relationship_Count) are ranked 3rd and 5th on the figure, although the 5th one has fairly low importance.

# Results
### Key findings and Recommendations
Logistic regression is not a perfect model in that the true negative rate is only 0.5.
Random Forest performed way better showing 0.96 accuracy, AUC ROC(Area under ROC curve) 0.89, 0.97 F-1 score, 0.98 recall score, and 0.79 specificity. 
The total transaction amount for last 12 months, total transaction count for 12 months, change in transaction count, and total revolving balance on the credit card are the primary features of our final model which must be considered in the business.
Recommendation is to use random forest model than logistic regression, and it is recommended to assume we have a budget of $200k  and consider how we can plan that budget in accordance with the model prediction.

### Concrete advice on how business would use the model -- and model output to answer the business question.
Our pre-assumed budget of $200k can be seperated into two parts, customer acquisition cost and customer retention cost.
False positive value which predicts disengaging customers as existing is highly related to customer acquisition cost(CAC). For the customers our model wrongly predicts that they will exist, we would have to work on customer acquisition because those are the ones we need to make up for. 
Meanwhile, false negative and true negative values which are associated with engaging customers are highly related to customer retention cost(CRC).  For the customers our model predicts that they will churn, we need to work on customer retention, to keep them from leaving
Therefore, the calculated ratio of customer retention cost to acquisition cost comes out to be about 1 to15, which makes $187.5K for customer retention cost, and $12.5K for customer acquisition cost. It can be easily calculated from the confusion matrix. 
Our model suggests the fact on how we will spend our customer retention; the less the total number of transactions and their amount, they are more likely to churn, and the more the change in transaction count and total revolving balance, they are also, more likely to churn. 
Therefore they are our target customers. For them, my suggestion is to reward customers by giving them discounts, exclusive or special offers, and generate marketing campaigns, messaging and offers at least once every thirty days
For the customer acquisition cost, even though we have a lower budget than we have for retention, a schematic plan of viral marketing is highly recommended.
Eventually, these budget plan will maximize Return On Investment.

### How business should act on model output from example input
The output is "1" when the customer is predicted to stay in the bank, and the output is "0" when the customer is predicted to churn from the bank.  
The bank manager is recommended to treat it as a total effect of the input, which is the combination of the features dealt by our final model. 
Use the model and its predicted output to actually plan on budgetting customer retention and customer acquisition.

# Potential next steps or further research topics
We can consider trying other models such as XGBoost as it has the powerful performance, and we can use some oversampling method as our data is actually imbalanced as the 80% of the data are 'Existing Customers'.

# Input Spec 
## Sample customer readable input spec
#### {"Customer_Age":54, <br/>"Dependent_count": 1, <br/>"Months_on_book": 40, <br/>"Total_Relationship_Count": 2, <br/>"Months_Inactive_12_mon": 3, <br/>"Contacts_Count_12_mon": 1, <br/>"Credit_Limit": 1438.3, <br/>"Total_Revolving_Bal": 808, <br/>"Avg_Open_To_Buy": 630.3, <br/>"Total_Amt_Chng_Q4_Q1": 0.997, <br/>"Total_Trans_Amt": 705, <br/>"Total_Trans_Ct": 19, <br/>"Total_Ct_Chng_Q4_Q1":	0.9, <br/>"Avg_Utilization_Ratio": 0.562,  <br/>"Gender": F, <br/>"Education_Level": Graduate, <br/>"Marital_Status": Married, <br/>"Income_Category": Less than $40K, <br/>"Card_Category" : Blue}

Variable | Meaning
-------- | ------- 
Customer_Age | Customer's Age in Years <br/>
Dependent_count | Number of dependents <br/>
Months_on_book | Period of relationship with bank <br/>
Total_Relationship_Count | Total no. of products held by the customer <br/>
Months_Inactive_12_mon" | No. of months inactive in the last 12 months <br/>
Contacts_Count_12_mon" | No. of Contacts in the last 12 months <br/>
Credit_Limit | Credit Limit on the Credit Card <br/>
Total_Revolving_Bal | Total Revolving Balance on the Credit Card <br/>
Avg_Open_To_Buy | Open to Buy Credit Line (Average of last 12 months) <br/>
Total_Amt_Chng_Q4_Q1 | Change in Transaction Amount (Q4 over Q1) <br/>
Total_Trans_Amt | Total Transaction Amount (Last 12 months) <br/> Total_Trans_Ct | Total Transaction Count (Last 12 months) <br/> Total_Ct_Chng_Q4_Q1 | Change in Transaction Count (Q4 over Q1) <br/>
Avg_Utilization_Ratio | Average Card Utilization Ratio <br/>Education_Level | Educational Qualification of the account holder <br/>
Marital_Status | Married, Single, Divorced, Unknown <br/>
Income_Category | Annual Income Category of the account holder (< $40K, $40K - 60K, $60K - $80K, $80K-$120K, > $120K, Unknown) <br/>
Card_Category | Type of Card (Blue, Silver, Gold, Platinum)

# Output
### Output is a predicted outcome variable, Attrition_Flag, and 1 indicates "Existing" while 0 indicates "Attritted". <br/> Attrition_Flag : {"Existing":1, "Attrited":0} <br/> Attrition_Flag : Internal event (customer activity) variable 

# Architecture Diagram
![Architecture_Diagram](/Churn_Analysis/image/Architecture_diagram.PNG)

# Instructions for running code 
## Sample input to put on your command line.
python main.py 54 1 40 2 3 1 1438.3 808 630.3 0.997 705 19 0.9 0.562 F Graduate Married 'Less than $40K' Blue
<br/>
#### Notice : For 15th~19th values must be one of the followings; Other than that, it will show an error with 'Wrong Input'<br/> Gender: M, F <br/> Education_Level : College, Doctorate, Graduate, High School, Post-Graduate, Uneducated, Unknown <br/> Marital_Status: Married, Single, Divorced, Unknown <br/> Income_Category: $120K +, $40K - $60K, $60K - $80K, $80K - $120K, Less than $40K, Unknown <br/> Card_Category: Blue, Gold, Platinum, Silver

## OS type and version
   macOS Mojave version 10.14.5
## Anaconda and Python versions
   conda 4.9.2 python3.8.8
## Instructions to run the code
   First, Download the 'final' folder on your repository.
   On command line, change directory to 'final' folder and put my sample input either on this file or in the doctring of main.py
## Instructions to accept input
   Important Notice (1) : For the Categorical input, only one of the pre-mentioned options for 5 categorical features can be a candidate. Other than that, it will show an error with 'Wrong Input' <br/>
   Important Notice (2) : For the Income Category which is 18th value of input, it has to be quotated with '' because it contains symbols like +.
