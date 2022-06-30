import os
import telebot
import requests
# from send_bnb import send # MẤT TIỀN

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
    msg = "This is the list of commands: \n greet - Say hello to bot \n start - Introduction \n help - How to use this bot \n gettoken - Get some testnet token from Firebird"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    bot.send_message(message.chat.id, "This is the list of commands: \n greet - Say hello to bot \n start - Introduction \n help - How to use this bot \n gettoken - Get some testnet token from Firebird")

@bot.message_handler(commands = ['faucet'])
def faucet(message):
    msg = "Okey! I have your address now ! Please wait while I send you some tokens"
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    
    bot.reply_to(message, msg)

    address = message.text[8:]
    # send_eth(address) # MẤT TIỀN
    bot.send_message(message.chat.id, "Successfully sent some tokens to your address !")
    print(f"Bot: {msg}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: Non")
    bot.reply_to(message, "Non")

bot.infinity_polling()
