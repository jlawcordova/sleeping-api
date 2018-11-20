"""
    Run
    ~~~

    Runs the application through the Flask CLI. Used for VSCode debugging in
    Windows but not needed in Linux.
"""
import sys
import re

from flask.cli import main

sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
sys.exit(main())
