import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN="1806533440:AAFMAoAB4Snpvcs78NYSIJSaP7zsZUXn4X4"

def start(update, context):
    print(update)
    author=update.message.from_user.first_name
    reply=f"Hey!! {author}"
    context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def _help(update, context):
    reply="This is a help text"
    context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def echo_text(update, context):
    reply= update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def echo_sticker(update, context):
    reply=update.message.sticker.file_id
    context.bot.send_sticker(chat_id=update.effective_chat.id,sticker=reply)

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update, update.error)


def main():
    # Create Updater
    updater = Updater(TOKEN)
    # Create Dispatcher
    dp = updater.dispatcher
    # Add handlers¶
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)   


    # Start Polling and wait for any signal to end the program¶
    updater.start_polling()
    logger.info("Started polling...")
    updater.idle()


if __name__=='__main__':
    main()