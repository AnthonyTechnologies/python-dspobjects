"""getlocalzone.py
Gets the local time zone.
"""

# Header #
__package_name__ = "dspobjects"

__author__ = "Anthony Fong"
__credits__ = ["Anthony Fong"]
__copyright__ = "Copyright 2021, Anthony Fong"
__license__ = "MIT"

__version__ = "0.5.0"


# Imports #
# Standard Libraries #
from datetime import timedelta, timezone
import time

# Third-Party Packages #

# Local Packages #


# Definitions #
# Functions #
def get_localzone() -> timezone:
    """Gets the local time zone.

    Returns:
        The system's current time zone.
    """
    local_time = time.localtime()
    return timezone(timedelta(seconds=local_time.tm_gmtoff), local_time.tm_zone)