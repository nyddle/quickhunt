# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server, Command, Option
from quickhunt import create_app

manager = Manager(create_app)

manager.add_option('-e', '--env', dest='env', required=False, default='debug')

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_reloader = True,
    host = '0.0.0.0')
)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    host='0.0.0.0'
    manager.run()

