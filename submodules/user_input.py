from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from submodules import miscellaneous as mc
import json, requests

def link_user(update, context):
    """
    Function to link user with their todo manager account.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    if context.args == []:
        update.message.reply_text("Usage: <b>/link &lt;email&gt;</b>", parse_mode=ParseMode.HTML)
        return None
    with open("./config/endpoint.json", "r") as file:
        endpoint = json.load(file)["endpoint"]
    res = requests.post(endpoint + "/link", data = {"email": context.args[0], "telegram_id": update.message.chat_id, "telegram_handle": update.message.from_user.username})
    if res.status_code == 200:
        update.message.reply_text("Todo Manager account & Telegram account successfully linked! You will now receive reminder notifications for your tasks. To disable notifications, please do so at your profile: https://todo-manager.tjtanjin.com/profile")
    elif res.status_code == 404:
        update.message.reply_text("User not found or telegram handle does not match.")
    elif res.status_code == 403:
        update.message.reply_text("Account already linked.")
    else:
        update.message.reply_text("An error has occurred, please contact an administrator.")
    return None

def entertain_me(update, context):
    """
    Function to show entertainment options to users.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    reply_markup = InlineKeyboardMarkup(mc.build_menu([InlineKeyboardButton("Play Age Of Empires", url="https://t.me/Ageofempire_bot")], n_cols=2))
    update.message.reply_text("Why not show some support for my game? :)", reply_markup=reply_markup)

def show_help(update, context):
    """
    Function to show help options to users.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    update.message.reply_text("""Here are the currently available commands:\n
        <b>/link &lt;email&gt;</b> - links your telegram and todo manager accounts\n
        <b>/entertain</b> - shows a list of entertainment options\n
        <b>/help</b> - displays the available commands\n
Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/todo_website">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None