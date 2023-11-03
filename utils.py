"""Module providing a util funcions."""


def return_year_in_hs(GEC):
    """Converts student Cohort Code (GEC) to their year in HS"""
    CURRENT_YEAR = 2023
    GEC_dict = {
        "3": 2023,
        "2": 2022,
        "1": 2021,
        "Z": 2020,
        "Y": 2019,
        "X": 2018,
    }
    YEAR_STARTED_HS = GEC_dict.get(GEC)
    return CURRENT_YEAR - YEAR_STARTED_HS + 1
