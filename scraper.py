import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.emag.ro/telefon-mobil-samsung-galaxy-s22-ultra-dual-sim-256gb-12gb-ram-5g-phantom-black-sm-s908bzkgeue/pd/DQZ01FMBM/?X-Search-Id=66d0d07cba819e12ed11&X-Product-Id=9265669&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}




def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "page-title"}).get_text()
    print(title.strip())

    full_price = soup.find("p", {"class": "product-new-price"}).get_text()
    converted_price = str(full_price[:5])
    price = converted_price.replace('.','')
    print(price)

    if int(price) < 5000:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('alex.karatistul@gmail.com', 'metkzjamfinwzxan')

    subject = "Price fell down!"
    body = 'Check the Emag link https://www.emag.ro/telefon-mobil-samsung-galaxy-s22-ultra-dual-sim-256gb-12gb-ram-5g-phantom-black-sm-s908bzkgeue/pd/DQZ01FMBM/?X-Search-Id=66d0d07cba819e12ed11&X-Product-Id=9265669&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'alex.karatistul@gmail.com',
        'kohan.alex26@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
