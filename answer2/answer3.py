import pandas as pd

data = pd.read_csv(r"C:\Users\Huawei\masaüstü\answer2\country_vaccination_stats.csv")


mean_vaccinations = data.groupby('country')['daily_vaccinations'].mean().sort_values(ascending=False)


top_3_countries = mean_vaccinations.head(3)

print(top_3_countries)