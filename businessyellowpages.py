from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
print('DONE - browser setup')

driver.get('https://www.business-yellowpages.com/united-states')
print('DONE - open website')


tag_a_objects = driver.find_elements(By.TAG_NAME, 'a')
urls = [tag_a_object.get_attribute('href') for tag_a_object in tag_a_objects]
company_urls = [url for url in urls if url and 'details' in url]
print('DONE - load URLs')

def printkv(keyElements):
    print()
    print('-'*40)
    print()
    for keyEl in keyElements:
        valEl = driver.find_element(locate_with(By.TAG_NAME, 'td').to_right_of(keyEl))
        print(keyEl.text,valEl.text)

print('NOW SCRAPING')
driver.switch_to.new_window('tab')
for url in company_urls:
    driver.get(url)
    keyElements = driver.find_elements(By.CLASS_NAME, "td-label")
    printkv(keyElements)

driver.quit()
