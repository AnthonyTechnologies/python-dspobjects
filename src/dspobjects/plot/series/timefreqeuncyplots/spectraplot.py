"""spectraplot.py

"""

# Header #
__package_name__ = "dspobjects"

__author__ = "Anthony Fong"
__credits__ = ["Anthony Fong"]
__copyright__ = "Copyright 2021, Anthony Fong"
__license__ = "MIT"

__version__ = "0.5.0"


from ....header import *

# Imports #
# Standard Libraries #

# Third-Party Packages #

# Local Packages #
from ..stackedseriesplot import StackedSeriesPlot


# Definitions #
# Classes #
class SpectraPlot(StackedSeriesPlot):
    """

    Class Attributes:

    Attributes:

    Args:

    """

    default_x_unit: str | None = "Hz"