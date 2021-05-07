import bs4 as bs
import requests

def get_sp500_weights():
    resp = requests.get('https://www.slickcharts.com/sp500')
    soup = bs.BeautifulSoup(resp.text, features="lxml")
    table = soup.find('table', {'class': 'table table-hover table-borderless table-sm'})
    sp500_weights = []
    for row in table.findAll('tr')[1:]:
        sp500_weight = row.findAll('td')[3].text
        sp500_weights.append(sp500_weight)
    print(sp500_weights)
    return sp500_weights

get_sp500_weights()




