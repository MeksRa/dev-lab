import os
from typing import Final

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()


def load_env_var(var: str) -> str:
    value = os.getenv(var, "")
    if not value:
        raise ValueError(f"{var} not found in environment variables.")
    return value


BOT_TOKEN: Final[str] = load_env_var("BOT_TOKEN")
BOT_USERNAME: Final[str] = load_env_var("BOT_USERNAME")

# -- --- -- --- --


# make it for each command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! Nice to meet you! Let's chat!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just type something and I will respond to you!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command.")


# --- -- ---


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hey there!"
    if "how are you" in processed:
        return "I am good, thanks!"
    if "i love python" in processed:
        return "Python is cool!"

    return "I do not understand..."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Log
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Handle message type
    if message_type == "group":  # answer in groups only if mentioned
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    # Reply
    print("Bot:", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


def main() -> None:
    print("Starting up bot...")
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)


if __name__ == "__main__":
    main()
