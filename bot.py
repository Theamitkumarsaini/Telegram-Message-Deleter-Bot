#GitHub github.com/devgaganin
# Telegram : @dev_gagan

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters, Updater, CallbackQueryHandler
from uuid import uuid4

TOKEN = 'YOUR_BOT_TOKEN'

bot = Bot(token=TOKEN)

CHANNEL, START_MESSAGE_ID, END_MESSAGE_ID = range(3)

channel_message_ranges = {}

def start_deletion(update, context):
    update.message.reply_text("Please enter the channel ID (-100 imcluded)...")
    return CHANNEL

# Define a function to handle the channel ID
def handle_channel_id(update, context):
    channel_id = update.message.text
    context.user_data['channel_id'] = channel_id
    update.message.reply_text("Please enter the start message ID...")
    return START_MESSAGE_ID
  
def handle_start_id(update, context):
    try:
        start_message_id = int(update.message.text)
        context.user_data['start_message_id'] = start_message_id
        update.message.reply_text("Please enter the end message ID...")
        return END_MESSAGE_ID
    except ValueError:
        update.message.reply_text("Invalid message ID, restart process by /delete")
        return START_MESSAGE_ID

def handle_end_id(update, context):
    try:
        end_message_id = int(update.message.text)
        start_message_id = context.user_data['start_message_id']
        channel_id = context.user_data['channel_id']

        # Delete messages within the specified range
        for message_id in range(start_message_id + 1, end_message_id):
            try:
                bot.delete_message(chat_id=channel_id, message_id=message_id)
            except Exception as e:
                logger.error(f"Failed to delete message {message_id}: {str(e)}")

        update.message.reply_text(f"Deleted messages between {start_message_id} and {end_message_id} in channel {channel_id}.")

     
        context.user_data.clear()
        return ConversationHandler.END
    except ValueError:
        update.message.reply_text("Invalid message ID. Please enter a valid message ID.")
        return END_MESSAGE_ID

def start(update, context):
    photo = open('botphoto.jpg', 'rb')
    caption = "Welcome to Channel/Group Message Delete Bot! Click Help button to get started?"
    buttons = [
        [InlineKeyboardButton("Join Group", url="https://t.me/dev_gagan")],
        [InlineKeyboardButton("Help", callback_data="help")]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_photo(photo=photo, caption=caption, reply_markup=keyboard)
    return ConversationHandler.END

def help_command(update, context):
    update.message.reply_text("You can use the /delete command to delete messages in a specified range.")

def button(update, context):
    query = update.callback_query
    if query.data == "help":
        update.callback_query.answer()
        update.callback_query.message.reply_text("How to use this bot?\n\n1. Make Bot admin with delete right in channel/group in which you want to delete.\n2. Start /delete process and follow on going instructions")
    else:
        update.callback_query.answer()

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('delete', start_deletion), CommandHandler('start', start)],
    states={
        CHANNEL: [MessageHandler(Filters.text & ~Filters.command, handle_channel_id)],
        START_MESSAGE_ID: [MessageHandler(Filters.text & ~Filters.command, handle_start_id)],
        END_MESSAGE_ID: [MessageHandler(Filters.text & ~Filters.command, handle_end_id)],
    },
    fallbacks=[],
)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CallbackQueryHandler(button))

# Start the bot
if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
