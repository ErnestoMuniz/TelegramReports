from base import interact
import os

#import needed packages
import telebot, json

#gets bot base data
with open('base/keys.json', 'r') as read_file:
    data = json.load(read_file)
    #creates the bot
    bot = telebot.TeleBot(data['bot_key'])

#command trigger
@bot.message_handler(commands=interact.commands)
def send_report(message):
    msg = message.text.replace('/', '')
    msg = msg.split(' ')
    if msg[0] in interact.commands:
        report(interact.commands[msg[0]], message, msg)

#reply message
def report(arg, message, comm):
    spl = arg.split('/')
    variaveis = json.load(open('modules/{}/variables.json'.format(spl[0]), 'r'))
    with open('modules/{}/variables.json'.format(spl[0]), 'w') as vrbs:
        try:
            variaveis['arg'] = comm[1]
            json.dump(variaveis, vrbs)
        except:
            variaveis['arg'] = ''
            json.dump(variaveis, vrbs)
    os.system('cd modules/{}/ && python3 {}.py'.format(spl[0], spl[1]))
    variaveis = json.load(open('modules/{}/variables.json'.format(spl[0]), 'r'))
    if variaveis['report'] == "":
        pass
    else:
        bot.reply_to(message, variaveis['report'])

#update loop
print('Bot running...')
bot.polling()