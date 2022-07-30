# Customer Churn Analysis and Prediction

Customer attrition (a.k.a customer churn) is one of the biggest expenditures of any organization. If we could figure out why a customer leaves and when they leave with reasonable accuracy, it would immensely help the organization to strategize their retention initiatives manifold.

Telephone service companies, Internet service providers, pay TV companies, insurance firms, and alarm monitoring services, often use customer attrition analysis and customer attrition rates as one of their key business metrics because the cost of retaining an existing customer is far less than acquiring a new one. Companies from these sectors often have customer service branches which attempt to win back defecting clients, because recovered long-term customers can be worth much more to a company than newly recruited clients.
### Datasource: [Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### App Link: [App deployed on Heroku](https://churn-predict-app.herokuapp.com/)

![pic1](https://user-images.githubusercontent.com/66205648/181985064-8a47136e-2bd4-4902-b099-9e519405d801.png)

![pic2](https://user-images.githubusercontent.com/66205648/181985483-5ea0d3b8-0741-4e98-840a-0e33f92b655f.png)

## Project Outline
- Problem
- Dataset Information
- Data Analysis
- Feature Processing and Feature Engineering
- Machine Learning 
- Model Development
- Prediction/Result
- Dashboard Visualization
- Future Scope
## About Dataset

The dataset was a made up telco subscription data set for a fictional telco company.

**Metadata:**

The dataset is a multivariate dataset in a CSV format.
It has 7043 datapoints and 21 fields or attributes.

**Attribute Information:**

- Gender 1. Male, 2.Female
- Partner 1.Yes, 2.No.
- Dependents 1.Yes, 2.No.
- Phone Service 1.Yes, 2.No.
- Multiple Lines 1.Yes, 2.No, 3.No phone service.
- Internet Service 1.Yes, 2.DSL, 3.Fiber optic.
- Online security 1.Yes, 2.No, 3.No internet service.
- Online backup 1.Yes, 2.No, 3.No internet service.
- Device protection 1.Yes, 2.No, 3.No internet service.
- Tech Support 1.Yes, 2.No, 3.No internet service.
- Streaming TV 1.Yes, 2.No, 3.No internet service.
- Streaming movies 1.Yes, 2.No, 3.No internet service.
- Paperless billing 1.Yes, 2.No.
- PaymentMethod 1.Electronic check, 2.Mailed check, 3.Bank transfer (automatic), 4.'Credit card (automatic)'
- Churn 1.Yes, 2.No.
- Contract 1.Month-to-month,  2.One year, 3.Two year

## Data insights
- Mean Monthly charges is about 64.76 units and 75% of observations are monthly charged around 89.85
- About 50% of customers stayed for 55 months tenure and were charged 70.3 per month
- Most customers with Month-to-month contract and Fibre optic Internet Service churned.
- Customers with Two-year contract and No Internet service have least churn rate.
- Customers who did churn showed a declining trend with increase in tenure period.
- Churn rate is higher for customers with Multiple Lines while those with No Phone Service have least churn rate.


## Model Building
**Applied Machine Learning Models:**
- Decision Tree Classifier
- Random Forest Classifier
- ANN Model

## Dashboard Visualization
![dashpic1](https://user-images.githubusercontent.com/66205648/181995213-c5edda93-9973-4544-84b3-4bb3439c8865.png)

![dashpic2](https://user-images.githubusercontent.com/66205648/181995225-a9da879b-bfda-46fc-9a1f-85a9a89dd8be.png)

## Future Scope
- Share key insights about the customer demographics and churn rate that is garnered from the exploratory data analysis sections to the sales and marketing team of the organization. Let the sales team know the features that have positive and negative correlations with churn so that they could strategize the retention initiatives accordingly.
- Further, classify the upcoming customers based on the propensity score as high risk (for customers with propensity score > 80%), medium risk (for customers with a propensity score between 60–80%) and lastly low-risk category (for customers with propensity score <60%). Focus on each segment of customers upfront and ensure that there needs are well taken care of.
