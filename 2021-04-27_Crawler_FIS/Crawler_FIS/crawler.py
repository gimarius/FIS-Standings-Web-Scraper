from Crawler import RidersFetcher

'''
Author: Marius Gisler
Ziel: Das Ziel des Crawlers besteht darin, die Daten des Gesamtklassements des Ski Gesamtweltcups der Frauen und Männer zu crawlen.
Der Crawler lädt der Namen, die Nationalität und der Rang des Athleten herunter.
Die Resultate werden nach Geschlecht getrennt in zwei CSV-Files gespeichert.
'''


def main(keyword):
    fetcher = RidersFetcher(keyword)
    results = fetcher.fetch()
    df = results.transpose()
    df.columns = ['Name', 'Nation', 'Rank', 'Points']
    transform = lambda x: x + 1
    df.index = df.index.map(transform)

    '''
    Speichern des gecrawlten Website.
    '''

    if keyword == "M":
        df.to_csv("riders_list_men.csv", index=False, header=True)
    else:
        df.to_csv("riders_list_women.csv", index=False, header=True)


'''
Der Nutzer wird hier aufgefordert auszuwählen, ob das Männer oder das Frauenklassement gecrawlt werden sollte.    
'''


if __name__ == "__main__":
    main(str(input("Geben Sie 'M' für Herren und 'L' für Frauen ein: ")))


