
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
with open('names.txt', 'r',encoding='utf-8') as f:
    names = f.read().split('\n')
with open('indexes.txt', 'r') as f:
    indexes = f.read().split('\n')
indexes = [int(i) for i in indexes]
def find_name(u_name):
    #u_name = input('enter your name in hebrew: ')
    found = False
    found_twice = False
    index = -1
    for i, m_name in enumerate(names):
        if u_name in m_name:
            if found:
                found_twice = True
                break
            else:
                found = True
                index = indexes[i]
    if found and not found_twice:
        return names[index],True
    elif found_twice:
        return 'too many matches for this name',False
        #find_name()
    else:
        return 'name not found',False
        #find_name()
    #input('press any key to exit')
# find_name()


def reply(update, context):
    """Send to the user the most recommended paths according to his query"""

    user_input = update.message.text
    output,status = find_name(user_input)
    if status:
        update.message.reply_text(output)
    else:
        update.message.reply_text(output)
    update.message.reply_text('תרצה לחפש עוד שם?')   
        # dp = updater.dispatcher
        # dp.add_handler(MessageHandler(Filters.text, reply))
    # keyboard = []
    # for i in range(10):

    #keyboard.append([InlineKeyboardButton(str(rank) + ") " + title, callback_data=int(i))])

    #reply_markup = InlineKeyboardMarkup(keyboard)
    #update.message.reply_text('בחר.י מסלול לפירוט',reply_markup=reply_markup)

    # handle choice of specific path
    #dp = context.dispatcher
    #dp.add_handler(CallbackQueryHandler(get_choice))


def start(update: Update, context: CallbackContext) -> None:
    """
    start the discussion with the bot
    """
    # start message and image
    update.message.reply_text('כתוב את שמך כדי לגלות מי הגמד שלך')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))


# bot handling
updater = Updater("5101989049:AAEprzfylIDpjo2WGTnUj98mel1xcF5tTAU")
print('created updater')
updater.dispatcher.add_handler(CommandHandler('start', start))
print('strat command')
updater.start_polling()
updater.idle()
