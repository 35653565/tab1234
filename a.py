import bs4 as bs
import requests

def get_sp500_weights():

    # get data from website, parse with beautiful soup
    url = 'https://www.slickcharts.com/sp500'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    resp = requests.get(url, headers=headers)
    soup = bs.BeautifulSoup(resp.text, features="lxml")
    print(soup)

    table = soup.find('table', {'<class': 'table table-hover table-borderless table-sm>'})
    print(table)
    sp500_weights = []
    for row in table.findAll('tr')[1:]:
        sp500_weight = row.findAll('td')[3].text
        sp500_weights.append(sp500_weight)
    print(sp500_weights)
    return sp500_weights

get_sp500_weights()




