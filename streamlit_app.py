import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('model.pkl','rb'))
encoder = pickle.load(open('target_encoder.pkl','rb'))
transformer = pickle.load(open('transformer.pkl','rb'))

st.title("Insurance Premium Prediction")


## for Gender Column
sex = st.selectbox('Please select gender', ('male', 'female'))


## for age Column
age = st.text_input('Enter Age', 18)
age = int(age)


# for BMI Column
bmi = st.text_input('Enter BMI', 18)
bmi = float(bmi)


## for children Column
children = st.selectbox('Please select number of children ', (0,1,2,3,4,5))
children = int(children)


## for smokers Column
smoker = st.selectbox('Please select smoker category ', ("yes","no"))


## for region Column
region = st.selectbox('Please select region ', ("southwest", "southeast", "northeast", "northwest"))


l = {}
l['age'] = age
l['sex'] = sex
l['bmi'] = bmi
l['children'] = children
l['smoker'] = smoker
l['region'] = region

df = pd.DataFrame(l, index=[0])

df['region'] = encoder.transform(df['region'])
df['sex'] = df['sex'].map({'male':1, 'female':0})
df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

df = transformer.transform(df)
y_pred = model.predict(df)


if st.button("Show Result"):
    st.header(f" Insurance Prediction is  {round(y_pred[0],2)} INR")