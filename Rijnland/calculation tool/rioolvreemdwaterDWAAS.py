"""
Rioolvreemdwater calculations acording DWAAS methodology.

"""

from dataclasses import dataclass

import pandas as pd


@dataclass
class RioolvreemdwaterDWAAS:
    """Logic to calculate the amount of rioolvreemdwater.

    Returns:
        pd.DataFrame: rioolvreemdwater output.
    """

    def calculate(self, data: pd.DataFrame, theoretisch_dwa: float,) -> pd.DataFrame:
        """Calculate the amount of rioolvreemdwater.

        Args:
            data (pd.DataFrame): Input data.
            theoretisch_dwa (float): ...

        Returns:
            pd.DataFrame: Rioolvreemdwater output.
        """
        data = data.copy()

        nr_days = data["date"].count()
        debiet_sum = data["debiet"].sum()
        debiet_average = data["debiet"].mean()
        debiet_average_dwa = data.loc[data["dry_day"], "debiet"].mean()
        debiet_dwa_sum = theoretisch_dwa * nr_days
        debiet_rvw_sum = (debiet_average_dwa - theoretisch_dwa) * nr_days
        debiet_hwa_sum = debiet_sum - debiet_dwa_sum - debiet_rvw_sum
        rvw_perc_dwa = debiet_rvw_sum / debiet_dwa_sum
        rvw_perc_totaal = debiet_rvw_sum / debiet_sum

        result = pd.DataFrame(
            {
                "debiet_sum": [debiet_sum],
                "debiet_average": [debiet_average],
                "debiet_average_dwa": [debiet_average_dwa],
                "debiet_dwa_sum": [debiet_dwa_sum],
                "debiet_rvw_sum": [debiet_rvw_sum],
                "debiet_hwa_sum": [debiet_hwa_sum],
                "rvw_perc_dwa": [rvw_perc_dwa],
                "rvw_perc_totaal": [rvw_perc_totaal],
            }
        )

        return result
