import bs4 as bs
from urllib.request import Request, urlopen

def search_box_builder():
    search_box = 'https://ny.milesplit.com/search?category=athlete&q='
    first_name = input('First Name:')
    last_name = input('Last Name:')
    url = search_box + first_name + '+' + last_name
    return url

def scrape(url):
    source = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(source).read()
    soup = bs.BeautifulSoup(webpage, 'lxml')
    return soup

try:
    result = scrape(search_box_builder()).find('div', class_='no-result').text
    print(result)
    print('Try again!')

    try1 = scrape(search_box_builder())
    result = try1.find('span', class_='footnotelight').text

except AttributeError:
    print('Enter name once more to confirm')
    try1 = scrape(search_box_builder())
    result = try1.find('span', class_='footnotelight').text

print(result)









