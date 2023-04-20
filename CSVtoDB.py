import pandas as pd

df = pd.read_csv("cars.csv")


from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root@localhost/car")
df.to_sql(name="cars", con=engine, if_exists="append", index=False)
engine.dispose()
