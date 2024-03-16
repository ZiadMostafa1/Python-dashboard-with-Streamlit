# main.py
import streamlit as st
from prediction_page import prediction_page
from data_exploration import data_exploration_page

PAGES = {
    "Data Exploration and Visualization": data_exploration_page,
    "Model prediction": prediction_page
}

def main():
    st.set_page_config(page_title='Tips Dashboard', page_icon=':moneybag:', layout='wide', initial_sidebar_state='auto')
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()