import pandas as pd
import glob


def read_csvs(path):
    """Reads the banking file CSVs (for multiple accounts) and concatenates them in one DataFrame

       Parameters
       ----------
       path : str
           The directory where one or more csv files are located

       Returns
       -------
       DataFrame
           All banking files. The Account name is stated in column 'Konto'
       """
    files = glob.glob(path + "/*.csv")
    data_list = []
    for file in files:
        print("Loading file:", file)
        account = pd.read_csv(file, header=None, nrows=1, sep=";").iloc[0, 1]
        data = pd.read_csv(file, skiprows=4, sep=";")
        data["Konto"] = account
        data_list.append(data)
    return (pd.concat(data_list))
