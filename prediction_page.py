# prediction_page.py
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly.graph_objects as go
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Load the LabelEncoder
le = joblib.load('labelencoder.pkl')

def prediction_page():
    st.title('Model prediction')
    st.write('In this page we will predict the tips using the total')

    # Sidebar inputs for model prediction
    total_bill = st.sidebar.number_input('Total Bill', min_value=0.0, max_value=100.0, value=30.0)
    sex = st.sidebar.selectbox('Sex', options=['Male', 'Female'])
    smoker = st.sidebar.selectbox('Smoker', options=['Yes', 'No'])
    day = st.sidebar.selectbox('Day', options=['Thur', 'Fri', 'Sat', 'Sun'])
    time = st.sidebar.selectbox('Time', options=['Lunch', 'Dinner'])
    size = st.sidebar.number_input('Size', min_value=1, max_value=10, value=4)
    
    X = np.array([ total_bill, sex, smoker, day,  time,  size])

    X_df = pd.DataFrame(data=[X], columns=['total_bill', 'sex', 'smoker', 'day', 'time', 'size'])
    st.write(X_df)

    le = LabelEncoder()
    all_unique_values = np.unique(X)  
    le.fit(all_unique_values)
    X = le.transform(X)
    X = X.astype(float)
 
    if st.button('Predict!'):
        predicted_tip = model.predict([X])
        st.write(f"Predicted tip: {predicted_tip[0]:.2f}")

    # model cofficients with plotly
    st.subheader('Model Coefficients')
    bar = go.Bar(x=model.coef_, y=model.feature_names_in_, orientation='h')
    layout = go.Layout(title='Model Coefficients', xaxis=dict(title='Coefficient Value'), yaxis=dict(title='Feature'))
    fig = go.Figure(data=[bar], layout=layout)
    st.plotly_chart(fig, use_container_width=True)

    # model prediction vs actual values
    st.subheader('Model Prediction Vs. Actual Values')
    st.image('model_prediction_vs_actual_values.png', use_column_width=True)
    st.markdown('The model prediction vs. actual values is shown in the image above. The model prediction is shown in blue and the actual values are shown in red.')
    st.write("")
    st.markdown("This model isn't very good :pensive:.")