import os
import telebot
from telebot.types import InlineKeyboardButton
from lib import wallpaper as WP
from lib import image
import time

os.system('cls' if os.name=='nt' else 'clear')


API_KEY = os.getenv("API_KEY") if os.getenv("API_KEY")!=None else "2068683845:AAFsB-599frUUaUj6W_aTenovaBbV-xSNX4"
bot = telebot.TeleBot(API_KEY)    
 
wallpaper = telebot.types.InlineKeyboardMarkup()
wallpaper2 = telebot.types.InlineKeyboardMarkup()
contact = telebot.types.InlineKeyboardMarkup()

WALLPAPER = {
    "Hot ️‍🔥" : "hot",
    "Top ❤️" : "top"
}

items = list(WALLPAPER.keys())

wallpaper.add(
    InlineKeyboardButton(items[0],callback_data=items[0]),
    InlineKeyboardButton(items[1],callback_data=items[1])
    )

contact.add(InlineKeyboardButton("Contact Developer",callback_data="contact"))
contact.add(InlineKeyboardButton("Explore Wallpaper",callback_data="explore"))

wallpaper2.add(InlineKeyboardButton("Explore Wallpaper",callback_data="explore"))

def sleep(seconds: int):
    start = time.time()
    while (time.time() - start < seconds):
        pass

@bot.message_handler(commands=['start'])
def start(message):

    msg = rf'''
    Koniciwa!, {message.from_user.first_name}
Nice to meet you 😊

I'm Asuna and I will send you wallpaper as per your interest.
If you have any suggestions, please feel free to contact my developer
    '''

    bot.send_photo(message.chat.id, caption=msg, photo=open('pfp.jpg','rb'), reply_markup=contact)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data in WALLPAPER.keys():

        while True:
            raw_title, url = WP.wallpaper(WALLPAPER.get(call.data))

            if url == "None":
                continue
            else:
                break
        title = raw_title.replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`").replace("]","\\]").replace("(","\\(").replace(")","\\)").replace("-","\\-").Welcome to Gboard clipboard, any text that you copy will be saved here.replace(".","\\.")
        filename = image.download(call.message.chat.id, url)
        photo_url = f"{title}\n[Download Here]({url})"
        sleep(1)

        try:
            bot.send_photo(call.message.chat.id, caption=photo_url, photo=open(filename, 'rb'), parse_mode="MarkdownV2", reply_markup=wallpaper)
        except Exception as e:
            try:
                bot.send_document(call.message.chat.id, caption=photo_url, document=open(filename, 'rb'), parse_mode="MarkdownV2", reply_markup=wallpaper)
            except Exception as e:
                bot.send_message(call.message.chat.id, text=str(e), reply_markup=wallpaper)
        try:
            os.remove(filename)
        except Exception as e: print("Could not remove")
    
    if call.data == 'explore':
        bot.send_message(call.message.chat.id, text="I only Provide High Quality Wallpaper 😁", reply_markup=wallpaper)
    
    if call.data == 'contact':
        developer = r"""**Thanks** for using my Bot\.
I hope, this kills your trouble to find wallpapers\.

If you have any problems or suggestions, you can contact me through [Twitter](twitter.com/saikatdas_) or directly [DM me on Telegram](https://t.me/saikat0326)
            
Have a nice day \!
        """
        bot.send_message(call.message.chat.id, text=developer, parse_mode='MarkdownV2',
                            reply_markup=wallpaper2, disable_web_page_preview=True)

bot.polling()
