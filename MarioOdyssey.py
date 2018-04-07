from selenium import webdriver
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_ACCOUNT_AUTH_TOKEN']
my_number = os.environ['MY_PHONE_NUMBER']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

browser = webdriver.Chrome()
browser.get('https://www.amazon.com/dp/B01MY7GHKJ/')

client = Client(account_sid, auth_token)

elem = browser.find_element_by_id('availability')
children = elem.find_elements_by_xpath('.//*')
for child in children:
    if('In Stock' in child.text):
        client.api.account.messages.create(
                to=my_number,
                from_=twilio_number,
                body="Hey, you should check Mario Odyssey")
