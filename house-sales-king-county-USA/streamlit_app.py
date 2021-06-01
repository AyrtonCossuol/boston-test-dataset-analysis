import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout = 'wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data

# get data
PATH = 'base/kc_house_data.csv'
data = get_data(PATH)

# add new feature
data['price_m2'] = data['price'] / data['sqft_lot']

# =============================
# Data overview
# =============================
f_attributes = st.sidebar.multiselect('Enter columns', data.columns)
f_zipcode = st.sidebar.multiselect('Enter zipcode', 
                                    data['zipcode'].unique())

st.title('Data Overview')

if f_zipcode != [] and f_attributes != []:
    data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
elif f_zipcode != [] and f_attributes == []:
    data = data.loc[data['zipcode'].isin(f_zipcode), : ]
elif f_zipcode == [] and f_attributes != []:
    data = data.loc[:, f_attributes ]
else:
    data = data.copy()

st.write(data.head())