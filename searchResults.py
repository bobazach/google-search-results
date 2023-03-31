# Python script to return the number of search results for a keyword on Google
import requests
from bs4 import BeautifulSoup

def pyGoogleSearch(word):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    address = "https://www.google.com/search?q="
    URL = address + word
    result = requests.get(URL, headers=headers)    

    soup = BeautifulSoup(result.content, 'html.parser')

    total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) # Entire line
    results_num = ''.join([num for num in total_results_text if num.isdigit()]) # Number of results
    return results_num