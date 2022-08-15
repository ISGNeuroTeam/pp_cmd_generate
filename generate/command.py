import pandas as pd
import numpy as np
from .signals import Sinusoid
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class GenerateCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Positional("name", required=True, otl_type=OTLType.TEXT),
            Keyword("type", required=True, otl_type=OTLType.TEXT),
            Keyword("frequency", required=True, otl_type=OTLType.NUMERIC),
            Keyword("amplitude", required=False, otl_type=OTLType.NUMERIC),
            Keyword("offset", required=False, otl_type=OTLType.NUMERIC),
            Keyword("fs", required=True, otl_type=OTLType.NUMERIC),
            Keyword("duration", required=False, otl_type=OTLType.NUMERIC),
            Keyword("start", required=False, otl_type=OTLType.NUMERIC),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start generate command')
        # that is how you get arguments
        signal_name = self.get_arg("name").value
        signal_type = self.get_arg("type").value
        freq = self.get_arg("frequency").value
        amp = self.get_arg("amplitude").value or 1.0
        offset = self.get_arg("offset").value or 0.0
        duration = self.get_arg("duration").value or 1.0
        fs = self.get_arg("fs").value
        start = self.get_arg("start").value or 0.0

        if signal_type == "sinusoidal":
            signal = Sinusoid(freq=freq, amp=amp, offset=offset, func=np.sin)
            df[signal_name] = signal.make_wave(duration=duration, fs=fs, start=start)
        else:
            raise ValueError("Unknown signal type!")

        self.log_progress(f'Signal {signal_name} has been created.', stage=1, total_stages=1)

        return df
