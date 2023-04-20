from pymongo import MongoClient

# replace 'my_user', 'my_password', and 'my_database' with your own values
client = MongoClient('mongodb+srv://rootguvi:rootguvi@cluster0.u37z9wj.mongodb.net/test')

# replace 'my_collection' with the name of your collection
collection = client.my_database.my_collection

results = collection.find()

import pandas as pd
import pandas as pd
import plotly.express as px
import streamlit as st
import warnings
import pymysql

import plotly.graph_objects as go
from plotly.subplots import make_subplots
warnings.filterwarnings("ignore")
st. set_page_config(layout="wide")
df = pd.DataFrame(list(results))

print(df)


st.write("### **:PURPLE[CAR BRANDS IN MAX PRICE]**")
max_prices = df.groupby('Brand')['Price'].max()

max_prices_df = pd.DataFrame({'Brand': max_prices.index, 'Max Price': max_prices.values})

print(max_prices_df)

# Coropleth_Dataset = max_prices_df.sort_values(by=['Price'])
fig = px.bar(max_prices_df, x='Brand', y='Max Price',title="MAX PRICE OF EACH BRANDS" )

st.plotly_chart(fig, use_container_width=True)

plot = px.scatter(df, x="Year", y="Price", color="Brand" ,hover_data=['Model'] ,title="Most Priced Models and Year Wise")

st.plotly_chart(plot, use_container_width=True)


# Sort the dataframe by price in descending order
df_sorted = df.sort_values(by="Price", ascending=False)

# Create a new dataframe with the top 5 models and their prices
df_top10 = df_sorted.head(20)[["Brand", "Model", "Price" , "Year"]]

# Print the new dataframe
print(df_top10)


fig = px.bar(df_top10, x='Year', y='Price', color="Model", hover_data=['Brand'],title="TOP 10 Car Models By Year Wise" )

st.plotly_chart(fig, use_container_width=True)


# Define the x-axis as mileage, y-axis as price, and color as registration status
fig = px.scatter(df, x="Mileage", y="Price", color="Registration",
                 hover_data=["Brand", "Model"],title="Registered and Not Registered Models")

# Show the plot
st.plotly_chart(fig, use_container_width=True)