import requests
from bs4 import BeautifulSoup
from const import SINOPTIK_URL

def get_parsed_data():
    page = requests.get(SINOPTIK_URL)
    soup = BeautifulSoup(page.content,'html.parser')
    today_temp = soup.find('p', attrs= {'class':'today-temp'})
    description = soup.find('div', attrs= {"class":"description"})
    if today_temp is not None and description is not None:
        return {
            today_temp.get_text(),
            description.get_text()
        }
    return (None,None)
