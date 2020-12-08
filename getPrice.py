import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#product-content > div.row > div.price-wrapper.text-right.col-auto > div > span')
    return elems[0].text.strip("From\n")
price = getPrice('https://www.emp.co.uk/p/hells-bells-1980/456131.html')
print('The price is ' + price)
