import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import calendar

def load_model():
    with open('final_model_1.pkl', 'rb') as f1:
        data1 = pickle.load(f1)
    with open('final_model_2.pkl', 'rb') as f2:
        data2 = pickle.load(f2)
    with open('final_model_3.pkl', 'rb') as f3:
        data3 = pickle.load(f3)
    with open('final_model_4.pkl', 'rb') as f4:
        data4 = pickle.load(f4)

    return data1, data2, data3, data4

data1, data2, data3, data4 = load_model()

m1 = data1['model']
m2 = data2['model']
m3 = data3['model']
m4 = data4['model']

e = data1['le_day']

def date_to_day(year, month, date):
    date = datetime.datetime(year, month, date)
    day = calendar.day_name[date.weekday()]
    return day

def show_predict_page():

    st.title("Traffic Prediction")

    st.write("""### We need some information about the date and Junction to predict the traffic.""")
    
    year = {
        2015, 
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024
    }

    month = {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
    }

    date = {
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
    }

    hour = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
    }

    

    junction = {
        1, 2, 3, 4 
    }

    year = st.selectbox("In what year would you be travelling?", year)
    month = st.selectbox("Type in the month", month)
    date = st.selectbox("Type in the date", date)
    hour = st.selectbox("At what approximate hour would you be travelling?", hour)
    junction = st.selectbox("Which Junction would you be following?", junction)

    day = date_to_day(year, month, date)
    day = e[day]

    ok = st.button("Predict Traffic")

    if ok:
        if junction == 1:
            prediction = m1.predict([[year, month, date, hour, day]])
            prediction = int(np.ceil(prediction[0]))
            st.subheader(f"The number of vehicles on the Junction 1 at the given hour are predicted to be {prediction}")

        elif junction == 2:
            prediction = m2.predict([[year, month, date, hour, day]])
            prediction = int(np.ceil(prediction[0]))
            st.subheader(f"The number of vehicles on the Junction 2 at the given hour are predicted to be {prediction}")

        elif junction == 3:
            prediction = m3.predict([[year, month, date, hour, day]])
            prediction = int(np.ceil(prediction[0]))
            st.subheader(f"The number of vehicles on the Junction 3 at the given hour are predicted to be {prediction}")

        elif junction == 4:
            prediction = m4.predict([[year, month, date, hour, day]])
            prediction = int(np.ceil(prediction[0]))
            st.subheader(f"The number of vehicles on the Junction 4 at the given hour are predicted to be {prediction}")            
