import math

from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from pymongo import MongoClient

# replace 'my_user', 'my_password', and 'my_database' with your own values
client = MongoClient('mongodb+srv://rootguvi:rootguvi@cluster0.u37z9wj.mongodb.net/test')

# replace 'my_collection' with the name of your collection
collection = client.my_database.my_collection

results = collection.find()

df = pd.DataFrame(list(results))

app = Flask(__name__)

print(df)
@app.route('/api/chart')
def chart():
    max_prices = df.groupby('Brand')['Price'].max()
    data = [['Brand', 'Max Price']]
    for brand, max_price in max_prices.items():
        data.append([brand, max_price])
    return jsonify(data)

@app.route('/api/data')
def data():
    data = [[ 'Price', 'Year']]

    for price, year in zip( df['Price'], df['Year']):
        if not math.isnan(price):
            data.append([price, year])

    data.pop(0)

    return jsonify(data)

@app.route('/api/economy')
def data_economy():
    # Sort the dataframe by price in descending order
    df_sorted = df.sort_values(by="Mileage", ascending=False)

    # Create a new dataframe with the top 5 models and their prices
    df_top10 = df_sorted.head(20)[["Brand", "Model", "Mileage"]]

    # Print the new dataframe
    print(df_top10)

    data = [[ 'Brand', 'Mileage']]

    for brand, milage in zip( df_top10['Brand'], df_top10['Mileage']):

        data.append([brand, milage])

    return jsonify(data)


@app.route('/api/price')
def chart_year_price():
    # Sort the dataframe by price in descending order
    df_sorted = df.sort_values(by="Mileage", ascending=False)

    # Create a new dataframe with the top 5 models and their prices
    df_top10 = df_sorted.head(20)[["Year", "Price", "Mileage"]]

    # df_top10new = df_top10.sort_values(by='Year', ascending=False)
    # df_top10 = df_top10new.head(20)[["Year", "Price", "Mileage"]]

    # Print the new dataframe
    print(df_top10)

    data = [["Year", "Price" , "Mileage"]]

    for year, price , mileage in zip(df_top10['Year'], df_top10['Price'], df_top10['Mileage']):
        data.append([year, price , mileage])

    return jsonify(data)

@app.route('/api/alldata')
def get_data():
    df.dropna(inplace=True)
    data = [['id','Brand','Price', 'Body', "Mileage",'EngineV','Engine_Type', 'Year' ,'Model' ,'Registration']]
    id=0
    for brand,price, body, mileage,engineV,engine_Type, year ,model ,registration in zip(df['Brand'],df['Price'],df['Body'],df['Mileage'],df['EngineV'],df['Engine_Type'],df['Year'],df['Model'], df['Registration']):
        if not math.isnan(price):
            id=id+1
            data.append([id,brand,price, body, mileage,engineV,engine_Type, year ,model])

    return jsonify(data)


@app.route('/api/searchbyid')
def data_by_id():
    param = request.args.get('param')


    df.dropna(inplace=True)
    data = [['id', 'Brand', 'Price', 'Body', "Mileage", 'EngineV', 'Engine_Type', 'Year', 'Model', 'Registration']]
    newdata = [[ 'Brand', 'Price', 'Body', "Mileage", 'EngineV', 'Engine_Type', 'Year', 'Model', 'Registration']]
    id = 0
    for brand, price, body, mileage, engineV, engine_Type, year, model, registration in zip(df['Brand'], df['Price'],
                                                                                            df['Body'], df['Mileage'],
                                                                                            df['EngineV'],
                                                                                            df['Engine_Type'],
                                                                                            df['Year'], df['Model'],
                                                                                            df['Registration']):
        if not math.isnan(price):
            id = id + 1
            data.append([id, brand, price, body, mileage, engineV, engine_Type, year, model])

    for row in data:
        if row[0] == int(param):
            newdata.append(row)
            return jsonify(newdata)
    return jsonify({'error': 'Data not found'})


@app.route('/api/alldatabyrange')
def get_data_range():
    param = request.args.get('param')
    df.dropna(inplace=True)
    df_top10 = df.head(int(param))
    data = [['id','Brand','Price', 'Body', "Mileage",'EngineV','Engine_Type', 'Year' ,'Model' ,'Registration']]
    id=0
    for brand,price, body, mileage,engineV,engine_Type, year ,model ,registration in zip(df_top10['Brand'],df_top10['Price'],df_top10['Body'],df_top10['Mileage'],df_top10['EngineV'],df_top10['Engine_Type'],df_top10['Year'],df_top10['Model'], df_top10['Registration']):
        if not math.isnan(price):
            id=id+1
            data.append([id,brand,price, body, mileage,engineV,engine_Type, year ,model])

    return jsonify(data)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)