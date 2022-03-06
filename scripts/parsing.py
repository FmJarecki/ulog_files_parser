from pyulog import ulog2csv
from os import path, mkdir


class UlgNotFound(Exception):
    def __init__(self, message: str = 'File not found. Check if the file is in the resources directory'):
        self.message = message
        super().__init__(self.message)


def convert_ulg_to_csv(ulog: str, msgs: str, output: str, delimiter: chr):
    ulog = f'../resources/{ulog}.ulg'
    output = f'../resources/{output}'
    if not path.exists(ulog):
        raise UlgNotFound()
    if not path.exists(output):
        mkdir(output)
    ulog2csv.convert_ulog2csv(ulog, msgs, output, delimiter)
