import ConfigParser
import os


class Configuration(object):
    # Absolute path of configuration file
    __file_name = './general_settings.cfg'

    @classmethod
    def get(cls, section, option):
        '''
        Gets a configuration value.
        :param section: String containing the section of the configuration.
        :param option: String containing the name of the configuration to get.
        :return: A string containing the configuration value.
        '''
        configuration = ConfigParser.RawConfigParser()
        if os.path.isfile(cls.__file_name):
            configuration.read(cls.__file_name)
            configuration_value = configuration.get(section, option)
            return configuration_value
        else:
            raise IOError('File "%s" does not exist.' % cls.__file_name)

    @classmethod
    def get_int(cls, section,option):
        c = cls.get(section, option)
        return int(c)

    @classmethod
    def get_list(cls, section, option):
        l = str(cls.get(section, option))
        return [int(i) for i in l.split(',')]


    @classmethod
    def get_boolean(cls, section, option):
        '''
        Gets a boolean configuration value.
        A convenience method which coerces the option in the specified section to a Boolean value.
        Note that the accepted values for the option are "1", "yes", "true", and "on", which cause this method
        to return True, and "0", "no", "false", and "off", which cause it to return False. These string values
        are checked in a case-insensitive manner. Any other value will cause it to raise ValueError.
        :param section:
        :param option:
        :return:
        '''
        _boolean_states = {'1': True, 'yes': True, 'true': True, 'on': True,
                           '0': False, 'no': False, 'false': False, 'off': False}

        v = cls.get(section, option)
        if v.lower() not in _boolean_states:
            raise ValueError('Not a boolean: {}'.format(v))
        return _boolean_states[v.lower()]
