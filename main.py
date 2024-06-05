import smtplib
import datetime as dt
# import random
import requests


email = input("Enter your Email id: ")

print("To generate App password: \n Go to Gmail --> Manage your Google Account --> Open Security --->On 2 Step Verification --> Search App Passwords --> Write App Name --> Click Create👍 ")

password = input("Enter created App password: ")

now = dt.datetime.now()
day = now.weekday()

if day:
  res = requests.get("https://zenquotes.io/api/today") #api endpoint
  # print(res)  #getting 200 means success
  res.raise_for_status()

  data = res.json()
  quote = data[0]['q']
  author = data[0]['a']
  
  # with open("quotes.txt") as file:
  #   all_quotes = file.readlines()
  #   quote = random.choice(all_quotes)
  #   print(quote)

to_email = input("Email Address of Receiver: ")

with smtplib.SMTP("smtp.gmail.com", 587) as con:
  con.starttls()  #use to secure the connection
  con.login(user = email, password = password)
  
  con.sendmail(from_addr = email, to_addrs = {to_email}, msg=f"Subject: Motivational Quotes\n\n{quote} ~ By: {author}")

