import telebot
from flask import Flask, request

app = Flask(__name__)

# Tu token del bot de Telegram
TOKEN = "7712475781:AAE3g240q7POFYTd_t8tBbHwI9dEpgBYuQQ"
bot = telebot.TeleBot(TOKEN)

# Ruta raíz para comprobar si está en línea
@app.route("/", methods=["GET"])
def index():
    return "Bot is running", 200

# Ruta del webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Unsupported Media Type', 415

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup()

    fitness_button = telebot.types.InlineKeyboardButton(
        text="Test de Fitness",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest.html"))

    personality_button = telebot.types.InlineKeyboardButton(
        text="Trivia de Personalidad",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest2.html"))

    tictactoe_button = telebot.types.InlineKeyboardButton(
        text="Tic Tac Toe",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest3.html"))

    ahorcado_button = telebot.types.InlineKeyboardButton(
        text="¡Ahorcado Extremo!",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest4.html"))

    reaction_button = telebot.types.InlineKeyboardButton(
        text="Desafío de Reacción Ultra",
        web_app=telebot.types.WebAppInfo(
            url="https://www.fitnessjohnny.com/fitnessjohnnytest5.html"))

    markup.row(fitness_button, personality_button)
    markup.row(tictactoe_button, ahorcado_button)
    markup.add(reaction_button)

    welcome_text = (
        "👋 <b>¡Bienvenido al bot FitnessJohnny!</b>\n\n"
        "Descubre tests interactivos y juegos para ponerte en forma y divertirte:\n"
        "• Test de Fitness\n"
        "• Trivia de Personalidad\n"
        "• Tic Tac Toe\n"
        "• <b>Ahorcado Extremo</b>\n"
        "• <b>Desafío de Reacción Ultra</b>\n\n"
        "Haz clic en uno para comenzar. Si necesitas ayuda, escribe <b>/start</b>."
    )

    bot.send_message(chat_id, welcome_text, reply_markup=markup, parse_mode="HTML")

# Mensajes que no son comandos
@bot.message_handler(func=lambda message: True)
def default_handler(message):
    bot.send_message(message.chat.id, "Por favor, escribe /start para comenzar.")

# Inicia el servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

