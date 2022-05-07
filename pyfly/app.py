from fly_bbs import create_app
import os

config_name = os.environ.get('FLASK_CONFIG') or 'Dev'
app = create_app(config_name)


if __name__ == '__main__':
    app( )

