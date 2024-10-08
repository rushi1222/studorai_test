import os
import logging

# Function to read the contents of user.txt
def load_user_data():
    user_data_file = 'user.txt'
    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            return file.read()
    else:
        logging.error("user.txt file is missing.")
        return None
