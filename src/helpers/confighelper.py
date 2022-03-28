import os
from configparser import ConfigParser


class ConfigHelper(object):

    def __init__(self):
        cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(cur_file_dir, '..', '..',
                            'config.ini')
        config = ConfigParser()
        config.read(file)
        self.config = config

    def get_base_url(self):
        return self.config['app_config']['base_url']

    def get_access_token(self):
        return self.config['auth_config']['token']

    def get_auth_base_url(self):
        return self.config['auth_config']['auth_base_url']

    def get_token_payload(self):
        client_id = self.config['auth_config']['client_id']
        cs = self.config['auth_config']['client_secret']
        token_payload = 'grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + cs
        return token_payload

# print(config.sections())
# print(config['configdata']['base_url'])

# config.add_section('Test')
# config.set('Test', 'new', '123')
# config.set('configdata', 'base_url', '123')
# with open(file, 'w') as configfile:
# config.write(configfile)
