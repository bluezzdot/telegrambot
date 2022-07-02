import os
import telebot
import requests
from send_bnb_testnet import send # TESTNET
# from send_bnb import send # MAINNET. MẤT TIỀN

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['start'])
def start(message):
    msg = "Welcome ! This bot helps you to quickly request some testnet token"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    bot.send_message(message.chat.id, "Welcome ! This bot helps you to quickly request some testnet token")

@bot.message_handler(commands = ['greet'])
def greet(message):
    msg = "Hey! Hows it going?"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    bot.send_message(message.chat.id, "Hey! Hows it going?")

@bot.message_handler(commands = ['help'])
def help(message):
    msg = "This is the list of commands: \n /greet - Say hello to bot \n /start - Introduction \n /help - How to use this bot \n /faucet YOUR_ADDRESS - Get some testnet token from Firebird"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['faucet'])
def faucet(message):
    msg = "Okey! Please wait while I send you some tokens"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    
    bot.reply_to(message, msg)

    address = message.text[8:]
    if address[:2] != "0x" or len(address) != 42:
        msg = "Invalid address! Please try again"
        print(f"Bot: {msg}")
        bot.send_message(message.chat.id, msg)
        
    else:
        msg = "I have your address now ! Please wait while I send you some tokens"
        print(f"Bot: {msg}")
        bot.send_message(message.chat.id, msg)
        send(address)
        msg2 = "Successfully sent some tokens to your address !"
        bot.send_message(message.chat.id, msg2)
        print(f"Bot: {msg2}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: I don't understand you. You can type /help to see the list of commands")
    bot.reply_to(message, "I don't understand you. You can type /help to see the list of commands")

bot.infinity_polling()
