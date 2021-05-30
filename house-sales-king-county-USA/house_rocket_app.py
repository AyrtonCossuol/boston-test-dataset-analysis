import pandas as pd
import streamlit as st

st.title('House Rocket Company')

st.markdown('Ealcome to House Rockect Data Analyais')

st.header('Load data')

# read data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['data'] = pd.to_datetime(data['date'])

    return data

#load data
data = get_data('base/kc_house_data.csv')

#plot map
st.title('House Rocket Map')
is_check = st.checkbox('Display Map')

#filters
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_avg = int(data['price'].mean())
price_slider = st.slider('Price Range', 
                        price_min,
                        price_max,
                        price_avg)

if is_check:
    #select rows
    houses = data[data['price'] < price_slider][['id', 'lat', 'long', 'price']]
    st.dataframe(houses)

    #draw map
    