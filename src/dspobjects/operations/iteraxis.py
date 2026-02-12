"""iteraxis.py
A function that iterates over a specific dimension of a ndarray.
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

# Third-Party Packages #
import numpy as np

# Local Packages #


# Definitions #
# Functions #
def iteraxis(a: np.ndarray, axis: int = 0) -> np.ndarray:
    """Iterates over a given axis of an array.

    Args:
        a: The array to iterate through.
        axis: The axis to iterate over.

    Returns:
        The data at an element of the axis.
    """
    if axis == 0:
        return a
    else:
        return np.moveaxis(a, axis, 0)