import requests
from bs4 import BeautifulSoup

URL="https://www.emag.ro/telefon-mobil-samsung-galaxy-s10e-dual-sim-128gb-6gb-ram-4g-green-sm-g970fzgdrom/pd/DKY7QLBBM/?ref=prod_CMP-59033_5017_wow_deal_widget"
#
headers= {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    price = soup.find(id="priceblock_ourprice")

    # converted_price=float(price[:-5])
    # if converted_price<1.700:
    #     send_mail()

    print(price)

# def send_mail():
check_price()
