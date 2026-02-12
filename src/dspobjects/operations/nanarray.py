"""nanarray.py
A function that creates an array of NaNs.
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
from collections.abc import Iterable
from typing import Any

# Third-Party Packages #
import numpy as np

# Local Packages #


# Definitions #
def nan_array(shape: int | Iterable | tuple[int], dtype: object | None = None, **kwargs: Any) -> np.ndarray:
    """Creates an array of NaNs.

    Args:
        shape: The shape of the array to create.
        dtype: The data type of the array.
        **kwargs: The other numpy keyword arguments for creating an array.

    Returns:
        The array of NaNs.
    """
    a = np.zeros(shape=shape, dtype=dtype, **kwargs)
    try:
        a.fill(np.nan)
    except ValueError:
        pass

    return a