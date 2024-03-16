# data_exploration.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('tips.csv')

def data_exploration_page():
    st.sidebar.title('Tips Dashboard')
    st.title('Data Exploration and Visualization')
    st.sidebar.image('tips.jpg')
    st.sidebar.write('Welcome to the Tips Dashboard. Here you can explore the dataset and visualize the data.')
    st.sidebar.write('')
    st.sidebar.write('Filter your data:')
    cat_filter = st.sidebar.selectbox('Select a Category', [None, 'sex', 'smoker', 'day', 'time'])
    num_filter = st.sidebar.selectbox('Select a numerical value', [None,'total_bill', 'tip'] )
    row_filter = st.sidebar.selectbox('Select a row filter', [None, 'sex', 'smoker', 'day', 'time'] )
    col_filter = st.sidebar.selectbox('Select a column filter', [None, 'sex', 'smoker', 'day', 'time'] )

    st.sidebar.markdown('Make with :heart: by [Ziad Mostafa](https://www.linkedin.com/in/ziadmostafa)')

    # row a
    a1, a2, a3 ,a4, a5 = st.columns(5)

    a1.metric('Total Tips', df['tip'].count())
    a2.metric('max Tips', df['tip'].max())
    a3.metric('min Tips', df['tip'].min())
    a4.metric('Maximum Bill', df['total_bill'].max())
    a5.metric('Minimum Bill', df['total_bill'].min())

    # row b
    st.subheader('Total Bills Vs. Tips')
    fig = px.scatter(df, x='total_bill', y='tip', color = cat_filter, size = num_filter, facet_col=col_filter, facet_row=row_filter)
    st.plotly_chart(fig, use_container_width=True)

    # row c
    c1, c2, c3 = st.columns((4, 3 ,3))

    with c1:
        st.text('Sex Vs. Total Bill')
        fig = px.bar(df, x = 'sex', y = 'total_bill', color = cat_filter, barmode = 'group', facet_col=col_filter, facet_row=row_filter)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.text('Smoker Vs. Non Smoker Vs. Tips')
        fig = px.pie(df, names = 'smoker', values = 'tip')
        st.plotly_chart(fig, use_container_width=True)

    with c3:
        st.text('Day Vs. Tips')
        fig = px.pie(df, names = 'day', values = 'tip', color = cat_filter, hole = 0.4)
        st.plotly_chart(fig, use_container_width=True)