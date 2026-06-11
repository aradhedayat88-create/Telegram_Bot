import telebot
import base
import convert_currency as cvt
import app_api

bot = telebot.TeleBot(base.TOKEN)

print('bot created')

base_currency = ''
target_currency = ''


@bot.message_handler(commands=['start'])
def say_hello(message):
    # print(message)
    bot.send_message(message.chat.id, 'به بات آموزشی ما خوش آمدید')


@bot.message_handler(commands=['help', 'contact'])
def show_help(message):

    bot.reply_to(message, 'در صورت نیاز به پشتیبانی با شماره 2222 تماس بگیرید')


@bot.message_handler(commands=['news'])
def get_news(message):

    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text='اخبار ورزشی', url ='https://varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text = 'اخبار روز', url = 'https://tabnak.ir')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='یکی از گزینه ها را انتخاب کنید', reply_markup=markup)


@bot.message_handler(commands=['menu'])
def show_menu(message):

    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton(text='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text= 'درباره ما')
    btn3 = telebot.types.KeyboardButton(text= 'عضویت')
    btn4 = telebot.types.KeyboardButton(text= 'بازگشت')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text='یکی از گزینه ها را انتخاب کنید', reply_markup=markup)



# @bot.message_handler(commands=['convert'])
# def exchange_currency(message):
#     msg = bot.send_message(message.chat.id, text='ارز مبدا را وارد کنید')
#     bot.register_next_step_handler(msg, get_base_currency)

# def get_base_currency(message):
    
#     global base_currency
#     base_currency = message.text.upper()

#     msg = bot.send_message(message.chat.id, text='ارز مقصد را وارد کنید')
#     bot.register_next_step_handler(msg, get_target_currency)

# def get_target_currency(message):
#     global target_currency


#     target_currency = message.text.upper()
#     rate = cvt.exchange_rate(base_currency, target_currency)
#     bot.send_message(message.chat.id, f'نرخ تبدیل ارز برابر است با : {rate}')


# @bot.message_handler(func = lambda message:True)
# def show_message(message):

#     if message.text == 'تماس با ما':
#         phone = '09123636451'
#         email  = 'support@gmail.com'
#         info = f'ایمیل:{email} -  شماره تماس:{phone}'
#         bot.send_message(message.chat.id, info)

#     elif message.text == 'درباره ما':
#         bot.reply_to(message,'این پروژه شامل تعداد زیادی بات های کاربردی است')


#     elif message.text == 'عضویت':
#         pass

#     elif  message.text == 'بازگشت':
#         markup = telebot.types.ReplyKeyboardRemove()
#         bot.send_message(message.chat.id,'بازگشت به صفحه چت', reply_markup=markup)


@bot.message_handler(commands=["movie"])
def get_movie_step_one(message):
    msg = bot.send_message(message.chat.id, text="نام فیلم مورد نظر را وارد کنید")
    bot.register_next_step_handler(msg, get_movie_info)

def get_movie_info(message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    title = result[0]
    year = result[1]
    country  = result[2]
    imdb_rate = result[3]
    info = f"title : {title}\n year : {year}\n country : {country}\n imdb rate : {imdb_rate}"
    bot.send_message(message.chat.id, text=info)





@bot.message_handler(func= lambda message: True)
def answer_to_all(message):
    
    if message.text == "تماس با ما":
        phone = '09123636451'
        email  = 'support@gmail.com'
        info = f'ایمیل:{email} -  شماره تماس:{phone}'
        bot.send_message(message.chat.id, info)
    
    elif message.text == "درباره ما":
        bot.reply_to(message,'ما یک گروه آموزشی هستیم')

    
    elif message.text == "بازگشت":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,'بازگشت به صفحه چت', reply_markup=markup)






if __name__ == '__main__':
    bot.infinity_polling()
