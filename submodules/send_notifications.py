import json, requests, datetime

def check_user_tasks(context):
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
			current_date = datetime.date.today()
			for task in tasks:
				days_left = getDifference(task["deadline"], current_date)
				if days_left <= 3 and days_left >= 0:
					if days_left == 0:
						days_left = "Today"
					expiring_tasks.append([task["task_name"], days_left])
			if len(expiring_tasks) != 0:
				send_reminders(user["name"], user["telegram_id"], expiring_tasks, context)

def getDifference(deadline, current_date): 
	deadlineparts = deadline.split('-');
	new_deadline = datetime.date(int(deadlineparts[0]), int(deadlineparts[1]), int(deadlineparts[2]))
	return (new_deadline - current_date).days

def send_reminders(todo_name, telegram_id, tasks, context):
	string = "Hello " + todo_name + ", this is a daily reminder that your following tasks are expiring soon:\n\n" + "Task Name ----- Days Left\n"
	for task in tasks:
		string = string + task[0] + " ----- " + str(task[1]) + "\n"
	context.bot.send_message(chat_id=telegram_id, text=string) 

def callback_timer(update, context):
	with open("./config/bot.json", "r") as file:
		is_su = json.load(file)["su"]
	if str(update.message.chat_id) == is_su:
		print("Queue started")
		context.job_queue.run_daily(check_user_tasks, datetime.time(16, 00, 00), context=context)

def stop_timer(update, context):
	with open("./config/bot.json", "r") as file:
		is_su = json.load(file)["su"]
	if str(update.message.chat_id) == is_su:
		print("Queue stopped")
		context.job_queue.stop()