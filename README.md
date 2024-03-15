Sure! Here's the updated README.md file with the deployment section divided into two parts - one for VPS/Local deployment and the other for deploying on Heroku with a deploy button:

```markdown
# Telegram Bot

This is a Telegram bot built with Python using the python-telegram-bot library. The bot allows users to delete messages within a specified range in a Telegram channel.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/telegram-bot.git
   ```

2. **Install Dependencies:**
   ```bash
   cd telegram-bot
   pip install -r requirements.txt
   ```

3. **Set Up Telegram Bot:**
   - Create a new bot on Telegram and obtain the bot token.
   - Update the `bot.py` file with your bot token.

4. **Run the Bot Locally:**
   ```bash
   python bot.py
   ```

## Usage

Once the bot is running, you can interact with it in the following ways:

- **/start**: Starts the bot and welcomes the user with a photo, caption, and buttons.
- **/delete**: Initiates the process to delete messages within a specified range in a Telegram channel.
- **/help**: Provides assistance on how to use the bot.

## Deployment

### VPS/Local Deployment

To deploy the bot on your own server or locally, follow these steps:

1. **Set up a Virtual Private Server (VPS) or Local Environment:** 
   Ensure you have a server or local machine where you can run the bot.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/telegram-bot.git
   ```

3. **Install Dependencies:**
   ```bash
   cd telegram-bot
   pip install -r requirements.txt
   ```

4. **Set Up Telegram Bot:**
   - Create a new bot on Telegram and obtain the bot token.
   - Update the `bot.py` file with your bot token.

5. **Run the Bot:**
   ```bash
   python bot.py
   ```

### Heroku Deployment

You can deploy the bot to Heroku with just a few clicks:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click the button above to deploy the bot to Heroku. Don't forget to set your Telegram bot token as a config variable named `TOKEN` in the Heroku dashboard.

## Files and Directory Structure

- **bot.py**: Main Python script containing the bot's functionality.
- **welcome_photo.jpg**: Welcome photo sent by the bot.
- **requirements.txt**: List of Python dependencies.
- **Procfile**: Specifies the process type and command to run the bot on Heroku.
- **README.md**: This file, providing instructions and information about the bot.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

In the Heroku deployment section, the deploy button will directly deploy the bot to Heroku when clicked.
