import telebot
from telebot import types
from os import remove
from coursesTXT import *
from schoolTXT import *
from url import *
from teachers import *
from os import environ
from dotenv import load_dotenv

load_dotenv()

token = environ['BOT_TOKEN']
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id, startMessage)
  bot.send_message(1124334301, 'Бота просматривает\ntg://user?id=' + str(message.chat.id))

@bot.message_handler(commands=['help'])
def help_message(message):
 bot.send_message(message.chat.id,'''Напиши свой вопрос''')

@bot.message_handler(commands=['activate'])
def activate_message(message):
  bot.send_message(message.chat.id, activateMessage, parse_mode='MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(commands=['aboutus'])
def aboutus_message(message):
  bot.send_message(message.chat.id, aboutusMessage)

@bot.message_handler(commands=['price'])
def price_message(message):
  bot.send_message(message.chat.id, priceMessage)

@bot.message_handler(commands=['gift'])
def gift_message(message):
  bot.send_message(message.chat.id, giftMessage)

@bot.message_handler(commands=['info'])
def info_message(message):
  bot.send_message(message.chat.id, f'{url_inst}\n{url_face}', parse_mode='MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(commands=['courses'])
def courses_message(message):
  bot.send_message(message.chat.id, courseslistMessage, parse_mode='MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(commands=['design'])
def start_message(message):
  bot.send_message(message.chat.id, designTXT)

@bot.message_handler(commands=['coding'])
def coding_message(message):
  bot.send_message(message.chat.id, pythonTXT)

@bot.message_handler(commands=['roblox'])
def roblox_message(message):
  bot.send_message(message.chat.id,robloxTXT)

@bot.message_handler(commands=['interface'])
def interface_message(message):
  bot.send_message(message.chat.id, interfaceTXT)

@bot.message_handler(commands=['teachers'])
def teachers_message(message):
  bot.send_message(message.chat.id, teachersMessage)

@bot.message_handler(commands=['sendapp'])
def sendapp_message(message):
  bot.send_message(message.chat.id, sendappMessage, parse_mode='MarkdownV2', disable_web_page_preview=True)


@bot.message_handler(commands=['roma'])
def roma_message(message):
  photoRoma = open('/root/telebotTeeIT/Photo/Roma.jpg', 'rb')
  bot.send_photo(message.chat.id, photoRoma)
  bot.send_message(message.chat.id, teacherRomaMessage, parse_mode='MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(commands=['dasha'])
def dasha_message(message):
  photoDasha = open('/root/telebotTeeIT/Photo/Dasha.jpg', 'rb')
  bot.send_photo(message.chat.id, photoDasha)
  bot.send_message(message.chat.id,teacherDashaMessage, parse_mode='MarkdownV2', disable_web_page_preview=True)

@bot.message_handler(content_types=['''text'''])
def text_message(message):
  global info
  info = message.text
  markup = types.InlineKeyboardMarkup(row_width=2)
  item1 = types.InlineKeyboardButton("Всё верно, отправить", callback_data='good' )
  item2 = types.InlineKeyboardButton("Изменить", callback_data='bad')
  markup.add(item1, item2)
  bot.send_message(message.chat.id,'Твоё сообщение:\n\n' + message.text + '\n\nВсе верно?', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.data == 'good':
    bot.send_message(1124334301, str(info)+ '\ntg://user?id=' + str(call.message.chat.id))
    bot.send_message(call.message.chat.id, 'Информация отправлена Даше, она свяжется с тобой в ближайшее время')
  elif call.data == 'bad':
    bot.send_message(call.message.chat.id, 'Напиши сообщение заново')


bot.infinity_polling()
