<p align="center">
  <img src="https://i.imgur.com/5vut1a3.png" />
  <h1 align="center">Todo Manager Telegram Bot</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
Todo Manager Telegram Bot is one of three small projects that form up the Todo Manager project that can be found here:
```
https://github.com/tjtanjin/CVWO-Assignment
```
This repository contains work concerning the telegram bot for Todo Manager, which serves to send up telegram notifications/messages through communicating with our backend API server.

Application link:
```
https://todo-manager.tjtanjin.com
```

### Features
Todo Manager Telegram Bot was created in a bid to bring the application closer to users. In a time where messaging applications such as telegram are found in majority of mobile devices, allowing reminders on these platforms is a function that is much desired. With such a function integrated into our application, users can more easily see our reminders as well as perform actions. 

While there is much more that can be added to this project such as allowing create, read, update and delete operations through telegram messages, current work on this project has been paused in lieu of the amount of time and effort that would be required. However, owing to the project structure of the Todo Manager project, the API endpoints for these operations are ready for use and implementing these features when I have more free time will be much more easier.

If you are interested in the full list of our application's current features, please refer to our user guide:
```
https://github.com/tjtanjin/todo_website/wiki/User-Guide
```

### Technologies
Technologies used by Todo Manager Telegram Bot is as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Deployed on:
<p align="center">
  <img height="150" width="150" src="https://i.dlpng.com/static/png/404295_thumb.png" />
</p>
<p align="center">
DigitalOcean
</p>

##### Project Repository
```
https://github.com/tjtanjin/todo_bot
```

### Setup
The following section will guide you through setting up your own Todo bot (telegram account required).
* First, head over to [BotFather](https://t.me/BotFather) and create your own telegram bot with the /newbot command. After choosing an appropriate name and telegram handle for your bot, note down the bot token provided to you.
* Next, cd to the directory of where you wish to store the project and clone this repository. An example is provided below:
```
$ cd /home/user/exampleuser/projects/
$ git clone https://github.com/tjtanjin/todo_bot.git
```
* Following which, create a config folder and within it, create a token.json file, saving the token you received from [BotFather](https://t.me/BotFather) as a value to the key "token" as shown below:
```
{"token": "your bot token here"}
```
* Under the same config folder, create another file called endpoint.json which would contain the API endpoint as value to the endpoint key. An example is shown below:
```
{"endpoint": "your_endpoint_ip_address/api/v1"}
```
* Then, create a third file within the config folder called bot.json with the following example fields which would support additional admin commands for /start and /stop. You may use dummy values if you have no interest in these 2 commands.
```
{"su": "your_telegram_id", "email": "your_email_account_on_todo_website", "password":"your_account_password"}
```
* Finally, from the base directory of the project, execute the following command and the terminal should print "Running..." if everything has been setup correctly!
```
$ python3 todo-manager-bot.py
```
* Note that with all these setup, only the telegram bot is working. Reminders and linking will not work unless the API is setup correctly. For that, please refer to the setup guide [here](https://github.com/tjtanjin/todo_api#setup).
* If you wish to host your telegram bot online 24/7, do checkout the guide [here](https://gist.github.com/tjtanjin/ce560069506e3b6f4d70e570120249ed).

### Team
* [Tan Jin](#https://github.com/tjtanjin)

### Contributing
If you have code to contribute to the project, open a pull request and describe clearly the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an issue.
### Others
If there are any questions pertaining to the application itself, kindly use the chatbot found at the bottom right corner of our application (https://todo-manager.tjtanjin.com).

For any questions regarding the implementation of the project, please drop me an email at: cjtanjin@gmail.com.
