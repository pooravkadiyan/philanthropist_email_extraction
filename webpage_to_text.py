import requests
from bs4 import BeautifulSoup
  

def get_text(url):   
    """This function will take a url and return the text from the webpage.
    
    Args:
      url: The url of the webpage.

    Returns:
      text : A string of text from the webpage.
      
    Raises:
        None
    """
    url='https://ankurwarikoo.com/contact/'
    resp=requests.get(url)  
    soup=BeautifulSoup(resp.text,'html.parser')    
    text = soup.get_text()

    return text


