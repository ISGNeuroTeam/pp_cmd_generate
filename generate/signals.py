import numpy as np
import math
from typing import Callable

PI2 = math.pi * 2

class Signal:
    """
    Represents a time-varying signal.
    """
    def evaluate(self, ts: np.ndarray):
        """
        Evaluates the signal at the given times
        :param ts: array of times
        :return: sinusoid signal
        """
        pass

    def make_wave(self, duration: float = 1, start: float = 0, fs: int = 125):
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

