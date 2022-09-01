import numpy as np


def normalize(ys: np.ndarray, amp: float = 1.0) -> np.ndarray:
    """
    Normalize a signal array so the maximum amplitude is +amp or -amp
    :param ys: signal array
    :param amp: max amplitude
    :return:
    """
    high, low = abs(max(ys)), abs(min(ys))
    return amp * ys / max(high, low)

def unbias(ys: np.ndarray) -> np.ndarray:
    """
    Shifts signal array so it has mean 0
    :param ys: signal array
    :return:
    """
    return ys - ys.mean()