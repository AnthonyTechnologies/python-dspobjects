"""rocpercisionrecallgroup.py

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
from collections.abc import Mapping
from typing import Any

# Third-Party Packages #

# Local Packages #
from ...bases import BasePlot, PlotGroup
from .rocplot import ROCPlot
from .precisionrecallplot import PrecisionRecallPlot


# Definitions #
# Classes #
class ROCPrecisionRecallGroup(PlotGroup):
    """

    Class Attributes:

    Attributes:

    Args:

    """

    default_layout_settings: dict[str, Any] = PlotGroup.default_layout_settings | dict(
        dragmode="zoom",
        legend=dict(traceorder="reversed"),
        template="plotly_white",
        modebar_add=[
            "zoom",
            "pan",
            "drawline",
            "drawopenpath",
            "drawclosedpath",
            "drawcircle",
            "drawrect",
            "eraseshape",
        ],
    )
    default_subplot_settings: dict[str, Any] = dict(rows=1, cols=2, horizontal_spacing=0.05)
    default_plots: Mapping[str, BasePlot | PlotGroup] = dict(roc=ROCPlot, precisionrecall=PrecisionRecallPlot)
    # default_plot_settings: dict[str, dict[str, Any]] = dict(
    #     roc=dict(xaxis=dict(constraintoward="right")),
    #     precisionrecall=dict(xaxis=dict(constraintoward="left")),
    # )
    default_locations: dict[str, tuple[int, int]] = dict(roc=(0, 0), precisionrecall=(0, 1))
    default_legend_group = "all"