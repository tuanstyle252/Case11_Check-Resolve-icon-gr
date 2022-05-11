import configparser

config = configparser.RawConfigParser()
configFilesPath = "D:\\PycharmProjects\\cas1_gr\\configuration\\config.ini"
config.read(configFilesPath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassWord():
        password = config.get('common info', 'password')
        return password