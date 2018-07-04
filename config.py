# coding=utf-8
# @File  : config.py
# @Author: PuJi
# @Date  : 3/22/18


class Config(object):
    """Base config class."""
    pass


class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgres://postgres:123@127.0.0.1:5432/ulord_test'
    # SQLALCHEMY_DATABASE_URI = "postgres://postgres:123@127.0.0.1:5432/jmilkfansblog"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:123456@192.168.14.45:3306/testblog'
    # SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite.db"
    # other sql connection string
    # main function :dialect+driver://username:password@host:port/database
    # 'mssql+pymssql://user:pass@IP:port/dbname'
    # 'mysql://user:pass@IP:port/dbname'
    # 'oracle://user:pass@IP:port/dbname'
    # 'postgresql://user:pass@IP:port/dbname'
    # 'sqlite://filepath'