import telebot
from sell import item_to_sell
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot("5180693282:AAFI9QJrfIFLALzNKn6WZpEsZ8fjXgnkEq8", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN





@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello there {}, I AM A NEW BOT, WHAT CAN I DO TO YOU! And this is tutorial bot.\n You can use /catalog to know more".format(message.from_user.first_name))



@bot.message_handler(commands=['catalog'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Here is the catalog.", reply_markup=InlineKeyboardMarkup(
		[
			[
InlineKeyboardButton(text="Come to our shop.And google this here", url="https://www.google.co.in", callback_data="Clicked")
			]
		]
	))
	bot.send_photo(message.chat.id, photo="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.bigbasket.com%2Fmedia%2Fuploads%2Fp%2Fxxl%2F40033819-2_6-fresho-apple-shimla.jpg&imgrefurl=https%3A%2F%2Fwww.bigbasket.com%2Fpd%2F40033819%2Ffresho-apple-shimla-4-pcs%2F&tbnid=NsWrN6aohNC-iM&vet=12ahUKEwiLvrq9zf_3AhXSkdgFHfYtDxEQMygLegUIARDvAQ..i&docid=z6LVRZyBCyKMRM&w=900&h=900&q=apple&ved=2ahUKEwiLvrq9zf_3AhXSkdgFHfYtDxEQMygLegUIARDvAQ")

@bot.callback_query_handler(func = lambda m : True)
def callback_query_handler(callback_query):
	# print(callback_query)
	# print(callback_query.data)
	bot.answer_callback_query(callback_query.id)
	if callback_query.data=="Clicked":
		bot.send_message(callback_query.from_user.id, "Find me here.")

bot.infinity_polling()