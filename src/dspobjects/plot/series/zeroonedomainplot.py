"""zeroonedomainplot.py

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
from typing import Any

# Third-Party Packages #

# Local Packages #
from .seriesplot import SeriesPlot


# Definitions #
# Classes #
class ZeroOneDomainPlot(SeriesPlot):
    """

    Class Attributes:

    Attributes:

    Args:

    """

    default_xaxis_settings: dict[str, Any] = dict(
        range=[0, 1],
        constrain="domain",
        scaleratio=1,
        tickmode="linear",
        tick0=0,
        dtick=0.10,
        minor=dict(ticks="outside", nticks=10, showgrid=True),
        showline=True,
        linewidth=2,
        linecolor="black",
        mirror=True,
    )
    default_yaxis_settings: dict[str, Any] = dict(
        range=[0, 1],
        constrain="domain",
        scaleratio=1,
        tickmode="linear",
        tick0=0,
        dtick=0.10,
        minor=dict(ticks="outside", nticks=10, showgrid=True),
        showline=True,
        linewidth=2,
        linecolor="black",
        mirror=True,
    )
    default_scaleanchor_x_to_y: bool = True
    default_scaleanchor_y_to_x: bool = True