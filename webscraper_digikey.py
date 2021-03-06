from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.digikey.com/en/products/detail/apem-inc/MJTP1230/1798037'

# opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
page_soup.body.span
containers = page_soup.findAll("div", {"class":"MuiGrid-root MuiGrid-item MuiGrid-grid-xs-true"})
prod_attr = containers[0]