import sys
sys.path.insert(0, '/var/www/uiju')

from uijuweb import app as application

if __name__ == '__main__':
    application.run(host='0.0.0.0')
