import pandas as pd
## Load Datasets
def load_dataset(data_url='data/titanic.csv'):
    data =pd.read_csv(data_url)
    return data