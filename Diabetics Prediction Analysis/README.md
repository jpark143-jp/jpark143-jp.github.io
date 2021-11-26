# Business Question
How to best predict Type 2 Diabetes using Logistic Regression

# Dataset
Data has been retreived from Kaggle(https://www.kaggle.com/tigganeha4/diabetes-dataset-2019)
This dataset consists of 952 rows including "Diabetic", response variable, and 17 columns of features. 

Variable | Type | Responses
-------- | ---- | ---------
Age | Categorical | Age brackets(4) <br/>
Gender | Categorial | Male/Female   <br/>
Family | History Categorical | Yes/No <br/>
High Blood Pressure | Categorial | Yes/No <br/>
Physically Active | Categorical | None/Some/Moderate/High <br/>
BMI | Numeric | Numeric <br/>
Smoking | Categorical | Yes/No <br/>
Alcohol Consumption | Categorical | Yes/No <br/>
Hours of Sleep | Numeric | Numeric <br/>
Sound Sleep | Numeric | Numeric <br/>
Regular Medicine | Categorical | Yes/No <br/> 
Junk food | Categorical | Yes/No <br/> 
Stress | Categorical | No/Sometimes/Often/Always <br/>
BP Level | Categorical | High/Normal/Low <br/>
Pregnancies | Numeric | Numeric <br/>
Gestational diabetes | Categorical | Yes/No <br/>
Frequent Urination | Categorial | Yes/No <br/>

# Methodology
### Data Pre-processing 
Creating a simple loop helped us navigate NA values and 47 of them were removed out.  As we have 14 categorical variables, label encoding was performed using "recode()" function in dplyr package in a simple and intuitive manner.

### Exploratory Data Analysis
As can be seen in Figure1, numerical variables such as BMI, Sleep, SoundSleep, and Pregancies are plotted by Diabetic as probability density functions.  Only Pregancies are skewed and other variables are well-distributed as close to normal distribution. 
<br/>![Figure1](/Diabetics_Prediction_Analysis/image/Figure1.png)

Figure2 shows side-by-side barplots for every categorical variable against Diabetic.  Considering we have about 70% of factor "no" and 30% of factor "yes" for Diabetic in total, we can grasp a general idea of data from these plots. 
<br/>![Figure2](/Diabetics_Prediction_Analysis/image/FIgure2.png)

### Random Forest
Even though Random Forest is more complicated model compared to logistic regression, this time we use it as feature selection method before we perform logistic regression as this project is aimed at logistic regression and its prediction. 
The gini index has effectively demonstrated the order of feature importance as shown in Figure3. This shows that people taking regular medicine and age are the two most powerful predictors, followed by BMI and BP. The real surprise here is Smoking, which is the lowest predictor. This https://www.cdc.gov/tobacco/data_statistics/sgr/50th-anniversary/pdfs/fs_smoking_diabetes_508.pdf CDC article makes it very clear that smoking increases risk of diabetes by 30-40%. We should check the odd-ratio of smoking and see if it is 1.3-1.4.
For the final glm, it is recommended to cut off at Pregnancies, guessing we will still get 90% accuracy. 
<br/>![Figure3](/Diabetics_Prediction_Analysis/image/Figure3.png)

### Logistic Regression
Splitting the encoded data into two parts, train and test datasets, train dataset was fit to logistic regression. Logistic regression was chosen for this dataset because of the binary repsonse variable, as it is useful in explaining the relationship between binary response variable and nominal/ordinal independent variables. 'glm()' function is best for logistic regression and we start with fitting the features we have retrieved from the result of random forest feature importance. After checking interaction plot as shown in Figure4, the slopes of the lines are different, so there is interaction between people who are on a regular medicine treatment and Physically
Active. Additionally, for people who exercise for one hour or more (3), the odds of diabetic type II increases much faster if a person take medicine regularly compared to someone who exercises for less than 30 mins.Therefore, we decided to add this interaction term to our final model. 
<br/>![Figure4](/Diabetics_Prediction_Analysis/image/Figure4.png)
<br/>After adding an interaction term we have implemented a backward elimination to achieve our final model. Our final model showed its great improvement in AIC as having 559.75 at first and reduced down to 532.42. Figure5 shows log of odds coefficients from the summary of our model. 
<br/>![Figure5](/Diabetics_Prediction_Analysis/image/Figure5.png)

# Results
### Key Findings
Odds ratios are used to compare the relative odds of the occurrence of the outcome of interest, especially in cases of disease or disorder. As shown in Figure6, model odds ratio has been measured followed by its 95% confidence intervals.   
<br/>![Figure6](/Diabetics_Prediction_Analysis/image/Figure6.png)
<br/>Figure7 is an odd ratio plot effectively demonstrates odd ratios by each features in our final model. <br/>
- The odds of having diabetes is 6.56x more than for participants aged >40 than participants aged <40  <br/>
- The odds of having diabetes is 25% lower for someone who does some sort of physical activity compared to participants who do not.<br/>
- The odds of having diabetes is 2.41x higher for someone who takes medicine regularly over someone who does not <br/>
- The odds of having diabetes is 6.47x higher for someone who has high BP over someone who has low blood pressure <br/>
- The odds of having diabetes is 26% higher for every extra hour of sound sleep over someone who does not have sound sleep <br/>
- The odds of having diabetes is 2.81x higher for someone who has a family history of diabetes over someone who does not <br/>
- The effect of someone taking medicine regularly on diabetes is not similar for different levels of physical activeness. 
As people have higher active levels the odds of having diabetes becomes more for people who take medicine regularly.
![Figure7](/Diabetics_Prediction_Analysis/image/Figure7.png)
<br/> As shown in Figure8, we have plotted interaction effects. Looking at those plots, we notice that the odds of Type II Diabetes
and BP level/Hours of SoundSleep are positively related. In addition, we see that the effect of Regular Medicine
on Type II Diabetes varies with Physically Active level.
![Figure8](/Diabetics_Prediction_Analysis/image/Figure8.png)

### Evaluation
Figure8 is an ROC Curve where we can get AUC(Area Under the Curve) of 0.97. 
<br/>![Figure9](/Diabetics_Prediction_Analysis/image/Figure9.png)
<br/>Figure10 shows a confusion matrix in which we can achieve accuracy of 0.923, sensitivity of 0.97, and specificity of 0.90. 
<br/>![Figure10](/Diabetics_Prediction_Analysis/image/Figure10.png)
<br/>We have implemented Pearson chi-square goodness-of-fit test as well. The chi-square from Pearson test is 745.3. The critical value of chi- square at 95% (alpha= 0.05) and df of residual = 802 is 868.9, and it is larger than what we got from the Pearson test, so we fail to reject the null hypothesis and conclude that the logistic model fits the data. mmp plot also supports that final model is a good fit for the data as in Figure11. 
<br/>![Figure11](/Diabetics_Prediction_Analysis/image/Figure11.png)

### Conclusion
- Our model shows that there is a combination of subject, health, and behavior predictors that are significant in predicting Type 2 Diabetes, most notably the interaction between regular medicine and physical activity.<br/>
- Our findings align with what is observed in literature- Age and blood pressure are significant predictors of diabetes. We also found that taking regular medicine, which could be a symptom of a genetic illness, can also help predict diabetes. In addition to our model having an accuracy of 0.92, our Type II error is 0.03, which is an important measure for a medical model. <br/>
- Shortcomings: Sample demographic may be limited to that in India, and might not generalize to other countries. Some predictor observations are skewed. <br/>
- Recommendation for Improvement: We have some redundant predictors such as sleep and sound-sleep, and bpLevel and highBP. It might be worth analyzing these some more and removing redundant predictors. Additionally, there is an opportunity to use blockwise regression in addition to the randomforest to find significant predictors.
