import time
import logging
from os import getenv
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

    @app.route('/info')
    def info():
        logging.warning('Watch out!')  # will print a message to the console
        logging.info('I told you so')  # will not print anything
        values = range(3)
        for i in values:
            app.logger.info('Info log {}'.format(i))

        return "info!"

    @app.route('/debug')
    def debug():
        values = range(3)
        for i in values:
            app.logger.debug('debug log {}'.format(i))

        return "debug!"
    
    @app.route('/error')
    def error():
        values = range(3)
        for i in values:
            app.logger.error('error log {}'.format(i))

        return "error!"

    app.run(debug=True, host='0.0.0.0')
