import argparse
import csv

from serial import Serial
from datetime import datetime

file_name = datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'

parser = argparse.ArgumentParser(
    description='Log Serial Output', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', '--port_device',
                    help='Port where device is connected', default='COM1')
parser.add_argument('-b', '--baudrate',
                    help='Device baudrate in bps', default=9600, type=int)
parser.add_argument(
    '-n', '--name', help='Files Output name (default is dynamic)', default=file_name)
parser.add_argument(
    '-s', '--sep', help='String separator coming from serial', default=';')
args = parser.parse_args()

port = args.port_device
baudrate = args.baudrate
file_name = args.name
sep = args.sep

serial = Serial(port, baudrate)
serial.flushInput()

print(
    f'Starting logger on port {port} with baudrate {baudrate}...Saving on {file_name}!')

while True:
    try:
        bytes = serial.readline()
        decoded = bytes[0:len(bytes)-2].decode('utf-8').split(sep)

        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(decoded)
    except:
        serial.close()
        print('Adios!')
        break
