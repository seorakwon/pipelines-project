from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd


def GetSoup(url):
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

def Scrape():


    url = 'http://www.planecrashinfo.com/2019/2019.htm'

    soup = GetSoup(url)

    accident_table = soup.find_all('table')[0]

    accidents = []

    for row in accident_table.select('tr')[-1:]:
        cell = row.find_all('td')
        accident = {
            "Date": cell[0].text,
            "Operator": cell[1].text,
        }
        accidents.append(accident)

    accident = pd.DataFrame(accidents)
    accident['Year'] = accident.Date.str[-4:]
    accident['Operator'] = accident.Operator.str[13:-2]
    return accident