import pandas as pd
import pathlib
from sklearn.model_selection import train_test_split

try:   
    ROOT = pathlib.Path(__file__)
except NameError:
    ROOT = pathlib.Path('.')
BASE = ROOT.parent

dataset_csv_path = (BASE / 'dataset' / 'Dataset.csv').absolute().as_posix()
train_csv_path = (BASE / 'dataset' / 'Train.csv').absolute().as_posix()
test_csv_path = (BASE / 'dataset' / 'Test.csv').absolute().as_posix()

df = pd.read_csv(dataset_csv_path)

train_df = pd.DataFrame()
test_df = pd.DataFrame()

for item in sorted(df.groupby(by=['label'])):
    label, label_df = item
    train, test = train_test_split(label_df, test_size=0.2, random_state=0)
    train_df = train_df.append(train, ignore_index=True)
    test_df = test_df.append(test, ignore_index=True)
else:
    train_df = train_df.reset_index(drop=True)
    train_df.to_csv(train_csv_path)
    test_df = test_df.reset_index(drop=True)
    test_df.to_csv(test_csv_path)
