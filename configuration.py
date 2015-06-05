import ConfigParser
import os
import time


class Configuration(object):
    
    """
    Returns dict object representing config key/values
    """
    
    CONFIGS_ENV_VARIABLE = 'PY_BAMBOO_CONFIG' 
    
    def _get_configs_fqdn_file(self):
        fqdn_file = os.environ.get(self.CONFIGS_ENV_VARIABLE)
        return fqdn_file
    
    def _open_and_get_configs(self):
        configs = ConfigParser.ConfigParser()
        configs.read(self._get_configs_fqdn_file())
        return configs
    
    def get_config(self, config_key, section='default'):
        configs = self._open_and_get_configs()
        config_value = configs.get(section, config_key)
        return config_value
    
    
    
    
        
    
    