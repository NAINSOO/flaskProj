from pathlib import Path

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "1234"
    WTF_CSRF_SECRET_KEY = "randomvalue1234000"

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLE = False

config = {
    "testing" : TestConfig,
    "local" : LocalConfig,
}