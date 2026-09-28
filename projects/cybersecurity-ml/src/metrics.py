import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, average_precision_score, confusion_matrix

def evaluate_binary(y_true, y_pred, y_score=None):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0,1]).ravel()
    out = {
      'precision': precision_score(y_true,y_pred,zero_division=0),
      'recall': recall_score(y_true,y_pred,zero_division=0),
      'f1': f1_score(y_true,y_pred,zero_division=0),
      'false_positive_rate': fp/(fp+tn) if fp+tn else 0.0,
      'alerts_per_1000': float(np.mean(y_pred)*1000)
    }
    if y_score is not None:
        out['roc_auc']=roc_auc_score(y_true,y_score)
        out['pr_auc']=average_precision_score(y_true,y_score)
    else:
        out['roc_auc']=np.nan; out['pr_auc']=np.nan
    return out
