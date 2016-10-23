# coding=utf-8
import subprocess
from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

p = None

def start(bot, update):
    logger.info('Received the /start command')
    update.message.reply_text('Hello World!')
    global p
    p = subprocess.Popen(['python', 'grading-assigner.py'])

def hello(bot, update):
    logger.info('Received the /hello command')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def stop(bot, update):
    logger.info('Received the /stop command')
    update.message.reply_text('Stopping the grader script')
    global p
    p.terminate()

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
updater.dispatcher.add_handler(CommandHandler('stop', stop))
# updater.dispatcher.add_error_handler(any)
updater.start_polling()
updater.idle()