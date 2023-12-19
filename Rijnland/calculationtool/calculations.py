"""
Executable functions to make the calculations for RIANT

"""

from dataclasses import dataclass
import pandas as pd
import numpy as np
from calculationtool import RioolvreemdwaterDWAAS


@dataclass
class RIANT:
    """Run the required calculations for RIANT.

    Returns:
        pd.DataFrame: Output dataframe.
    """
    #settings precipitation for calculation dry days      
    precip_threshold: float = 0.5
    precip_window: int = 2
    precip_center: bool = False


    def calculate_dry_day(
            self,
            neerslag: pd.Series,
        ) -> np.ndarray:
            """Calculate which days are dry days.

            Args:
                neerslag (pd.Series): Neerslag dataframe.

            Returns:
                np.ndarray: Values of True or False.
            """
            neerslag = neerslag.copy()
            dry_day = (
                neerslag.rolling(window=self.precip_window, center=self.precip_center)
                .max()
                .lt(self.precip_threshold)
                .values
            )
            return dry_day

    def calculate_rvw_results(
                self,
                theoretische_dwa,
                data):

        #dry days
        data = data.copy()
        data["dry_day"] = self.calculate_dry_day(data["neerslag"])
        #Rioolvreemdwater
        rvw = RioolvreemdwaterDWAAS()
        rvw_results = rvw.calculate(data,
                                    theoretische_dwa = theoretische_dwa)
        
        return rvw_results
    