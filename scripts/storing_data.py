import pandas as pd
import math
from typing import Tuple


def create_df(columns: list, output: str, ulog: str, filename: str) -> pd.DataFrame:
    cvs_name = f'./resources/{output}/{ulog}_{filename}_0.csv'
    return pd.read_csv(cvs_name, usecols=columns).dropna()


def convert_quaternion_to_rpy(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for i in range(df.count().timestamp):
        x, y, z = euler_from_quaternion(df.iloc[i]['q[0]'], df.iloc[i]['q[1]'], df.iloc[i]['q[2]'], df.iloc[i]['q[3]'])
        rows.append([df.iloc[i]['timestamp'], x, y, z])
    return pd.DataFrame(rows, columns=['timestamp', 'roll_body', 'pitch_body', 'yaw_body'])


def euler_from_quaternion(x: float, y: float, z: float, w: float) -> Tuple[float, float, float]:
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)
    return roll_x, pitch_y, yaw_z  # in radians
