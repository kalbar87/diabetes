# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:56:57 2023

@author: michalk
"""

import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class diabetes:
    def __init__(self, df):
        self.df = df
    
    def predict(self, df, model):
        prediction = model.predict(df)[0]
        print(prediction)
        if prediction==0:
            st.success('You are not Diabetes')
        elif prediction==1:
            st.error('You are Diabetes')


data = pd.read_csv('diabetes.csv')

st.header('Do you have diabetes ?')


pregnancies = st.slider('Pregnancies',0,17)
glucose = st.number_input('Glucose', 0,200)
skin_thickenss = st.number_input('Skin Thickness', 0,100)
insulin = st.number_input('Insulin',0,900)
bmi = st.number_input('Bmi', 0,70)
age = st.number_input(('Age'), 0 ,100)

X = np.array([pregnancies, glucose, skin_thickenss, insulin,  bmi, age])
columns = ['Pregnancies', 'Glucose', 'SkinThickness', 'Insulin', 'BMI', 'Age']
df = pd.DataFrame([X], columns=columns)
model = pickle.load(open('model.pkl', 'rb'))


db = diabetes(data)

if st.button('Calculate'):
    db.predict(df, model)
    





