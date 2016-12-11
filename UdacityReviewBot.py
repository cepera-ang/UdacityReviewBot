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
APItoken = ''

def start(bot, update):
    logger.info('Received the /start command')
    update.message.reply_text('Hello World!')
    global p, APItoken
    p = subprocess.Popen(['python3', 'grading-assigner.py', '-T'+ APItoken])

def hello(bot, update):
    logger.info('Received the /hello command')
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def stop(bot, update):
    global p
    logger.info('Received the /stop command, PID:' + str(p.pid))
    update.message.reply_text('Stopping the grader script, PID:' + str(p.pid))
    p.terminate()
    logger.info('Killed PID:' + str(p.pid))
    update.message.reply_text('Stopped the grader script')

def any(bot, update):
    logger.info('Received something strange') # TODO: add information about command received

try:
    lines = []
    for line in open('UdacityReview_bot.token').readlines():
        lines.append(line)
    token = lines[0].strip('\n')
    assert token == '295304941:AAG5mq8hklWjlHfkWF6_wvj5eH27xrOzhh0'
    APItoken = lines[1].strip('\n')
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