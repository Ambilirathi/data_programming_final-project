import pandas as pd
import plotly.express as px
import streamlit as st
import warnings
import pymysql

import plotly.graph_objects as go
from plotly.subplots import make_subplots
warnings.filterwarnings("ignore")
st. set_page_config(layout="wide")

username='root'
password='root'



conn=pymysql.connect(
    host='localhost',
    user=username,
    password=password
)

# USING PhonepeDB I HAVE CREATED IN DATABASE-INSTANCE OF RDS
mycursor=conn.cursor()
sql='''USE car'''
mycursor.execute(sql)

# RETRIEVING DATA FROM CLOUD DATABASE
query = 'select * from cars'
car_DF = pd.read_sql(query, con = conn)

print(car_DF)


# st.write("### **:PURPLE[CAR BRANDS IN MAX PRICE]**")
# max_prices = car_DF.groupby('Brand')['Price'].max()
#
# Coropleth_Dataset = car_DF.sort_values(by=['Price'])
# fig = px.bar(Coropleth_Dataset, x='Brand', y='Price',title="MAX PRICE OF EACH BRANDS" )
#
# st.plotly_chart(fig, use_container_width=True)