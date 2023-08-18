import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver

# Initialize Chrome webdrivers
page_main = webdriver.Chrome()
page_detail = webdriver.Chrome()

# Navigate to the main URL
urls = 'https://sansad.in/ls/members'
page_main.get(urls)

# Lists to store data
name_1 = []
url_1 = []
party_1 = []
constituency_1 = []
state_1 = []
LokSabhaTerms_1 = []
name2=[]
image_1= []


while True:
    rows = page_main.find_elements(By.XPATH, '//*[@id="mainContent"]/div/div/main/div/div[4]/div/div[1]/table/tbody/tr')
    
    for tender_html_element in rows:
        name = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > span a').text
        name_1.append(name)

        image_element = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > span > img')
        image_link = image_element.get_attribute("src")
        image_1.append(image_link)


        url = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > span a').get_attribute("href")
        url_1.append(url)       
        
        party = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        party_1.append(party)

        constituency = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
        constituency_1.append(constituency)

        state = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
        state_1.append(state)

        LokSabhaTerms = tender_html_element.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
        LokSabhaTerms_1.append(LokSabhaTerms)
              
    try:
        next_page = WebDriverWait(page_main, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(4) > nav > ul > li:nth-child(10) > button")))
        next_page.click()
    except:
        break


# Close the webdrivers
page_main.quit()
page_detail.quit()

# Create a DataFrame
data = {
    'Name': name_1,
    'URL': url_1,
    'Party': party_1,
    'Constituency': constituency_1,
    'State': state_1,
    'LokSabhaTerms': LokSabhaTerms_1,
    'Image_url':image_1
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_filename = 'members_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data saved to {excel_filename}")



