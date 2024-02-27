import pandas as pd

data = pd.read_csv(r"C:\Users\Huawei\masaüstü\answer2\country_vaccination_stats.csv")


country_min_vaccinations = {}

for country in data['country'].unique():
    min_vaccinations = data[data['country'] == country]['daily_vaccinations'].min()
    country_min_vaccinations[country] = min_vaccinations
 
for index, row in data.iterrows():
    country = row['country']
    if pd.isnull(row['daily_vaccinations']):
        if country in country_min_vaccinations:
            data.at[index, 'daily_vaccinations'] = country_min_vaccinations[country]
        else:
            data.at[index, 'daily_vaccinations'] = 0

print(data)