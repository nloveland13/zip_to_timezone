import numpy as np
import pandas as pd

class GetTimeZones(object):
    zips = None
    data = None

    def __init__(self):
        pass

    @classmethod
    def __main__(cls, data, newfile):
        # data s/b in csv format
        cls.data = cls._load_data(data)
        cls.zips = cls._load_zips()

        cls.data['zip'] = cls.data['zip+4'].apply(lambda x: str(x[:5]))
        data_merged = cls.data.merge(cls.zips, how='left', on='zip')
        data_merged.to_csv(newfile)

    @staticmethod
    def _load_data(data):
        return pd.read_csv(data)

    @staticmethod
    def _load_zips(zips='zipcode.csv'):
        zips = pd.read_csv(zips)
        # zips import as int, need to convert to str for join
        zips['zip'] = zips['zip'].apply(lambda x: str(x))
        return zips


if __name__ == '__main__':
    GetTimeZones.__main__(argv[1], argv[2])
