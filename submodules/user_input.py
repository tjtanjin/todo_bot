from telegram import ParseMode
import json, requests

def link_user(update, context):
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

def show_help(update, context):
    update.message.reply_text("""Here are the currently available commands:\n
        <b>/link (email)</b> - links your telegram and todo manager accounts\n
        <b>/help</b> - displays the available commands\n
Have ideas and suggestions for this mini project? Head over to the <a href="https://github.com/tjtanjin/todo_website">Project Repository</a>!""", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    return None
