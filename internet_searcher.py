from selenium import webdriver
#import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
import time


#Setting up the requirements
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#fpath = Path("chromedriver").absolute()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#chromedriver_autoinstaller.install()
#driver = webdriver.Chrome()

def internet_searcher(name: str) -> list:
    """
    A simple search function to search for contact information on the internet.

    Args:
        name (str): The name of the person to search for.

    Returns:
        list: A list of webpages containing contact information.

    Raises:
        None
        
    Note: IT RETURNS AN EMPTY LIST IF LESS THAN 3 RESULTS ARE FOUND.
    """

    input_name = name
    output_webpages = []


    #Getting Running Instances
    driver.get("https://searx.space/")
    public_instance_list = driver.find_elements(By.XPATH,"/html/body/div[1]/main/div/div/table/tbody/tr")
    length_of_instances = len(public_instance_list)
    instances_running = []
    for i in range(1,length_of_instances):
        instance_xpath = f'/html/body/div[1]/main/div/div/table/tbody/tr[{i}]/td[1]/span/a'
        instance = driver.find_element(By.XPATH,instance_xpath)
        instance_address = instance.text
        instances_running.append(instance_address)
        i+=1


    queries = [f"{input_name} + contact (or) contact information (or) contact me"]
    
    #Running Queries
    for instance in instances_running:
        try:
            driver.get(instance)
            driver.find_element(By.XPATH,'//*[@id="q"]').send_keys(queries[0])
            driver.find_element(By.XPATH,'//*[@id="send_search"]').click()
            time.sleep(2)
            search_outputs = driver.find_elements(By.XPATH,"/html/body/main/div/div[2]/article[contains(@class, 'google')]/a")
            for output in search_outputs:
                if output not in output_webpages:
                    output_webpages.append(output.get_attribute("href"))
                else:
                    pass

            if len(output_webpages) >= 3:
                break
            else:
                continue

        except:
            print("Error in running query on instance: ",instance)

        
    #Printing Output
    try:
        output_webpages = output_webpages[:3]
    except IndexError:
        output_webpages = []


    return output_webpages



if __name__ == "__main__":
    name = input("Enter name: ")
    print(internet_searcher(name))





