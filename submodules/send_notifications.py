from telegram import ParseMode
import json, requests, datetime, pytz

def check_user_tasks(context):
	"""
	Function to check the task of users and decide who should receive reminders for those expiring within the next 3 days. 
	Reminders are sent once at 12am per day.
	Args:
        context: default telegram arg
	"""
	print("Checking to send reminders...")
	with open("./config/endpoint.json", "r") as file:
		endpoint = json.load(file)["endpoint"]
	with open("./config/bot.json", "r") as file:
		creds = json.load(file)
	auth_res = requests.post(endpoint + "/authenticate", data = {"email": creds["email"], "password": creds["password"]})
	token = json.loads(auth_res.content)["auth_token"]
	get_user_res = requests.get(endpoint + "/users", headers = { "Authorization": "Bearer " + token})
	users = json.loads(get_user_res.content)
	for user in users:
		if user["telegram_notifications"] == "1" and user["telegram_id"] != None:
			get_task_res = requests.get(endpoint + "/users/" + str(user["id"]) + "/tasks", headers = { "Authorization": "Bearer " + token})
			tasks = json.loads(get_task_res.content)
			expiring_tasks = []
			timezone = pytz.timezone("Asia/Singapore")
			unaware_date = datetime.datetime.now()
			current_date = pytz.utc.localize(unaware_date, is_dst=None).astimezone(timezone).date()
			for task in tasks:
				days_left = getDifference(task["deadline"], current_date)
				if days_left <= 3 and days_left >= 0 and task["priority"] != "Completed" and task["priority"] != "Overdue":
					if days_left == 0:
						days_left = "Today"
					expiring_tasks.append([task["task_name"], days_left])
			if len(expiring_tasks) != 0:
				send_reminders(user["name"], user["telegram_id"], expiring_tasks, context)

def getDifference(deadline, current_date):
	"""
	Function to get the day difference between current date and due date.
	Args:
		deadline: the date to compare with today
		current_date: the date today
	"""
	deadlineparts = deadline.split('-');
	new_deadline = datetime.date(int(deadlineparts[0]), int(deadlineparts[1]), int(deadlineparts[2]))
	return (new_deadline - current_date).days

def send_reminders(todo_name, telegram_id, tasks, context):
	"""
	Function to send reminders out to users.
	Args:
		todo_name: username on todo manager account
		telegram_id: telegram_id of the user
		tasks: tasks that are expiring
		context: default telegram arg
	"""
	string = "Hello " + todo_name + ", this is a daily reminder that your following tasks are expiring soon:\n\n" + "Task Name ----- Days Left\n"
	for task in tasks:
		task_name, days_left = formatMessage(task[0], str(task[1]))
		string = string + task_name + " ----- " + days_left + "\n"
	string = "<pre>" + string + "</pre>"
	context.bot.send_message(chat_id=telegram_id, text=string, parse_mode=ParseMode.HTML)

def formatMessage(task_name, days_left):
	"""
	Function to format the reminder message before it is sent to users.
	Args:
		task_name: name of the task
		days_left: days left to task expiry
	"""
	for chars in range(0, 10):
		if len(task_name) < 9:
			task_name = task_name + " "
		elif len(task_name) > 9:
			task_name = task_name[:6] + "..."
		else:
			break
	for chars in range(0, 10):
		if len(days_left) < 9:
			days_left = " " + days_left
		elif len(days_left) > 9:
			days_left = "Invalid"
			break
		else:
			break
	return [task_name, days_left]

def callback_timer(update, context):
	"""
	Function to control the job queue for telegram (start).
	Args:
		update: default telegram arg
		context: default telegram arg
	"""
	with open("./config/bot.json", "r") as file:
		is_su = json.load(file)["su"]
	if str(update.message.chat_id) == is_su:
		print("Queue started")
		context.job_queue.run_daily(check_user_tasks, datetime.time(16, 00, 00), context=context)

def stop_timer(update, context):
	"""
	Function to control the job queue for telegram (stop).
	Args:
		update: default telegram arg
		context: default telegram arg
	"""
	with open("./config/bot.json", "r") as file:
		is_su = json.load(file)["su"]
	if str(update.message.chat_id) == is_su:
		print("Queue stopped")
		context.job_queue.stop()