#Importing libraries and dependencies
from selenium import webdriver
import chromedriver_autoinstaller
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException    
import time
import csv

#Importing own created functions for simplification
from webpage_to_text import get_text
from email_searcher import email_extractor
from internet_searcher import internet_searcher

#Setting up the requirements
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

#Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(credentials)

#Google Sheet Variable 
i=85

#Getting the name of the donar from the CSV file
with open("input.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    name=row[0]
    print(name)
    
     
    try:
      #Finding the potential lookup pages
      lookup_pages = internet_searcher(name)

      #Finding the emails from the lookup pages
      for page in lookup_pages:
        try:
          text = get_text(page)
          emails = email_extractor(text)
          if emails != []:
            for email in emails:
              #Opening the spreadsheet
              sheet = client.open("utdonars")
              sheet_1= sheet.sheet1

              #Writing to the spreadsheet
              cellname = 'A'+str(i)
              sheet_1.update(cellname, email)
              i+=1
          else:
            pass
        except:
          print("Error in getting text from the page")
          pass
        
    except:
      pass



