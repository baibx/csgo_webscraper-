import bs4 as bs
from urllib.request import Request, urlopen

# filtering by categories
category_search = ["guns", "knives", "agents", "graffiti", "gloves", "music-kits", "collectibles(pins)", "patch",
                   "pass"]

guns = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=tag_weapon_'

knives = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Knife&appid=730'

agents = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=any&category_730_Type%5B0%5D=tag_Type_CustomPlayer&appid=730'

graffiti = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Spray&appid=730'

gloves = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_Type_Hands&appid=730'

music_kits = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_MusicKit&appid=730'

collect = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Collectible&appid=730'

patch = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Tool_Patch&appid=730'

pass1 = 'https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Ticket&appid=730'

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
    return url_builder

for categories in enumerate(category_search):
    print(categories)

choice = float(input("Input the number that corresponds to the category"))

if choice == 0:
    url = urlbuilder(guns)
    print(url)












