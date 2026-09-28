import pandas as pd

def feature_importance(model_name, model, feature_names):
    if model_name == 'Logistic Regression':
        values = model.named_steps['logisticregression'].coef_[0]
    elif model_name == 'Random Forest':
        values = model.feature_importances_
    else:
        return pd.DataFrame(columns=['model','feature','importance'])
    return pd.DataFrame({'model':model_name,'feature':feature_names,'importance':values})
