import requests
from bs4 import BeautifulSoup
  

def get_text(url: str) -> str:
    """This function will take a url and return the text from the webpage.
    
    Args:
      url: The url of the webpage.

    Returns:
      text : A string of text from the webpage.
      
    Raises:
        None
    """
    resp=requests.get(url)  
    soup=BeautifulSoup(resp.text,'html.parser')    
    text = soup.get_text()

    return text

if __name__ == "__main__":
    url = input("Enter the url of the webpage: ")
    print(get_text(url))


