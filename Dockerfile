# Use the official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    TOKEN='YOUR_BOT_TOKEN'

# Set working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot.py file and the welcome photo to the container
COPY bot.py .
COPY botphoto.jpg .

# Run the bot
CMD ["python", "bot.py"]
