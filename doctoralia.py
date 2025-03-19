from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://www.doctoralia.com.br/pesquisa?q=Cardiologista&loc=S%C3%A3o%20Paulo&filters%5Bspecializations%5D%5B%5D=8"

driver = webdriver.Chrome()

def scrape(url):
    driver.get(url)
    result_items_details = driver.find_elements(By.XPATH, "//div[@data-test-id='result-items-details']")
    for item in result_items_details:
        print('-'*30, '\n', item.text)
    print('-'*30)

for i in range(1,101):
    page_url = base_url + '&page=' + str(i)
    print('\n','SCRAPING PAGE -',i,'\n')
    scrape(page_url)
