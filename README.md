# Tom Ticket Reports

A Telegram Bot made to send TomTicket reports on a chat.

## Installation

This repository uses [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) to have a functional Telegram python bot.

```bash
$ pip install pyTelegramBotAPI
```
Then clone the repository and edit the following files in order to customize it at your own taste.

init.py
```python
bot_api = "YOURKEYGOESHERE" #Telegram bot API key
tt_key = "YOURTOKENGOESHERE" #TomTicket token API
```

deps.py - edit the data object with your departaments infos.
```python
data = {
	'department':{
		'dp_id':'YOURDPID',
		'dp_name':'DPNAME'
	},
	'other_department':{
		'dp_id':'OTHERDP',
		'dp_name':'OTHERDP'
	}
}
```

chats.py
```python
ids = [99999999, -1000000000] #ids of the chats that are able to use the commands
```

## Usage

Run the bot with the following command:
```bash
$ python bot.py
```

Then just send the commands on a chat with permissions and you're done.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
