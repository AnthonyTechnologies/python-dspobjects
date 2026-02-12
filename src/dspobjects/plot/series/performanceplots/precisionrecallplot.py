"""precisionrecallplot.py

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
from typing import Any

# Third-Party Packages #
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType

# Local Packages #
from .thresholdperformanceplot import ThresholdPerformancePlot


# Definitions #
# Classes #
class PrecisionRecallPlot(ThresholdPerformancePlot):
    """

    Class Attributes:

    Attributes:

    Args:

    """

    default_title_settings: dict[str, Any] = dict(text="Precision Recall")
    default_xaxis_settings: dict[str, Any] = ThresholdPerformancePlot.default_xaxis_settings | dict(
        title="Recall",
    )
    default_yaxis_settings: dict[str, Any] = ThresholdPerformancePlot.default_yaxis_settings | dict(
        title="Precision",
    )
    default_static_traces: dict[str, BaseTraceType] = {
        "performance_line": go.Scattergl(
            x=[0, 1],
            y=[0, 0],
            mode="lines",
            line=dict(width=6, color="black", dash="dash"),
        ),
    }
    default_x_unit = "Recall"
    default_y_unit = "Precision"