import requests
import json
import os
from configparser import ConfigParser
import logging as logger
from src.helpers.confighelper import ConfigHelper


# Method to save token in config.ini file


def get_access_token(self):
    try:
        config_helper = ConfigHelper()
        auth_base_url = config_helper.get_auth_base_url()
        token_payload = config_helper.get_token_payload()
        logger.info('token created')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.request("POST", auth_base_url, headers=headers, data=token_payload)
        if response.status_code == 200:
            access_token = response.json()['access_token']

            save_token_to_configfile(access_token)
            return access_token
        else:
            # access_token = 'none'
            logger.error('Failed to generate token')
            raise Exception("Sorry, Failed to generate token")
        # return access_token
    except Exception as e:
        logger.error('Failed to generate token: ' + str(e))
        raise Exception('Sorry, Failed to generate token: ' + str(e))


def save_token_to_configfile(access_token):
    cur_file_dir = os.path.dirname(os.path.realpath(__file__))
    file = os.path.join(cur_file_dir, '..', '..', 'config.ini')
    config_token = ConfigParser()
    config_token.read(file)
    logger.info(list(config_token.sections()))
    config_token.set('auth_config', 'token', access_token)
    with open(file, 'w') as configfile:
        config_token.write(configfile)

# call the above method

# get_access_token(None)
