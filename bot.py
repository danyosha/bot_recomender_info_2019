import telebot, json
import random
import sched
import time
token ='650690422:AAEsDalv8DDRAqZYW-bz_3LhcCrc9NqYujI'
bot = telebot.TeleBot(token)
Counter = {}
s = sched.scheduler(time.time, time.sleep)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
   bot.send_message(message.chat.id, '''Hello, I am vandal_bot!
If you want to stop working with me send "stop"''')
   #s.enter(0, 1, sendphoto,argument = (message.chat.id))
   bot.send_photo(message.chat.id, open('Vasnetsov/{}.jpg'.format(2), 'rb'))
   bot.send_message(message.chat.id,'Answer to me, do you like this picture. Answer only "/yes" or "/no"')
   
def send_photo(message):
   print(1)
   bot.send_photo(message.chat.id, open('Vasnetsov/{}.jpg'.format(2), 'rb'))
   bot.send_message(message.chat.id,'Answer to me, do you like this picture. Answer only "/yes" or "/no"')

@bot.message_handler(commands=['yes'])
def answer_function_good(message):
   if (message.chat.id in Counter.keys()):
      Counter[message.chat.id] = Counter[message.chat.id] + 1
   else:
      Counter[message.chat.id] = 1
   if Counter[message.chat.id] == 1:
      bot.send_message(message.chat.id, 'If you want to see the pictures of great artistse in any time send me "/anytime"')
   elif (Counter[message.chat.id] > 1):
      s.run()
   else:
      send_photo(message)

@bot.message_handler(commands=['no'])
def answer_function_bad(message):
   pass

@bot.message_handler(commands=['anytime'])
def aytime(message):
   bot.send_message(message.chat.id,'''If you want to see pictures every hour send me "/hour",
If you want to see pictures every half of day send me "/half_day"
If you want to see pictures every day send me "/day"''')
   
@bot.message_handler(commands=['stop'])
def stop (message):
   bot.send_message(message.chat.id, 'You are the worsest human, that I know! Goodbye!')
   del Counter[message.chat.id]

@bot.message_handler(commands=['hour'])
def every_hour_interval(message):
   s.enter(15, 1, send_photo,argument = (message,))
   s.run()
@bot.message_handler(commands=['half_day'])
def every_half_of_day_interval(message):
   s.enter(43200, 1, send_photo,argument = (message,))
   s.run()
@bot.message_handler(commands=['day'])
def every_day_interval(message):
   s.enter(86400, 1, sendp_hoto,argument = (message,))
   s.run()  
bot.polling(none_stop = True)
