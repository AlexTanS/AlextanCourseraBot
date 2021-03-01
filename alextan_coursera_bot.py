import telebot

# Globals variables
TOKEN = ""

# Create bot
bot = telebot.TeleBot(TOKEN)


# Print messages: user - bot
@bot.message_handler()  # связываем функцию с реальным действием
def handle_message(message):
    print(message.text)  # печать сообщения от Пользователя
    bot.send_message(message.chat.id, text="Сообщение пришло")  # отправка сообщения от бота Пользователю


# Run bot
bot.polling()  # периодическая проверка сервера Телеграмм на предмет новых сообщений
