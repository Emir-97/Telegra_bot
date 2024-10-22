import logging
from telegram.ext import *
from telegram import Update
import responses

API_KEY = '7681079383:AAFloMlvv4YOTpdBsVcXFB90VUTDsBljg44'

# set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

async def start_command(update: Update, context):
    await update.message.reply_text('Hello there! I am a bot. What\'s up?')

async def help_command(update: Update, context):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')

async def custom_command(update: Update, context):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')

async def handle_message(update: Update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    response = responses.get_response(text)

    # Bot responses
    await update.message.reply_text(response)

async def error(update: Update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    application = Application.builder().token(API_KEY).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('custom', custom_command))

    # Messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    application.add_error_handler(error)

    # Run the bot
    application.run_polling(poll_interval=1.0)