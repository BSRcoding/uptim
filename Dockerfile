# Use a slim Python image
FROM python:3.8.5-slim-buster

# Set environment variables
ENV PIP_NO_CACHE_DIR=1

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    bash \
    libffi-dev \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository containing the bot code
RUN git clone https://github.com/BSRcoding/uptim.git /root/ptb

# Set working directory to the cloned repo
WORKDIR /root/ptb

# Install the Python dependencies
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Set the command to start the bot using python3 -m shivu
CMD ["python3", "-m", "shivu"]
