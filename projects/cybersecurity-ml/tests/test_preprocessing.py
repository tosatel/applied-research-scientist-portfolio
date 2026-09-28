import sys; sys.path.insert(0,'src')
import pandas as pd
from preprocessing import split_xy, FEATURES

def test_split_xy():
    d={f:[0,1] for f in FEATURES}; d['label']=[0,1]; X,y=split_xy(pd.DataFrame(d)); assert list(X.columns)==FEATURES and y.tolist()==[0,1]
