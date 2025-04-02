import pandas as pd


def read():
    """"
      Read input

      :return:
        str

    """
    return input('? :')


def read_file(file):
    """
      Read a file
      :param
        file: str, path to file
      :return:
        str
    """
    with open(file, 'r') as f:
        return f.read()


def read_file_with_pandas(file):
    """
      Read a csv file
      :param:
        path: str, path to file
      :return:
        String
    """
    return pd.read_csv(file).to_string()
