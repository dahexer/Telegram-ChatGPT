import openai
import configparser
from openai import OpenAI
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
# Read configuration from file
def read_config():
    config = configparser.ConfigParser()
    config.read('preferences.conf')
    return config['DEFAULT']



# Command handlers
async def start(update, context):
    await update.message.reply_text('Hello! I am your chatbot. Type any message and I will respond.')

async def help_command(update, context):
    await update.message.reply_text('/start - Start interacting with the bot\n/help - Get help info\n/info - Get bot information')

async def info(update, context):
    await update.message.reply_text('This bot uses OpenAI\'s GPT-4 to chat. Enjoy!')

# Handle messages using OpenAI GPT-4
async def handle_message(update, context):
    user_message = update.message.text
    config = read_config()
    client = OpenAI(api_key=config['OPENAI_API_KEY'])

    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "user", "content": user_message}
        ])
        chat_response = response.choices[0].message.content
    except Exception as e:
        chat_response = "Error processing the message: " + str(e)

    await update.message.reply_text(chat_response)

def main():
    config = read_config()

    application = Application.builder().token(config['TELEGRAM_API_KEY']).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
