import requests
from bs4 import BeautifulSoup
from const import SINOPTIK_URL

# def get_today_data():
#     page = requests.get(SINOPTIK_URL)
#     soup = BeautifulSoup(page.content,'html.parser')
#     day_1 = soup.find('div', attrs= {'id':'bd1'})
#     description_1 = str(day_1)[(str(day_1).rfind('title="')+7):str(day_1).find('"><img')]
#     day_2 = soup.find('div', attrs= {'id':'bd2'})
#     description_2 = str(day_2)[(str(day_2).rfind('title="')+7):str(day_2).find('"><img')]
#     day_3 = soup.find('div', attrs= {'id':'bd3'})
#     description_3 = str(day_3)[(str(day_3).rfind('title="')+7):str(day_3).find('"><img')]
#     day_4 = soup.find('div', attrs= {'id':'bd4'})
#     description_4 = str(day_4)[(str(day_4).rfind('title="')+7):str(day_4).find('"><img')]
#     day_5 = soup.find('div', attrs= {'id':'bd5'})
#     description_5 = str(day_5)[(str(day_5).rfind('title="')+7):str(day_5).find('"><img')]
#     day_6 = soup.find('div', attrs= {'id':'bd6'})
#     description_6 = str(day_6)[(str(day_6).rfind('title="')+7):str(day_6).find('"><img')]
#     day_7 = soup.find('div', attrs= {'id':'bd7'})
#     description_7 = str(day_7)[(str(day_7).rfind('title="')+7):str(day_7).find('"><img')]
    
#     # if today_temp is not None and description is not None:
#     #     return {
#     #         today_temp.get_text(),
#     #         description.get_text()
#     #     }
#     # return (None,None)

# get_today_data()

def get_week_data():
    page = requests.get(SINOPTIK_URL)
    soup = BeautifulSoup(page.content,'html.parser')
    day_1 = soup.find('div', attrs= {'id':'bd1'})
    description_1 = str(day_1)[(str(day_1).rfind('title="')+7):str(day_1).find('"><img')]
    day_2 = soup.find('div', attrs= {'id':'bd2'})
    description_2 = str(day_2)[(str(day_2).rfind('title="')+7):str(day_2).find('"><img')]
    day_3 = soup.find('div', attrs= {'id':'bd3'})
    description_3 = str(day_3)[(str(day_3).rfind('title="')+7):str(day_3).find('"><img')]
    day_4 = soup.find('div', attrs= {'id':'bd4'})
    description_4 = str(day_4)[(str(day_4).rfind('title="')+7):str(day_4).find('"><img')]
    day_5 = soup.find('div', attrs= {'id':'bd5'})
    description_5 = str(day_5)[(str(day_5).rfind('title="')+7):str(day_5).find('"><img')]
    day_6 = soup.find('div', attrs= {'id':'bd6'})
    description_6 = str(day_6)[(str(day_6).rfind('title="')+7):str(day_6).find('"><img')]
    day_7 = soup.find('div', attrs= {'id':'bd7'})
    description_7 = str(day_7)[(str(day_7).rfind('title="')+7):str(day_7).find('"><img')]
    data = True
    for i in [day_1,day_2,day_3,day_4,day_5,day_6,day_7,description_1,description_2,description_3,description_4,description_5,description_6,description_7]:
        if i is None :
            data = False
            break
    if data :
        for i in [day_1.get_text(),description_1,day_2.get_text(),description_2,day_3.get_text(), description_3,day_4.get_text(),description_4,day_5.get_text(),description_5,            day_6.get_text(),description_6,day_7.get_text(),description_7 ]:
            print (i)
    else:
        return {None,None,None,None,None,None,None,None,None,None,None,None,None,None}


get_week_data()