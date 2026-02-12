"""test_precisionrecallplot.py

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
from src.dspobjects.plot import PrecisionRecallPlot


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


class TestPrecisionRecallPlot:
    def generate_data(self, samples=1024, channels=10):
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

    def test_precisionrecall_figure(self):
        x, y = self.generate_data()
        plot1 = PrecisionRecallPlot(
            x=x,
            y=y,
        )
        plot1._figure.show()

    def test_precisionrecall_subplot(self):
        x, y = self.generate_data()
        fig = Figure()
        fig.update_layout(title="Figure Name")
        fig.update_layout(PrecisionRecallPlot.default_layout_settings)
        fig.set_subplots(3, 1, horizontal_spacing=0.05, vertical_spacing=0.05)
        plot1 = PrecisionRecallPlot(subplot=fig.subplots[0][0], x=x, y=y)
        plot2 = PrecisionRecallPlot(subplot=fig.subplots[1][0], x=x, y=y)
        plot1.update_title(text="Test Name")
        # plot2 = TimeSeriesPlot(subplot=fig.subplots[0][1], y=data, sample_rate=1024.0)
        fig.show()