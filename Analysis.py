import pandas as pd


df = pd.read_csv("Zomato_Data_Set.csv")


print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)


print("\nFirst 5 rows:\n", df.head())


df = df.dropna()


if 'rate' in df.columns:
    df['rate'] = df['rate'].astype(str).str.replace('/5', '')
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')


if 'rate' in df.columns:
    print("\nAverage Rating:", df['rate'].mean())


if 'rate' in df.columns and 'name' in df.columns:
    top_restaurants = df.sort_values(by='rate', ascending=False).head(10)
    print("\nTop Restaurants:\n", top_restaurants[['name', 'rate']])


if 'location' in df.columns:
    location_analysis = df['location'].value_counts().head(10)
    print("\nTop Locations:\n", location_analysis)


if 'approx_cost(for two people)' in df.columns:
    cost_analysis = df['approx_cost(for two people)'].value_counts().head(10)
    print("\nCost Distribution:\n", cost_analysis)