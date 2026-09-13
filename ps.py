from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# Direct token — only for learning
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"


# Hardcoded greetings
GREETINGS = {
    "hi": "Hello 👋",
    "hello": "Hey! How are you? 😊",
    "hy": "Hey 👋 Nice to meet you!",
    "hey": "Hey there! 😄",
    "hii": "Hii 👋",
    "good morning": "Good morning! ☀️",
    "good afternoon": "Good afternoon! 🌤️",
    "good evening": "Good evening! 🌆",
    "bye": "Bye! 👋 Have a great day!",
}


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower().strip()

    # Check hardcoded greetings
    if message in GREETINGS:
        await update.message.reply_text(GREETINGS[message])
    else:
        await update.message.reply_text(
            "I don't understand that yet 🤔"
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Receive text messages
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()