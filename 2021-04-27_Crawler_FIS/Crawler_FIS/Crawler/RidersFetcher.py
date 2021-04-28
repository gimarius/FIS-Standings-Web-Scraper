import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


class RidersFetcher():
    def __init__(self, keyword):
        self.keyword = keyword

        '''
        Initialisierung des Crawlers. Nimmt Keyword als Input für die URL.        
        '''

    def fetch(self):

        '''
        Hier wird die URL eingelesen und mit dem keyword "L" für Frauen oder "M" für Männer ergänzt.
        '''

        url = "https://www.fis-ski.com/DB/alpine-skiing/cup-standings.html?sectorcode=AL&seasoncode=2020&cupcode=WC&disciplinecode=ALL&gendercode={0}&nationcode=".format(
            self.keyword)
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")
        time.sleep(1)

        '''
        Verschiedene Loops suchen mit CSS-Selektoren die Daten und speichern sie in Listen ab.
        '''
        name_list = []
        for item in doc.select(".container")[4:]:
            name = item.select_one(".container .g-xs-10").text
            name = name.strip()
            name_list.append(name)
        nation_list = []
        for item in doc.select(".country"):
            nation = item.select_one(".container .country__name-short").text
            nation = nation.strip()
            nation_list.append(nation)
        rank_list = []
        for item in doc.select(".g-xs-24")[3::7]:
            rank = item.select_one(".container .g-xs-5").text
            rank = rank.strip()
            rank_list.append(rank)
        point_list = []
        for item in doc.select(".g-xs-24")[3::7]:
            point = item.select_one(".container .pl-xs-1").text
            point = point.strip()
            point_list.append(point)

        df = pd.DataFrame([name_list, nation_list, rank_list, point_list])

        return df