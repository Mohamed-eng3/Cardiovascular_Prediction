import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data
 
data = load_model()
clf = data["model"]

def show_predict_page():
    st.title("Cardiovascular Prediction")

    st.write("""### We need some information to predict the disease""")

    genders = (1, 2)
    height = st.slider("Height", 0, 200, 1)
    weight = st.slider("Weight", 0, 200, 1)
    bmi = weight/((height/100)**2)
    systolic = st.slider("Systolic BP", 0, 200, 1)
    diastolic = st.slider("Diastolic BP", 0, 200, 1)
    age = st.slider("Age", 0, 80, 1)
    cholesterols = (1,2,3)
    gluc = (1,2,3)
    smokes = (0,1)
    actives = (0,1)


    #Selection Boxes
    gender = st.selectbox("Gender", genders)
    cholesterol = st.selectbox("Colesterol", cholesterols)
    glucose_lvl = st.selectbox("Glucose Range", gluc)
    smoke = st.selectbox("Smoke", smokes)
    active = st.selectbox("Active", actives)


    
    def calc_bmi_class(row):
      if row < 18.5:
        bmi_class = 1
      elif row > 18.5 and row  < 24.9:
        bmi_class = 2
      elif row > 24.9 and row < 29.9:
        bmi_class = 3
      elif row > 29.9 and row < 34.9:
        bmi_class = 4
      elif row > 34.9 and row < 39.9:
        bmi_class = 5
      elif row > 39.9 and row < 49.9:
        bmi_class = 6
      return bmi_class
    
    bmi_class = calc_bmi_class(bmi)
    
    def calc_age_bin(age):
      
      if age < 30:
        age_bin = '0'
      elif age > 30 and age  < 40:
        age_bin = '1'
      elif age > 40 and age  < 50:
        age_bin = '2'
      elif age > 50 and age  < 60:
        age_bin = '3'
      elif age > 60 and age  < 70:
        age_bin = '4'
      
      return age_bin
    
    age_bin = calc_age_bin(age)
       


    ok = st.button("Calculate Salary")
    if ok:
              
        X = np.array([[gender, height, weight, systolic, diastolic, age, age_bin, bmi_class, cholesterol,glucose_lvl,smoke,active]])

        pred = clf.predict(X)
        st.subheader(f"The prediction is {pred[0]f}")
