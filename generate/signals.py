import numpy as np
import math
from typing import Callable
from .utils import normalize, unbias

PI2 = math.pi * 2

class Signal:
    """
    Represents a time-varying signal.
    """
    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return: sinusoid signal
        """
        pass

    def make_wave(self, duration: float = 1, start: float = 0, fs: int = 125) -> np.ndarray:
        """
        Makes a wave
        :param duration: duration, seconds
        :param start: start time of signal, seconds
        :param fs: frames per second
        :return:
        """
        n = round(duration * fs)
        ts = start + np.arange(n) / fs
        return self.evaluate(ts)


class Sinusoid(Signal):
    """
    Represents a sinusoidal signal
    """
    def __init__(self, freq: float = 440, amp: float = 1.0, offset: float = 0, func: Callable = np.sin):
        """
        Initializes a sinusoidal signal.
        :param freq: frequency in Hz
        :param amp: amplitude
        :param offset: phase offset in radians
        """
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = func

    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return: sinusoid signal
        """
        ts = np.asarray(ts)
        phases = PI2 * self.freq * ts + self.offset
        ys = self.amp * self.func(phases)
        return ys

class TriangleSignal(Sinusoid):
    """
    Represents a triangle signal
    """
    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at given times
        :param ts: array of times
        :return:
        """
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
        ys = np.abs(frac - 0.5)
        ys = normalize(unbias(ys), self.amp)
        return ys


class SquareSignal(Sinusoid):
    """
    Represents a square signal
    """
    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluate the signal at the given times
        :param ts: array of times
        :return:
        """
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
        ys = self.amp * np.sign(unbias(frac))
        return ys


class Impulse(Signal):
    """
    Represents an impulse
    """
    def __init__(self, freq: float, amp: float = 1.0):
        self.locations = None
        self.freq = freq
        self.amp = amp

    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return:
        """
        ys = np.zeros(len(ts))
        indices = np.searchsorted(ts, self.locations)
        ys[indices] = self.amp
        return ys

    def make_wave(self, duration: float = 1, start: float = 0, fs: int = 125):
        """
        Makes a wave
        :param duration: duration, seconds
        :param start: start time of signal, seconds
        :param fs: frames per second
        :return:
        """
        self.locations = np.arange(start, start+duration, duration / self.freq)
        n = round(duration * fs)
        ts = start + np.arange(n) / fs
        ys = self.evaluate(ts)
        return ys


class Noise(Signal):
    """
    Represents a noise signal (abstract parent class).
    """
    def __init__(self, amp: float = 1.0):
        """
        Initializes a white noise signal
        :param amp: amplitude
        """
        self.amp = amp


class UncorrelatedUniformNoise(Noise):
    """
    Represents uncorrelated uniform noise
    """

    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return: noise signal array
        """
        ys = np.random.uniform(-self.amp, self.amp, len(ts))
        return ys


class UncorrelatedGaussianNoise(Noise):
    """
    Represents uncorrelated gaussian noise
    """

    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return: noise signal array
        """
        ys = np.random.normal(0, self.amp, len(ts))
        return ys


class BrownNoise(Noise):
    """
    Represent Brown noise
    """
    def evaluate(self, ts: np.ndarray) -> np.ndarray:
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return:
        """
        dys = np.random.uniform(-1, 1, len(ts))
        ys = np.cumsum(dys)
        ys = normalize(unbias(ys), self.amp)
        return ys