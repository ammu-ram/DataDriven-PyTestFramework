import configparser
config=configparser.RawConfigParser()
configFilePath = "C://Users/Admin/PycharmProjects/SwagLabshybrid/Configurations/config.ini"
config.read(configFilePath)

class ReadConfiguration():

    @staticmethod
    def url():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def username():
        username = config.get('common info','username')
        return username
    @staticmethod
    def password():
        password = config.get('common info','password')
        return password
