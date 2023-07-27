import pandas as pd

food_df = pd.read_csv('data/food_ordering.csv', delimiter="|")

print(food_df.head())
