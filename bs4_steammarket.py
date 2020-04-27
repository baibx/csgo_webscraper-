import bs4 as bs
from urllib.request import Request, urlopen

search = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=tag_weapon_'
guns = ["awp", "ak47", "aug", "CZ", "deagle", "dualies", "famas", "five-seven", "G3SG1", "galil", "glock", "M249", "m4a1-s", "m4", "mac10", "mag7", "mp5", "mp7", "mp9", "negev", "nova", "p2k", "p250", "p90", "ppbizon", "revolver", "sawed-off", "scar", "sg553", "scout", "tec9", "ump", "usp", "xm"]

for weapons in enumerate(guns):
    print(weapons)

def filtering():

    weapon = float(input("Input the number that corresponds to the weapon"))
    if (weapon == 0):
        awp = search + 'awp&appid=730'
        return awp
    elif (weapon == 1):
        ak47 = search + "ak47&appid=730"
        return ak47
    elif (weapon == 2):
        aug = search + "aug&appid=730"
        return aug
    elif (weapon == 3):
        cz = search + "cz75a&appid=730"
        return cz
    elif (weapon == 4):
        deagle = search + "deagle&appid=730"
        return deagle
    elif (weapon == 5):
        dual = search + "elite&appid=730"
        return dual
    elif (weapon == 6):
        famas = search + "famas&appid=730"
        return famas
    elif (weapon == 7):
        fiveseven = search + "fiveseven&appid=730"
        return fiveseven
    elif (weapon == 8):
        t_auto = search + "g3sg1&appid=730"
        return t_auto
    elif (weapon == 9):
        galil = search + "galilar&appid=730"
        return galil
    elif (weapon == 10):
        glock = search + "glock&appid=730"
        return glock
    elif (weapon == 11):
        m249 = search + "m249&appid=730"
        return m249
    elif (weapon == 12):
        m4a1_s = search + "m4a1_silencer&appid=730"
        return m4a1_s
    elif (weapon == 13):
        m4 = search + "m4a1&appid=730"
        return m4
    elif (weapon == 14):
        mac10 = search + "mac10&appid=730"
        return mac10
    elif (weapon == 15):
        mag7 = search + "mag7&appid=730"
        return mag7
    elif (weapon == 16):
        mp5 = search + "mp5sd&appid=730"
        return mp5
    elif (weapon == 17):
        mp7 = search + "mp7&appid=730"
        return mp7
    elif (weapon == 18):
        mp9 = search + "mp9&appid=730"
        return mp9
    elif (weapon == 19):
        negev = search + "negev&appid=730"
        return negev
    elif (weapon == 20):
        nova = search + "nova&appid=730"
        return nova
    elif (weapon == 21):
        p2k = search + "hkp2000&appid=730"
        return p2k
    elif (weapon == 22):
        p250 = search + "p250&appid=730"
        return p250
    elif (weapon == 23):
        p90 = search + "p90&appid=730"
        return p90
    elif (weapon == 24):
        bizon = search + "bizon&appid=730"
        return bizon
    elif (weapon == 25):
        r8 = search + "revolver&appid=730"
        return r8
    elif (weapon == 26):
        sawed = search + "sawedoff&appid=730"
        return sawed
    elif (weapon == 27):
        scar = search + "scar20&appid=730"
        return scar
    elif (weapon == 28):
        sg = search + "sg556&appid=730"
        return sg
    elif (weapon == 29):
        scout = search + "ssg08&appid=730"
        return scout
    elif (weapon == 30):
        tec = search + "tec9&appid=730"
        return tec
    elif (weapon == 31):
        ump = search + "ump45&appid=730"
        return ump
    elif (weapon == 32):
        usp = search + "usp_silencer&appid=730"
        return usp
    elif (weapon == 33):
        xm = search + "xm1014&appid=730"
        return xm
url = filtering()

amount_of_keywords = float(input("How many keywords? Please input as a number and not a word. Ex. 1 instead of one"))
keyword = input("Keyword search: ")
split = keyword.split(" ")

if (amount_of_keywords == 1):
    keyword_search = keyword
elif (amount_of_keywords == 2):
    keyword_search = split[0] + "+" + split[1]
elif (amount_of_keywords == 3):
    keyword_search = split[0] + "+" + split[1] + "+" + split[2]
elif (amount_of_keywords == 4):
    keyword_search = split[0] + "+" + split[1] + "+" + split[2] + "+" + split[3]

url_builder = url + "&q=" + keyword_search
print(url_builder)

sauce = Request(url_builder, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

import csv
csv_file = open('steamscrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name of Item', 'Sale Price'])

for name in soup.find_all('span', class_='market_listing_item_name'):
    csv_writer.writerow([name.text])

for price in soup.find_all('span', class_='sale_price'):
    csv_writer.writerow([price.text])

csv_file.close()

f = open('steamscrape.csv', 'r+')
csv_f = csv.reader(f)

prices1 = []

for prices in csv_f:
    prices1.append(prices)

#returns a list of lists need to access this
print(prices1)

results = soup.find('div', class_='market_paging_summary ellipsis')

# can't split NoneTypes but can split .text
isolate_results = results.text.split('-')

#isolated_variable now contains the amount of results shown on the page
isolate_results1 = isolate_results[1].split(' of')
isolated_variable = int(isolate_results1[0])

def pricing(x):
    first_price = (x * 2) + 2
    return first_price

csv_file = open('steamscrape_formatted.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name of Item', 'Sale Price'])

#prices1 here is the list that we have built above
for prices in range(0, isolated_variable):
    csv_writer.writerow([prices1[2 + (2 * prices)], prices1[pricing(isolated_variable) + (2 * prices)]])

















