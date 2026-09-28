from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def build_models(seed=42, contamination=0.14):
    return {
      'Logistic Regression': make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, class_weight='balanced', random_state=seed)),
      'Random Forest': RandomForestClassifier(n_estimators=250, class_weight='balanced', random_state=seed, min_samples_leaf=2),
      'Isolation Forest': IsolationForest(n_estimators=250, contamination=contamination, random_state=seed)
    }
