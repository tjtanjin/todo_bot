from telegram.ext import Updater, CommandHandler
from submodules import user_input as ui
from submodules import send_notifications as sn
import json

def main():
	print("Running...")
	with open("./config/token.json", "r") as file:
		token = json.load(file)["token"]
	updater = Updater(token, use_context=True, workers=4)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("link", ui.link_user, pass_args=True))
	dp.add_handler(CommandHandler("entertain", ui.entertain_me, pass_args=True))
	dp.add_handler(CommandHandler("help", ui.show_help))
	dp.add_handler(CommandHandler("start", sn.callback_timer, pass_job_queue=True))
	dp.add_handler(CommandHandler("stop", sn.stop_timer, pass_job_queue=True))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()