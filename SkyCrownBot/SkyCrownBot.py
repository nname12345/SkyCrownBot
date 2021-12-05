import telebot

bot = telebot.TeleBot("5080456491:AAG04U9ujGZDNy-6Q7W9_w1Fwt1Eu9AdFJo", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, message.chat.first_name + ' 👑' ", добро пожаловать! Вы попали в самую стартегическую игру. Вам предостоит: "
													"\n\n 💎 Принимать важные стратегические решения. "
													"\n\n 💎 Учавстовать в войнах. "
													"\n\n 💎 Сохрнаить государственную казну и спасти Ваш народ от злых бедствий. "
													"\n\n Желаем удачи! Помните, что любое Ваше действие, меняет судьбу всего королевства. "
													"Порой, некоторые действия бывают обманчивы, по этому включайте свою инициативу, а также чувства лжи. "
													"Смекалка, верность перед народом — ключ к лучшей жизни.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, message.chat.first_name + ', здравствуйте!')
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBdOxgzFavLbl_Z6SpTXHYrRJm_r52pwACyg0AApFgIUix94gF8D5V-B8E")
	elif message.text == "Хай":
		bot.send_message(message.chat.id, message.chat.first_name + ', здравствуйтеыыыыыыыыыыыы!')

print('Запущен')
bot.polling()