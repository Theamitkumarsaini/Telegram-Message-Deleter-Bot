# Telegram Channel Messages Deleter Bot

This is a Telegram bot built with Python using the python-telegram-bot library. The bot allows users to delete messages within a specified range in a Telegram channel or Group coded by [Team SPY](https:/t.me/dev_gagan).

## Deployment / Setup

### VPS/Local Deployment

To deploy the bot on your own server or locally, follow these steps:

1. **Set up a Virtual Private Server (VPS) or Local Environment:** 
   Ensure you have a server or local machine where you can run the bot.

2. **Clone the Repository:** Fork the repository and add star my repo
   ```bash
   git clone your_repo_link
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

Click the button above to deploy the bot to Heroku. Don't forget to set your Telegram bot token as a config variable named `TOKEN` in the `bot.py`.

## Usage

Once the bot is running, you can interact with it in the following ways:

- **/start**: Starts the bot and welcomes the user with a photo, caption, and buttons.
- **/delete**: Initiates the process to delete messages within a specified range in a Telegram channel.
- **/help**: Provides assistance on how to use the bot.

## Support

Feel free to reach out for support or follow me on various platforms:

[![Telegram](https://img.icons8.com/color/48/000000/telegram-app--v2.png)](https://t.me/dev_gagan)
[![Website](https://img.icons8.com/color/48/000000/domain.png)](https://devgagan.in/)
[![YouTube](https://img.icons8.com/color/48/000000/youtube-play.png)](https://youtube.com/@dev_gagan)
[![Instagram](https://img.icons8.com/color/48/000000/instagram-new.png)](https://instagram.com/devgagan.in)
[![GitHub](https://img.icons8.com/color/48/000000/github--v1.png)](https://github.com/devgaganin)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
