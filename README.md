# Data Science Immersive - Capstone
## Heart Health Screening Tool: Detecting Risk of Heart Disease 
### Precious Smith
#### *DSIR-22221E, General Assembly, Presented 5.14.21* 


---
## Executive Summary
Heart Disease is the number 1 cause of death in the US accounting for 1 in 4 deaths. More than [655,000 people](https://millionhearts.hhs.gov/learn-prevent/cost-consequences.html) die each year from heart disease complications. Heart disease is a term that encompasses several conditions, and coronary artery disease is the most common. Heart disease can lead to stroke and heart attack and has several associated risk factors. The main 3 risk factors include hypertension (high blood pressure), high cholesterol and smoking, and shockingly, 47% of Americans have at least one of those risks. Other risk factors include diabetes, unhealthy diet, excessive alcohol use, overweight/obesity and physical inactivity, according to the [CDC](https://www.cdc.gov/heartdisease/about.htm). The CDC's [Million Hearts website](https://millionhearts.hhs.gov/learn-prevent/cost-consequences.html) on heart disease lists the ABCS of Heart Health which is an easy way to remember how to lower your risk of heart disease. The ABCS are: Take **aspirin** as directed by a physician, Control your **blood** pressure, Manage your **cholesterol**, and Don't **smoke**.

According to [Psychology Today](https://www.psychologytoday.com/us/blog/how-healing-works/201902/recent-survey-finds-gaps-in-doctor-patient-conversations), "45% of U.S. adults who have a primary care physician (PCP) say they wish they talked with their doctor more about why they want to be healthy, and 57% of people aged 18-44 say they wish their doctor would talk to them about treatments that do not involve medication." To me this means there's a great opportunity to connect patients and doctors and improve the communication between them. I believe we can use data science to help empower patients to initiate informed conversations with their physicians. We can also educate patients on things they should be aware of regarding their general health and equip them with tools to make better decisions for themselves.

This project sets out to do just that by creating a predictive binary classification model using SelectKBest, SMOTEN and Logistic Regression to predict whether or not someone has heart disease and diabetes. I then [create an app](https://share.streamlit.io/psmith19/dsi-capstone/main/heart_app.py) that provides a questionnaire to users and after running the submission through the relevant model it tells the user if they are at risk of developing heart disease or diabetes. It also gives a list of diagnostic tests a user can ask their physician about as well as links to resources for more information about heart disease and diabetes, their risk factors, symptoms and prevention tips. 

---
## Problem Statement
Can we predict whether someone is at risk of heart disease using a few key features, then create an app that informs users of their risk and provides them with test and discussion suggestions to take to their physicians?


## Data Cleaning & EDA
### Data Collection
Data for this project was collected from the sample adult portion of the CDC's annual [National Health Interview Survey](https://www.cdc.gov/nchs/nhis/2019nhis.htm). 

The dataset has 534 features consisting of survey questions regarding various health factors and family and household demographics. There were 31,997 observations. All of the value points, besides the household ID, were integers; however, the data were categorical and represented specific response options given by the respondent. 

Target feature pertains to survey question asking respondents if they'd ever been told they have heart disease.


### Data Dictionary
|Feature	|Type	|Dataset	|Description|
|-	|-	|-	|-	|
|CHDEV_A	|	object	|adult19|	Has the respondent ever been told they have heart disease?	|
|AFNOW_2.0	|	object	|adult19|	Respondent is not currently on full-time active duty in the armed forces	|
|EMPWRKLSWK_A_2	|	object	|adult19|	Respondent did not work last week	|
|MEDICARE_A_3	|	object	|adult19|	Respondent is not on Medicare	|
|OVER65FLG_A_1	|	object	|adult19|	Respondent has one person living in the home who is over 65 years of age	|
|INCSSRR_A_2.0	|	object	|adult19|	Respondent is not receiving retirement income from Social Security or Railroad Retirement	|
|HIKIND02_A_2	|	object	|adult19|	Respondent's health insurance was not mentioned	|
|MIEV_A_2	|	object	|adult19|	Respondent has not been told they had a heart attack	|
|ANGEV_A_2	|	object	|adult19|	Respondent has not been told they had angina	|
|CHLEV_A_2	|	object	|adult19|	Respondent has not been told they have high cholesterol	|
|HYPEV_A_2	|	object	|adult19|	Respondent has not been told they have hypertension	|
|SMKCIGST_A_3	|	object	|adult19|	Respondent is a former smoker	|
|DIBEV_A	|	object	|adult19|	Has the respondent ever been told they have diabetes?	|
|SHTPNUEV_A_2	|	object	|adult19|	Respondent has not received a pneumonia shot	|
|DIABLAST_A_1	|	object	|adult19|	Respondent received a blood sugar test within the last year	|
|RX12M_A_2	|	object	|adult19|	Respondent has not taken prescription medication within the last 12 months	|
|PREDIB_A_2	|	object	|adult19|	Respondent has not been told they have prediabetes	|
|CHDEV_A_2	|	object	|adult19|	Respondent has not been told they have heart disease	|


### Data Cleaning & Processing
- Columns with more than half of values missing were removed.
- Changed datatypes from integer to object except for target column.
- Created dummies for all features excluding target variable.
- Reclassified target variable to binary classification (0=No, 1=Yes).
    - Dropped 103 rows that were not classified as No or Yes.
- Feature Selection
    - Used SelectKBest to find 10 most predictive features
    - Hand-picked 56 features based off research
- Balancing Classes
    - Used SMOTEN to create balanced classes resulting in 45,072 observations for each class
    - Used NearMiss to create balanced classes resulting in 2768 observations for each class


### Exploratory Data Analysis
- Explored target variable in combination with various features to get a feel of the health status of respondents.
- Created distribution charts of various features to see how the number of respondents were broken down by region, sex, race, age, BMI and other features.
- Found that 36% of respondents have hypertension and 13% of those people also have heart disease.
- 29% of respondents have high cholesterol and 14% of them also have heart disease.
- 13% of respondents are current smokers and 9% of those respondents also have heart disease.
- 10% of respondents have diabetes and 18% of those individuals also had heart disease.


## Modeling & Evaluation
### Heart Model
Created several binary classification models while using target variable CHDEV_A for heart disease with variations of SelectKBest vs Hand-picked features and SMOTEN vs NearMiss and Logistic Regression vs Decision Tree vs AdaBoost vs Gradient Boost. Best model used SelectKBest with k=10, SMOTEN and Logistic Regression with default parameters. I chose to maximize accuracy and recall scores to minimize false negatives. I felt this was important since I was dealing with medical data, and I wanted to minimize the people who fall through the cracks with false information. The accuracy score for the heart model was .82 with a recall score of .83 for the positive class. This tells us that the model is correctly predicting positive heart disease 83% of the time.

I tried changing the number of features in SelectKBest, but 10 proved to be the best number of predictive variables for the least amount of misclassifications. Although we minimized false negatives, false positives were still high which could cause it's own concerns. 


### Diabetes Model
Created a few different binary classification models using target variable DIBEV_A for whether a respondent had diabetes. The best model was similar to the heart model with SelectKBest with k=10, SMOTEN and Logistic Regression. This model used C=0.01 instead of the default C=1.0. The accuracy score was .82 with a recall score of .81 for the positive class. This still leaves a lot of room for error. However, for the sake of this project and app at this stage, being accurate 82% of the time is a great improvement over the null model of 50%.


## Heart Health Screening Tool - Streamlit App
Created a Streamlit app using both the heart and diabetes models. App provides basic information about heart disease and diabetes and allows user to select questionnaire with yes/no answers to assess whether they are at risk or not for either disease. App also provides list of tests and topics user can take to physician to discuss their concerns, as well as links to resources to learn more about symptoms, risk factors, and prevention tips.

Heart Health Screening Tool can be found within the files of this repo under filename *heart_app.py* or online [here](https://share.streamlit.io/psmith19/dsi-capstone/main/heart_app.py).


## Conclusions & Limitations
I was able to satisfy the problem statement by creating a model that predicts heart disease risk with 82% accuracy while minimizing false negatives and building an app that takes user input then uses the model to give results and suggestions for tests and informative discussions with a physician. I also expanded the app and included a model that predicts diabetes risk also with 82% accuracy. There are still a number of misclassifications which can give false negatives and false positive results to users which could cause unnecessary worry and distrust in the app. 

Some limitations during the process was the limited data available for relevant diagnostic test scores and possibly more predictive variables. Possibly someone with greater understanding of medical data and heart disease would be able to create a stronger model with the dataset I used. 


### Future Directions
- Moving forward, I would like to improve the model with possibly finding other data sources.
- I would also like to expand the screening tool and include other diseases and conditions beyond heart disease and diabetes.
- I could see this app being used in a doctor's office while patients are in the waiting room waiting to be see by their physician. They could complete the questionnaire and take their results to the nurse and physician and begin a discussion about their concerns.
- It could also be a part of a patient portal as something a patient could complete and submit directly to their physician for feedback at their next visit.


---

## File Structure

```
dsi-capstone
|__ 01_Heart_EDA_Cleaning.ipynb
|__ 02_Heart_KBest_Models.ipynb
|__ 03_Heart_Self-Select_Models.ipynb
|__ 04_Heart_Smoking.ipynb
|__ 05_Heart_Final_Model.ipynb
|__ 06_Diabetes.ipynb
|__ README.md
|__ adult19.csv
|__ adult19_clean.csv
|__ heart_app.py
|__ model_diabetes.p
|__ model_heart.p
|__ presentation.pdf
|__ requirements.txt
``` 
---
## References
https://www.cdc.gov/heartdisease/coronary_ad.htm
https://millionhearts.hhs.gov/learn-prevent/cost-consequences.html
https://www.cdc.gov/heartdisease/about.htm
https://www.cdc.gov/nchs/nhis/2019nhis.htm
https://www.psychologytoday.com/us/blog/how-healing-works/201902/recent-survey-finds-gaps-in-doctor-patient-conversations
