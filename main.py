
from bs4 import BeautifulSoup
import requests
import time
from discordwebhook import Discord

discord = Discord(url="https://discord.com/api/webhooks/1222898078777086035/pUnL-HRl_JTCbX1Ml0vj4Boff6hXGXn_QU0WrLDunOudKdKXOzA6O_zxlGouKsKYpUfA")

def main():
   print("check webpage")
   html = requests.get("https://www.microcenter.com/product/677543/asus-zenbook-duo-ux8406ma-ps99t-14-laptop-computer---inkwell-gray_Hatchfeed?utm_campaign=Asus&storeID=121")
   soup = BeautifulSoup(html.text,"html.parser")
   result = soup.find("div",{"class":"inventory"}).find("span").text
   print(result)
   return result

def sendNotification():
    discord.post(content="@everyone web page have changed go to link https://www.microcenter.com/product/677543/asus-zenbook-duo-ux8406ma-ps99t-14-laptop-computer---inkwell-gray_Hatchfeed?utm_campaign=Asus&storeID=121")

if __name__ == '__main__':
    sec = 10
    lastResult = "test" 
    while(True):
         time.sleep(sec)
         result = main()
         if(result != lastResult):
               sendNotification()
         lastResult = result