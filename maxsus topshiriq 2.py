# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R5i_8Nyr817AZataBVJrZMjCAB_qgcZg
"""

!pip install openpyxl

import pandas as pd


url = "https://raw.githubusercontent.com/Zulayho06/Maxsus-topshiriq/main/WHO%20COVID-19%20cases.csv"
df = pd.read_csv(url)


print("DataFrame Ma'lumotlari:")
df.info()


print("\nUstunlar ro'yxati:")
print(df.columns)


print("\nDataFrame'ning bosh qismini ko'rib chiqish:")
print(df.head())


covid_by_country = df.groupby('Country')['Cumulative_cases'].sum().reset_index()


covid_by_country = covid_by_country.sort_values(by='Cumulative_cases', ascending=False)

print("\nEng yuqori tasdiqlangan holatlar bo'yicha 10 ta davlat:")
print(covid_by_country.head(10))


usa_data = df[df['Country'] == 'USA']


print("\nUSA bo'yicha tasdiqlangan COVID-19 holatlari:")
print(usa_data[['Date_reported', 'Cumulative_cases']].tail())



india_data = df[df['Country'] == 'India']


print("\nIndia bo'yicha tasdiqlangan COVID-19 holatlari:")
print(india_data[['Date_reported', 'Cumulative_cases']].tail())