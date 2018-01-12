Simple python telegram bot based on Telepot library to monitor server status via app. 
No need to set port-forwardings, no custom signed certificates, no webhooks, no bullshit.

# You'll need to run bot.py:

- Python interpreter, on debian: "sudo apt-get python".
- Telepot library, on debian with python installed: "sudo pip install telepot".
- Telegram bot token, obtainable via @BotFather chat, write it at the 'settings.txt'.
- Personal chatid, write it at the 'settings.txt'.

To enable bot to comunicate with you ( due to telegram security policy, anti-spam etc...), 
you need to chat first by opening bot chat and sending "/start", enough to unlock bot direct messaging without human interaction.

# To run bot

- **$ python bot.py settings.txt**
- (to give bot root access) **$ sudo python bot.py settings.txt**

The bot is configured to reply only to your chatid (in yor chat) for security reasons, 
ever use spaces to indentate or you'll get execution errors, use tabs instead.

To add more defined commands simply aggregate to "def handle(msg)" function more elif cases. Have fun.

You can autostart the bot following this toutorial:
http://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/

Additionally, if you're interested in SBC (single board computers) monitoring, you can add 
gpio functions directly in python to control leds, fans, sensors and much other.
I've configured a bot to start a fan in case of CPU overheating in my Orange Pi One sbc.
