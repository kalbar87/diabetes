# Diabetes Prediction

## Table of Contents
- [Overwiev](#overview)
- [Screenshot](#screenshot)
- [Learning Objective](#learning-objective)
- [Tools and Software Requirements](#tools-and-software-requirements)
- [Packages Requirements](#packages-requirements)
- [Instalation](#instalationn)
- [Model](#model)
- [Results](#results)

## Overview
Project contains exploratory data analysis and building machine laerniang models based on Pima Indians Diabetes dataset. 

Here is a brief description of the features in the Pima Indians Diabetes Dataset:

Pregnancies: Number of times the patient has been pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skin fold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: Diabetes pedigree function
Age: Age in years
Outcome: Class variable (0 or 1), where 1 indicates that the patient has diabetes and 0 indicates that the patient 
does not have diabetes.

## Screenshot
![Screenshot](/Images/app_screenshot.png)

## Learning Objective
- Data gathering
- Cleaning data
- Exploratory data analysis
- Feature engineering
- Data Preprocessing
- Data Visualization
- Data Modelling
- Model Evaluation
- Model Deployment


## Tools and Software Requirements
- [Github Account](https://github.com/)
- [Github CLI](https://cli.github.com/)
- [VS Code IDE](https://code.visualstudio.com/)
- [Jupyter](https://jupyter.org/)
- [Python3.8](https://www.python.org/downloads/release/python-380/)

## Packages Requirements
- Numpy
- Pandas
- Matplotlib
- Sciki-Learn
- Streamlit
- Seaborn

## Instalation
1. Clone repository git clone https://github.com/kalbar87/diabetes.git
2. Navigate to the project directory: cd diabetes
3. Install dependencies: pip install -r requirements.txt
4. Run the project: streamlit run app.py

## Model

 Random Forest Classifier is a machine learning algorithm used for classification tasks. It is an ensemble method that combines multiple decision trees to improve the accuracy and robustness of the model.

The Random Forest algorithm works by creating a set of decision trees, where each tree is trained on a random subset of the data and a random subset of the features. During training, the algorithm selects a random subset of the data and features for each tree, and each tree is trained on this subset. The algorithm then combines the predictions of all the trees to make the final classification decision.

## Results

Classification Report

|            |precition|   recall| f1-score| support|
|-----------:|--------:|--------:|--------:|-------:|
|           0|     0.93|     0.88|     0.90|      99|
|           1|     0.80|     0.87|     0.83|      55|
|            |         |         |         |        |
|    accuracy|         |         |     0.88|     154|
|   macro avg|     0.86|     0.88|     0.87|     154|
|weighted avg|     0.88|     0.88|     0.88|     154|

![Screenshot](/Images/confussion_matrix.png)