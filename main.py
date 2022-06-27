import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['start'])
def greet(message):
    bot.reply_to(message, "Welcome ! This bot helps you to quickly request some testnet token")

@bot.message_handler(commands = ['greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands = ['help'])
def greet(message):
    bot.reply_to(message, "This is the list of commands: \n greet - Say hello to bot \n start - Introduction \n help - How to use this bot \n gettoken - Get some testnet token from Firebird")

@bot.message_handler(commands = ['gettoken'])
def greet(message):
    bot.reply_to(message, "Okey! Just paste your account address: ")

bot.polling()