from selenium import webdriver
from twilio.rest import Client
import os, sys

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_ACCOUNT_AUTH_TOKEN']
my_number = os.environ['MY_PHONE_NUMBER']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

try:
  browser = webdriver.Chrome()
except ConnectionResetError:
  sys.exit(0)

browser.get('https://www.amazon.com/dp/B01MS6MO77/')

client = Client(account_sid, auth_token)

try:
    elem = browser.find_element_by_id('availability')
except:
    sys.exit(0)
children = elem.find_elements_by_xpath('.//*')
for child in children:
    if('In Stock' in child.text):
        client.api.account.messages.create(
                to=my_number,
                from_=twilio_number,
                body="Hey, you should check Breath of the Wild")
