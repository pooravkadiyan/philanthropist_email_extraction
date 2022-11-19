from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    
from bs4 import BeautifulSoup
from urllib import request
import time
import csv
import get_text from webpage_to_text
import email_extractor from email_searcher

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

#Getting the name of the donar from the CSV file

with open("input.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    name=row[0]
    print(name)

    query = f"[{name}] + contact (or) contact information (or) contact me"
    driver.get("https://www.google.com/")
    m = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    m.send_keys(query)
    m.submit()
    time.sleep(3)

    results_list = driver.find_elements_by_tag_name('a')
    top_3_results = []

    for i in results_list:
      top_3_results.append(i.get_attribute('href'))
      print(i.get_attribute('href'), '\n')
      if i == 3:
        break
      else:
        continue
      i+=1
    
    for i in top_3_results:
        text = get_text(top_3_results[i])
        emails = email_extractor(text)

        with open('output.csv', 'a') as file:
            writer = csv.writer(file)
            for i in emails:
                writer.writerow([name, i])
                print(i)

    print(name, top_3_results)


