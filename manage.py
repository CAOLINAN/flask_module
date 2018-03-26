# coding=utf-8
# @File  : manage.py
# @Author: PuJi
# @Date  : 3/22/18

# from flask.ext.script import Manager, Server
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

import blog
import module


# Init manager object via app object
manager = Manager(blog.app)

# Init migrate object via app and db object
migrate = Migrate(blog.app, module.db)

# Create some new commands
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    """create a python CLI.


    return:Default import object
    type:'Dict'
    """
    return dict(app=blog.app,
                db=module.db,
                User=module.User,
                Post=module.Post,
                Comment=module.Comment,
                Tag=module.Tag)


if __name__ == '__main__':
    manager.run()
