from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import json, requests

def link_user(update, context):
    """
    Function to link user with their todo manager account.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
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
    reply_markup = InlineKeyboardMarkup(build_menu([InlineKeyboardButton("Play Age Of Empires", url="https://t.me/Ageofempire_bot")], n_cols=2))
    update.message.reply_text("Why not show some support for my game? :)", reply_markup=reply_markup)

def show_help(update, context):
    """
    Function to show help options to users.
    Args:
        update: default telegram arg
        context: default telegram arg
    """
    update.message.reply_text("""Here are the currently available commands:\n
        <b>/link (email)</b> - links your telegram and todo manager accounts\n
        <b>/entertain</b> - shows a list of entertainment options\n
        <b>/help</b> - displays the available commands\n
Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/todo_website">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    """
    Function to build the menu buttons to show users.
    Args:
        buttons: buttons to press
        n_cols: number of cols
    """
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu