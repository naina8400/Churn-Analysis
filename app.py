import streamlit as st 
import pickle
import pandas as pd
import numpy as np
from PIL import Image

st.sidebar.title("Churn Probability of a Single Customer")
html_temp = """
<div style="background-color:#9593D9;padding:10px">
<h1 style="color:white;text-align:center;">Churn Prediction App </h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)
image = Image.open('home_app_pic.png')
st.image(image, caption='churn',use_column_width=True)

df_1=pd.read_csv("Telco-Customer-Churn.csv")
# tenure = st.sidebar.slider("Tenure : Months customer stayed",1,72,12,step=1)
tenure = st.sidebar.number_input("Tenure : Months customer stayed")
MonthlyCharges = st.sidebar.slider("Charge : Amount charged to customer",18.25,118.75,50.00,step = 0.05)
TotalCharges = st.sidebar.slider("Charge : Total Amount charged to customer",18.8,8684.8,4000.00,step = 500.00)  ##


SeniorCitizen = st.sidebar.radio("Senior Citizen", ('Yes', 'No')) ##
gender = st.sidebar.radio("Gender", ('Female', 'Male')) ##
Partner = st.sidebar.radio("Partner", ('Yes', 'No')) ##
Dependents = st.sidebar.radio("Dependents", ('Yes', 'No')) ##
PhoneService = st.sidebar.radio("Phone Service", ('Yes', 'No')) ##
MultipleLines = st.sidebar.radio("Customer`s Multiple Lines", ('No', 'Yes', 'No phone service'))##
Contract=st.sidebar.radio("Contract term", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.radio("Customer`s online security", ('No', 'Yes', 'No internet service'))
OnlineBackup=st.sidebar.radio("Customer`s online backup", ('No', 'Yes', 'No internet service'))##
DeviceProtection=st.sidebar.radio("Customer`s Device Protection", ('No', 'Yes', 'No internet service'))##
StreamingTV =st.sidebar.radio("Is Customer Streaming TV ?", ('No', 'Yes', 'No internet service'))##
StreamingMovies =st.sidebar.radio("Is Customer Streaming Movies ?", ('No', 'Yes', 'No internet service'))##
PaperlessBilling =st.sidebar.radio("PaperlessBilling", ('No', 'Yes'))##
PaymentMethod =st.sidebar.radio("Payment Method", ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))##
InternetService=st.sidebar.radio("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.radio("Customer has tech support?", ('No', 'Yes', 'No internet service'))


my_dict = {
'MonthlyCharges' : MonthlyCharges,
'TotalCharges' : TotalCharges, ##
'tenure' : tenure, ##
# 'tenure-binned': binning_feature('tenure', 7),
'SeniorCitizen' : SeniorCitizen, ##
'gender' : gender, ##
'Partner' : Partner, ##
'Dependents' : Dependents, ##
'PhoneService' : PhoneService, ##
'MultipleLines' : MultipleLines, ##
'Contract' : Contract,
'OnlineSecurity' : OnlineSecurity,
'OnlineBackup' : OnlineBackup, ##
'DeviceProtection' : DeviceProtection, ##
'StreamingTV' : StreamingTV, ##
'StreamingMovies' : StreamingMovies, ##
'PaperlessBilling' : PaperlessBilling, ##
'PaymentMethod' : PaymentMethod, ##
'InternetService' : InternetService,
'TechSupport' : TechSupport}
df = pd.DataFrame.from_dict([my_dict])


new_df = pd.DataFrame(df, columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender',  'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService','OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport','StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod', 'tenure'])
df_2 = pd.concat([df_1, new_df], ignore_index = True) 

labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
df_2['tenure_group'] = pd.cut(df_2.tenure.astype(int), range(1, 80, 12), right=False, labels=labels)

df_2.drop(columns= ['tenure'], axis=1, inplace=True)   
 
new_df_dummies = pd.get_dummies(df_2[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
           'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
           'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
           'Contract', 'PaperlessBilling', 'PaymentMethod','tenure_group']])
         
with open('model_1.pkl', 'rb') as file:  
    model = pickle.load(file)

run = st.sidebar.button("RUN")
if run:
	prediction = model.predict(new_df_dummies)[0]
	if prediction == 1:
		prediction = "Churn Yes !"
		st.sidebar.warning(prediction)
	else:
		prediction = "Churn No"
		st.sidebar.success(prediction)

st.cache()
dfshow = pd.read_csv("Telco-Customer-Churn.csv",index_col=0)

if st.checkbox('Select Random Customers'):
	num = st.slider("Number of random Customers to display",1,dfshow.shape[0],1,step=24)
	selection = dfshow.iloc[np.random.randint(dfshow.shape[0], size=num)]
	st.success(f"Churn probability of {num} randomly selected customer")
	st.table(selection)

