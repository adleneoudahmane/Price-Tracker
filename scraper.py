#with this we access a URL like best buy and pull out the data from the website
import requests

#helps us parse and pull individual items from the whole data we get from page
from bs4 import BeautifulSoup

import smtplib

URL = 'https://www.ebay.ca/itm/276062424870?chn=ps&mkevt=1&mkcid=28&srsltid=AfmBOoralzTqhfYgzxt3Zf_MAhoJcaMsQz3oNI0vTi1GSisQQNcJcSDgm3k'

#gives us info about our browser
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}


def check_price():

    #now we can make a call
    #returns all the data from the website
    page = requests.get(URL, headers=headers)

    #makes the raw html data in a structured way
    soup = BeautifulSoup(page.content, "html.parser")

    #pull the title of the product using id
    #get_text() to only get the text part
    title = soup.find(class_="x-item-title__mainTitle").get_text()
    price = soup.find(class_="x-price-primary").get_text()

    converted_price = float(price[3:6])

    if(converted_price < 210):
        send_email()

    #strip() to get rid of the empty spaces
    print("Product:\t" + title.strip())
    print(converted_price)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('xxxx@gmail.com', 'password generated by google')

    subject = "price fell down!"
    body = "check the eBay link https://www.ebay.ca/itm/276062424870?chn=ps&mkevt=1&mkcid=28&srsltid=AfmBOoralzTqhfYgzxt3Zf_MAhoJcaMsQz3oNI0vTi1GSisQQNcJcSDgm3k"

    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        "xxx@gmail.com",
        "xxxx@gmail.com",
        msg
    )

    print("email has been sent")

    server.quit()


check_price()