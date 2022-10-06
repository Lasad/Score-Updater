import smtplib, ssl
from bs4 import BeautifulSoup
import requests
import time

#input before running code
home_team = 'Man Utd'
away_team = 'Arsenal'
match_id = 74966 #from premier league website
sender_email = "sender@email.com"
password = "password123"
receiver_email = ["receiver@email.com"]


lasad_old = '0-0' #starting score
while(True):
    #scraping the score
    site = "https://www.premierleague.com/match/74966"

    source = requests.get(site).text
    soup = BeautifulSoup(source, 'lxml')

    lasad = soup.find('div',class_="score").text
    t = soup.find('span',class_="js-match-time").text

    if lasad != lasad_old:
        lasad_old = lasad
        #emailing the score
        port = 465
        smtp_server = "smtp.gmail.com"

        message = f"""\n
        Subject: Score update!\n\n

        {home_team} {lasad} {away_team}\n Minutes played: {t}"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            for receiver in receiver_email:
                server.sendmail(sender_email, receiver, message)
        time.sleep(5)