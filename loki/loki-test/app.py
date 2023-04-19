import logging
from os import getenv
from flask import Flask

if __name__ == '__main__':

    app = Flask(__name__)
    logging.basicConfig(
        level=logging.DEBUG, 
            format='{"timestamp":"%(asctime)s", "level":"%(levelname)s", "logger":"%(module)s", "message":"%(message)s"}'
    )

    @app.route('/info')
    def info():
        values = range(3)
        for i in values:
            app.logger.info('info log {}'.format(i))

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
    
    @app.route('/health')
    def health():
        return {'result': 'healthy'}

    app.run(debug=True, host='0.0.0.0')
