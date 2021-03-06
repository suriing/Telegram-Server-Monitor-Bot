import os
import sys
import time
import random
import datetime
import subprocess
import ConfigParser
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# configparser for token & chat_id
config = ConfigParser.ConfigParser()
config.read(sys.argv[1])
token = config.get('settings','token')
chat_id = config.get('settings','chat_id')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_ids = msg['chat']['id']

    if content_type == 'text':
        command = msg['text'].lower()
        print('Command received: %s' % command)
        if command == 'enable vnc server':
            risp=subprocess.check_output("vncserver", shell=True)
            bot.sendMessage(chat_id, 'Done.')
        elif command == 'disable vnc server':
            subprocess.check_output("vncserver -kill :1", shell=True)
            bot.sendMessage(chat_id, 'Done.')
        elif command == '/start':
            bot.sendMessage(chat_ids, 'This bot responds only to its owner.')
        elif command == 'time':
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif command == 'help':
            bot.sendMessage(chat_id, 'Text me one of the following commands:')
            bot.sendMessage(chat_id, 'time')
            bot.sendMessage(chat_id, 'uptime')
            bot.sendMessage(chat_id, 'free ram')
            bot.sendMessage(chat_id, 'free ram 2')
            bot.sendMessage(chat_id, 'free space')
            bot.sendMessage(chat_id, 'enable/disable VNC server')
            bot.sendMessage(chat_id, 'enable/disable test2 dir')
            bot.sendMessage(chat_id, 'command X (executes X command in linux shell and returns output)')
            bot.sendMessage(chat_id, 'command X && Y && ... (executes independents comands and returns output)')
            bot.sendMessage(chat_id, 'command X & Y & ... (executes dependents comands and returns output)')
            bot.sendMessage(chat_id, 'reboot')
            bot.sendMessage(chat_id, '/c for custom keyboard')
        elif command.find('command') == 0:
            command=command.replace('command ','')
            bot.sendMessage(chat_id, 'Running...')
            risp=subprocess.check_output(command, shell=True)
            bot.sendMessage(chat_id, risp)
        elif command == 'enable test2 dir':
            risp=subprocess.check_output("sudo chmod 777 /var/www/test2", shell=True)
            bot.sendMessage(chat_id, 'Done.')
        elif command == 'disable test2 dir':
            risp=subprocess.check_output("sudo chmod 000 /var/www/test2", shell=True)
            bot.sendMessage(chat_id, 'Done.')
        elif command == 'free ram':
            risp=subprocess.check_output("free -h", shell=True)
            bot.sendMessage(chat_id, risp)
        elif command == 'free ram 2':
            risp=subprocess.check_output("vmstat -s", shell=True)
            bot.sendMessage(chat_id, risp)
        elif command == 'free space':
            risp=subprocess.check_output("df -H", shell=True)
            bot.sendMessage(chat_id, risp)
        elif command == 'uptime':
            risp=subprocess.check_output("uptime", shell=True)
            bot.sendMessage(chat_id, risp)
        elif command == 'reboot':
            bot.sendMessage(chat_id, 'Rebooting...')
            risp=subprocess.check_output("sudo reboot", shell=True)
        elif command == '/c':
            markup = ReplyKeyboardMarkup(keyboard=[
                ['time', 'uptime'],
                [ 'free ram','free space'],
                ['enable vnc server', 'disable vnc server'],
                ])
            bot.sendMessage(chat_id, 'command shorcuts', reply_markup=markup)
        else:
            if chat_ids != chat_id:
                bot.sendMessage(chat_ids, 'Error. Please retry.')

bot = telepot.Bot(token)
bot.message_loop(handle)
print('Listening...')
bot.sendMessage(chat_id,'Server booted, ready to go!')

while 1:
    time.sleep(10)

