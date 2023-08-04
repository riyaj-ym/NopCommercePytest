from configparser import RawConfigParser

config = RawConfigParser()
config.read("./configurations/config.ini")


def read_configuration(section, option):
    return config.get(section=section, option=option)
