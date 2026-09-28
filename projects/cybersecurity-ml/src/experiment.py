import argparse, os, sys, pandas as pd
from sklearn.model_selection import train_test_split
sys.path.insert(0, os.path.dirname(__file__))
from preprocessing import split_xy, FEATURES
from models import build_models
from metrics import evaluate_binary
from explainability import feature_importance

def run(data_path, output_path):
    df=pd.read_csv(data_path); X,y=split_xy(df)
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.30,stratify=y,random_state=42)
    models=build_models(contamination=max(.01,min(.49,float(ytr.mean())))); rows=[]; imps=[]
    for name,m in models.items():
        if name=='Isolation Forest':
            m.fit(Xtr[ytr==0]); score=-m.decision_function(Xte); pred=(m.predict(Xte)==-1).astype(int)
        else:
            m.fit(Xtr,ytr); score=m.predict_proba(Xte)[:,1]; pred=m.predict(Xte)
            imps.append(feature_importance(name,m,FEATURES))
        rows.append({'model':name,**evaluate_binary(yte,pred,score)})
    out=pd.DataFrame(rows); os.makedirs(os.path.dirname(output_path),exist_ok=True); out.to_csv(output_path,index=False)
    pd.concat(imps,ignore_index=True).to_csv(os.path.join(os.path.dirname(output_path),'feature_importance.csv'),index=False)
    print(out.round(4).to_string(index=False)); return out
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--data',required=True); p.add_argument('--output',required=True); a=p.parse_args(); run(a.data,a.output)
