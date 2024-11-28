# Clone the repository
RUN git clone https://github.com/BSRcoding/uptim.git /root/ptb

# Set the working directory
WORKDIR /root/ptb

# Install requirements
RUN pip install -r requirements.txt
