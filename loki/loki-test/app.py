import logging
from os import getenv
from flask import Flask
from random import randint

if __name__ == '__main__':

    app = Flask(__name__)
    logging.basicConfig(
        level=logging.DEBUG, 
            format='{"timestamp":"%(asctime)s", "level":"%(levelname)s", "logger":"%(module)s", "message":"%(message)s"}'
    )

    @app.route('/info')
    def info():
        values = range(3)
        app.logger.info('Info log')

        return "info!"

    @app.route('/debug')
    def debug():
        values = range(3)
        for i in values:
            random = randint(1, 100)
            app.logger.debug('{}'.format(random))

        return "debug!"
    
    @app.route('/error')
    def error():
        values = range(3)
        for i in values:
            app.logger.error('Error log {}'.format(i))

        return "error!"
    
    @app.route('/health')
    def health():
        return {'result': 'healthy'}

    app.run(debug=True, host='0.0.0.0')
