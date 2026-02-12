"""test_rocprecisionrecallgroup.py

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
import abc
import pathlib

# Third-Party Packages #
import pytest
import numpy as np

# Local Packages #
from src.dspobjects.plot import Figure
from src.dspobjects.plot import ROCPrecisionRecallGroup


# Definitions #
# Classes #
# Functions #
@pytest.fixture
def tmp_dir(tmpdir):
    """A pytest fixture that turn the tmpdir into a Path object."""
    return pathlib.Path(tmpdir)


# Classes #
class ClassTest(abc.ABC):
    """Default class tests that all classes should pass."""

    class_ = None
    timeit_runs = 100000
    speed_tolerance = 200

    def test_instance_creation(self):
        pass


class TestROCPrecisionRecallGroup:
    def generate_data(self, samples=10240, channels=10):
        # Create Signal
        rng = np.random.default_rng()
        amp = 1
        noise_power = 0.0001
        carrier = 1 - amp / np.log(np.arange(1, samples + 1) * np.e)
        carrier = np.flip(carrier)
        y = np.repeat(carrier[:, None], channels, axis=1)
        noise = rng.normal(scale=np.sqrt(noise_power), size=(samples, channels))
        y += noise

        x = np.linspace(0, 1, samples)
        return x, y

    def test_rocprecisionrecallgroup_figure(self):
        x, y = self.generate_data()
        ts_group = ROCPrecisionRecallGroup()
        ts_group["roc"].build(x=x, y=y)
        ts_group["precisionrecall"].build(x=x, y=y)
        ts_group.figure.show()