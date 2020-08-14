"""
THIS PROJECT GOAL IS TO DEMONSTRATE THE CAPABILITY OF STREAMLIT TO BUILD AN PYTHON APPLICATION
"""
import streamlit as st
import pandas as pd
import numpy as np
from dateutil.parser import parse



time_series_covid19_confirmed_global= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
time_series_covid19_confirmed_US = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
time_series_covid19_deaths_US = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
time_series_covid19_deaths_global = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
time_series_covid19_recovered_global = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
#Create DF from csv files
#confirmed_US = pd.read_csv(time_series_covid19_confirmed_US)
#confirmed_global = pd.read_csv(time_series_covid19_confirmed_global)
#deaths_US = pd.read_csv(time_series_covid19_deaths_US)
#deaths_global = pd.read_csv(time_series_covid19_deaths_global)
#recovered_global = pd.read_csv(time_series_covid19_recovered_global)


def load_df(name):
  if name == 'US Confirmed':
    returned_df = pd.read_csv(time_series_covid19_confirmed_US)
  elif name == 'Golbal Confirmed':
    returned_df = pd.read_csv(time_series_covid19_confirmed_global)
  elif name == 'Death US':
    returned_df = pd.read_csv(time_series_covid19_deaths_US)
  elif name == 'Death Global':
    returned_df = pd.read_csv(time_series_covid19_deaths_global)
  elif name == 'Recovered':
    returned_df = recovered_global = pd.read_csv(time_series_covid19_recovered_global)
  return returned_df



def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
def find_indexes_columns (table_df):
  index_cols = []
  for columns_name in table_df.columns.to_list():
    if not is_date(columns_name):
      index_cols.append(columns_name)
  return index_cols


#confirmed_global_melted = pd.melt(confirmed_global,id_vars=find_indexes_columns(confirmed_global), var_name = "Date", value_name="Confirmed_cases")
#deaths_US_melted = pd.melt(deaths_US,id_vars=find_indexes_columns(deaths_US), var_name="Date", value_name="number_of_deaths")
#deaths_global_melted = pd.melt(deaths_global,id_vars=find_indexes_columns(deaths_global), var_name="Date", value_name="number_of_deaths")
#recovered_global = pd.melt(recovered_global, id_vars=find_indexes_columns(recovered_global), var_name="Date", value_name="number_of_deaths")

# Add a selectbox to the sidebar:
if run:
  scale = st.sidebar.selectbox(
    'Global or US?',
    ('Global', 'US')
  )
  if scale == 'US':
    df_type = st.sidebar.selectbox(
      'Confirmed or Death?',
      ('Confirmed', 'Death')
    )
    if df_type == 'Confirmed':
      load_df('US Confirmed')