from storing_data import create_df, convert_quaternion_to_rpy
from analysis import Analyzer
from parsing import convert_ulg_to_csv
from error_value import calculate_error_value


class DataFrames:
    def __init__(self, ulog_file: str):
        convert_ulg_to_csv(ulog_file, ','.join(messages), output_directory, csv_delimiter)
        cols = ['timestamp', 'x', 'y', 'z', 'vx', 'vy', 'vz', 'ax', 'ay', 'az']
        self.localization_df = create_df(cols, output_directory, ulog_file, messages[0])

        cols = ['timestamp', 'x', 'y', 'z', 'vx', 'vy', 'vz', 'acceleration[0]', 'acceleration[1]', 'acceleration[2]']
        self.localization_set_point_df = create_df(cols, output_directory, ulog_file, messages[1])

        cols = ['timestamp', 'q[0]', 'q[1]', 'q[2]', 'q[3]']
        quaternion_orientation_df = create_df(cols, output_directory, ulog_file, messages[2])
        self.orientation_df = convert_quaternion_to_rpy(quaternion_orientation_df)

        cols = ['timestamp', 'roll_body', 'pitch_body', 'yaw_body']
        self.orientation_set_point_df = create_df(cols, output_directory, ulog_file, messages[3])


if __name__ == '__main__':
    messages = ['vehicle_local_position',
                'vehicle_local_position_setpoint',
                'vehicle_attitude',
                'vehicle_attitude_setpoint']
    output_directory = 'csv_files'
    csv_delimiter = ','

    log_1 = DataFrames('log-1')
    log_2 = DataFrames('log-2')

    analysis = Analyzer()
    analysis.add_scatter(log_1.localization_df, 'log_1 trajectory')
    analysis.add_scatter(log_1.localization_set_point_df, 'log_1 trajectory setpoint')
    analysis.add_scatter(log_2.localization_df, 'log_2 trajectory')
    analysis.add_scatter(log_2.localization_set_point_df, 'log_2 trajectory setpoint')
    analysis.show()

    iae_1 = calculate_error_value(log_1.localization_df, log_2.localization_df)
    iae_2 = calculate_error_value(log_1.localization_df, log_1.localization_set_point_df)
    iae_3 = calculate_error_value(log_2.localization_df, log_2.localization_set_point_df)

