import telebot
from flask import Flask
import threading

app = Flask(__name__)

# Poner el token directamente aquí
TOKEN = "7712475781:AAE3g240q7POFYTd_t8tBbHwI9dEpgBYuQQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()

    # Botón para Test de Fitness
    fitness_button = telebot.types.InlineKeyboardButton(
        text="Test de Fitness",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest.html"))

    # Botón para Trivia de Personalidad
    personality_button = telebot.types.InlineKeyboardButton(
        text="Trivia de Personalidad",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest2.html"))

    # Botón para Tic Tac Toe
    tictactoe_button = telebot.types.InlineKeyboardButton(
        text="Tic Tac Toe",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest3.html"))

    # Botón para Ahorcado Extremo
    ahorcado_button = telebot.types.InlineKeyboardButton(
        text="¡Ahorcado Extremo!",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest4.html"))

    # Botón para el Desafío de Reacción Ultra
    reaction_button = telebot.types.InlineKeyboardButton(
        text="Desafío de Reacción Ultra",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest5.html"))

    # Organiza los botones:
    markup.row(fitness_button, personality_button)
    markup.row(tictactoe_button, ahorcado_button)
    markup.add(reaction_button)

    welcome_text = (
        "👋 <b>¡Bienvenido al bot FitnessJohnny!</b>\n\n"
        "Descubre tests interactivos y juegos para ponerte en forma y divertirte:\n"
        "• Test de Fitness\n"
        "• Trivia de Personalidad\n"
        "• Tic Tac Toe (¡juega X y O!)\n"
        "• <b>Ahorcado Extremo</b> (¡Descubre tu destino, atrévete a jugar!)\n"
        "• <b>Desafío de Reacción Ultra</b> (¡Pon a prueba tus reflejos al máximo!)\n\n"
        "Elige una opción para comenzar. Si no sabes cómo empezar, escribe <b>/start</b>."
    )

    bot.send_message(chat_id,
                     welcome_text,
                     reply_markup=markup,
                     parse_mode="HTML")


@bot.message_handler(func=lambda message: True)
def default_handler(message):
    bot.send_message(message.chat.id,
                     "Por favor, escribe /start para comenzar.")


@app.route('/')
def home():
    return "OK", 200


def run_bot():
    bot.polling()


if __name__ == "__main__":
    # Inicia el bot en un hilo aparte y luego arranca Flask
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
