import pandas as pd
from selenium import webdriver

df = pd.read_csv('upwork_oxford.csv')

for index, row in df.iterrows():
    driver = webdriver.Chrome()
    driver.get(row[3])
    var = driver.execute_script('return dataLayer;')
    print(row[3],':')
    print(var)
    print('-'*30)
    driver.quit()
