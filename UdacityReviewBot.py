# coding=utf-8

from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    logger.info('Received the /start command')
    update.message.reply_text('Hello World!')

def hello(bot, update):
    logger.info('Received the /hello command')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def any(bot, update):
    logger.info('Received something strange') # TODO: add information about command received

try:
    token = open('UdacityReview_bot.token').readline()
except:
    logger.critical('Unable to open token file')
    raise 'Unable to open token file!'

logger.info('Token read successfully ' + token)
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
# updater.dispatcher.add_error_handler(any)
updater.start_polling()
updater.idle()