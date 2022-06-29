import os
import telebot
import requests

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
faucet_link = "https://goerlifaucet.com/"


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
    msg = "Okey! Just paste your account address: "
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: {msg}")
    bot.reply_to(message, msg)
    # @bot.message_handler(func=lambda message: True)
    # def get_address(message):
    #     print(f"{message.from_user.username}: {message.text}")
    #     address = message.text
    #     url_faucet = 'https://goerlifaucet.com/'
    #     response_search = requests.get(url_faucet)
    #     print(f"Bot: Successful !" )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"{message.from_user.username}: {message.text}")
    print(f"Bot: Con gà")
    bot.reply_to(message, "Con gà")

bot.infinity_polling()
