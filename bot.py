#importa os modulos necessarios
import sys, telebot, json
import init, chats, funcoes, deps

#cria o bot
bot = telebot.TeleBot(init.bot_api)

#trigger dos comandos
@bot.message_handler(commands=deps.load)
def send_report(message):
	msg = message.text.replace('/', '')
	for item in deps.load:
		if item == msg:
			bot.reply_to(message, funcoes.report(deps.load[item]))

#loop de updates
bot.polling()