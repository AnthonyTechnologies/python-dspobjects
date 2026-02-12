"""__init__.py
Classes and tools for handling timing.
"""

# Header #
__package_name__ = "dspobjects"

__author__ = "Anthony Fong"
__credits__ = ["Anthony Fong"]
__copyright__ = "Copyright 2021, Anthony Fong"
__license__ = "MIT"

__version__ = "0.5.0"


# Imports #
# Local Packages #
from .getlocalzone import get_localzone
from .timestamp import Timestamp, NANO_SCALE
from .nanostamp import nanostamp