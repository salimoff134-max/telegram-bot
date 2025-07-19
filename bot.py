import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('7656740556:AAFrO8IFjNXVFhn97SnNR50vR5aaJEy0oVs')


# /site yoki /website komandasi
@bot.message_handler(commands=['site', 'website'])
def open_site(message):
    webbrowser.open('https://konsta.uz/')

# /start, /hello yoki /home komandasi
@bot.message_handler(commands=['start', 'hello', 'home'])

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Motivatsiya kerak emasmi?')
    btn2 = types.KeyboardButton('Rasmni ochirish')
    btn3 = types.KeyboardButton('Rasmni ozgartirish')
    markup.row(btn1)
    markup.row(btn2, btn3)
    with open('./gorkiy.png', 'rb') as file:
       bot.send_photo(message.chat.id,file,reply_markup=markup)
    #bot.send_message(message.chat.id, f'Assalom aleykum, {message.from_user.first_name}',' reply_markup=markup')
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Motivatsiya kerak emasmi?':
        bot.send_message(message.chat.id, 'Marxamat')
    elif message.text == 'Rasmni ochirish':
        bot.send_message(message.chat.id, 'Hop boladi')


# /help komandasi
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Yordam uchun quyidagi raqamga qo‘ng‘iroq qiling: 9921')


def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Motivatsiya kerak emasmi?')
    btn2 = types.KeyboardButton('Rasmni ochirish')
    btn3 = types.KeyboardButton('Rasmni ozgartirish')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Yaxshi', reply_markup=markup)

# Foto yuborilganda
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Motivatsiya kerak emasmi?',
                                      url='https://youtu.be/aitLkJ_VYMw?si=iQEztF9WqgnswikG')
    btn2 = types.InlineKeyboardButton("Rasmni o'chirish", callback_data="delete")
    btn3 = types.InlineKeyboardButton("Rasmni o'zgartirish", callback_data="edit")

    markup.row(btn1)
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Juda ham chiroyli rasm, ammo shug‘ullanmaymizmi :)', reply_markup=markup)


# Callback tugmalarni qayta ishlash
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'delete':
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    elif call.data == 'edit':
        bot.edit_message_text(
            'Bu matn o‘zgartirildi.',
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
    bot.answer_callback_query(call.id)


# Boshqa barcha matnlar
@bot.message_handler()
def echo_message(message):
    if message.text.lower() == 'assalom aleykum':
        bot.send_message(message.chat.id, f'Va aleykum assalom, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


# Ishga tushirish
bot.polling(none_stop=True)
