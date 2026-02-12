"""__init__.py
Functions and classes for plotting data.
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
from .subplot import Subplot
from .tracecontainer import TraceContainer
from .figure import Figure
from .baseplot import BasePlot
from .plotgroup import PlotGroup, PlotOrKey, XAssignments, YAssignments