import os
import sys

import pytest


if __name__ == "__main__":
    os.environ['APP_SETTINGS'] = 'TestingConfig'
    exitcode = pytest.main(['--cov-report', 'term-missing',
                            '--cov', 'basic_flask_app',
                            '--capture', 'no'])
    sys.exit(exitcode)
