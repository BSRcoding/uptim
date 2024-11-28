import time
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Store the start time when the bot starts
start_time = time.time()

# Command to get bot uptime
async def uptime(update: Update, context: CallbackContext) -> None:
    # Calculate the bot's uptime
    uptime_seconds = int(time.time() - start_time)
    
    # Convert uptime into hours, minutes, and seconds
    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60
    
    # Format the uptime message
    uptime_message = f"Bot has been running for: {hours} hours, {minutes} minutes, and {seconds} seconds."
    
    # Send the uptime message to the user
    await update.message.reply_text(uptime_message)

# Main function to set up the bot
async def main():
    # Use an environment variable to store the bot token for better security
    bot_token = os.getenv("7411570597:AAFJ33Kh-6xr4_28p8CDz78Nw6GSP7mQlnU")
    if not bot_token:
        raise ValueError("Bot token is not set. Please set the TELEGRAM_BOT_TOKEN environment variable.")
    
    # Create the Application and set the bot token
    application = Application.builder().token("7411570597:AAFJ33Kh-6xr4_28p8CDz78Nw6GSP7mQlnU").build()
    
    # Add command handler for /uptime
    application.add_handler(CommandHandler("uptime", uptime))
    
    # Run the bot with proper exception handling
    try:
        await application.run_polling()
    except Exception as e:
        print(f"Error running bot: {e}")

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
