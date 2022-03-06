from scipy.spatial import distance
import pandas as pd


def calculate_error_value(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    if df1.count().timestamp < df2.count().timestamp:
        num_of_rows = df1.count().timestamp
    else:
        num_of_rows = df2.count().timestamp
    rows = []
    for i in range(num_of_rows):
        x1, y1, z1 = df1.iloc[i]['x'], df1.iloc[i]['y'], df1.iloc[i]['z']
        x2, y2, z2 = df2.iloc[i]['x'], df2.iloc[i]['y'], df2.iloc[i]['z']
        dst = distance.euclidean((x1, y1, z1), (x2, y2, z2))
        rows.append([df1.iloc[i]['timestamp'], df2.iloc[i]['timestamp'], dst])
    return pd.DataFrame(rows, columns=['timestamp_1', 'timestamp_2', 'euclidian_distance'])


