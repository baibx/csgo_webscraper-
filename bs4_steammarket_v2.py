import bs4 as bs
from urllib.request import Request, urlopen

# filtering by categories
category_search = ["guns", "knives", "agents", "graffiti", "gloves", "music-kits", "collectibles(pins)", "patch",
                   "pass", "sticker"]

guns = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=any&category_730_Exterior%5B0%5D=tag_WearCategory2&category_730_Exterior%5B1%5D=tag_WearCategory1&category_730_Exterior%5B2%5D=tag_WearCategory4&category_730_Exterior%5B3%5D=tag_WearCategory3&category_730_Exterior%5B4%5D=tag_WearCategory0&category_730_Exterior%5B5%5D=tag_WearCategoryNA&appid=730'

knives = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Knife&appid=730'

agents = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=any&category_730_Type%5B0%5D=tag_Type_CustomPlayer&appid=730'

graffiti = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Spray&appid=730'

gloves = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_Type_Hands&appid=730'

music_kits = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_MusicKit&appid=730'

collect = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Collectible&appid=730'

patch = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Tool_Patch&appid=730'

pass1 = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Ticket&appid=730'

sticker = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Tool_Sticker&appid=730'

def urlbuilder(url):
    amount_of_keywords = float(input("How many keywords? Please input as a number and not a word. Ex. 1 instead of one"))

    keyword = input("Keyword search: ")
    split = keyword.split(" ")

    if amount_of_keywords == 1:
        keyword_search = keyword
        url_builder = url + "&q=" + keyword_search
    elif amount_of_keywords == 2:
        keyword_search = split[0] + "+" + split[1]
        url_builder = url + "&q=" + keyword_search
    elif amount_of_keywords == 3:
        keyword_search = split[0] + "+" + split[1] + "+" + split[2]
        url_builder = url + "&q=" + keyword_search
    elif amount_of_keywords == 4:
        keyword_search = split[0] + "+" + split[1] + "+" + split[2] + "+" + split[3]
        url_builder = url + "&q=" + keyword_search
    else:
        keyword_search = split[0] + "+" + split[1] + "+" + split[2] + "+" + split[3] + "+" + split[4] + "+" + split[5]
        url_builder = url + "&q=" + keyword_search
    return url_builder

for categories in enumerate(category_search):
    print(categories)

choice = float(input("Input the number that corresponds to the category"))

if choice == 0:
    url = urlbuilder(guns)
elif choice == 1:
    url = urlbuilder(knives)
elif choice == 2:
    url = urlbuilder(agents)
elif choice == 3:
    url = urlbuilder(graffiti)
elif choice == 4:
    url = urlbuilder(gloves)
elif choice == 5:
    url = urlbuilder(music_kits)
elif choice == 6:
    url = urlbuilder(collect)
elif choice == 7:
    url = urlbuilder(patch)
elif choice == 8:
    url = urlbuilder(pass1)
elif choice == 9:
    url = urlbuilder(sticker)

#finally have the url, now can scrape using beautifulsoup

source = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(source).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

#have all the source from the website saved as a "soup"

#here im making the file which we will be saving all of our information on
import csv
with open('steamscrape.csv', "w", encoding="utf-8") as csv_file:   #using with open instead of just open lets you process the weird symbols better from the html
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name of item', 'Sale Price'])  #making the first two columns of the spreedsheet

    for name in soup.find_all('span', class_='market_listing_item_name'):
        csv_writer.writerow([name.text])
        # searching the html of the site and writing it to the csv file
    for price in soup.find_all('span', class_='sale_price'):
        csv_writer.writerow([price.text])

 #this is however formatted all into one row
csv_file.close()

#making a list to store our values in to access later
prices1 = []

#going to get the values from the csv file to reformat
reader = open('steamscrape.csv', 'r+')
csv_reader = csv.reader(reader)

for row1 in csv_reader:
    prices1.append(row1) #adding all of the first row from the csv file to this list

#searching for the amount of results on the page
results = soup.find('div', class_='market_paging_summary ellipsis')

isolate_results = results.text.split('-')

#isolated_variable now contains the amount of results shown on the page
isolate_results1 = isolate_results[1].split(' of')
isolated_variable = int(isolate_results1[0])

def pricing(x):
    first_price = (x * 2) + 2
    return first_price

#making a new file to store the results
csv_file = open('steamscrape_formatted.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name of Item', 'Sale Price'])

#prices1 here is the list that we have built above
for prices in range(0, isolated_variable):
    csv_writer.writerow([prices1[2 + (2 * prices)], prices1[pricing(isolated_variable) + (2 * prices)]])













