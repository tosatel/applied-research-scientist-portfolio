FEATURES = ['failed_logins','connection_count','unique_destinations','bytes_mb','session_minutes','off_hours','privileged_action','baseline_deviation']

def split_xy(df):
    return df[FEATURES].copy(), df['label'].astype(int).copy()
