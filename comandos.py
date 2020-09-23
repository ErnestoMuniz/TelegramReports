#adicione os comandos nesta lista com o mesmo nome dos departamentos
@bot.message_handler(commands=init.deps)
def send_report(message):
	for id in chats.ids:
		if message.chat.id == chats.ids[id]:
			dep = message.text.replace('/', '')
			print(comamands)
			bot.reply_to(message, report(comandos[commands]))
		else:
			pass