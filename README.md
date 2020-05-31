# seriuslogger
A simple code to log data from Serial Port

This script logs data coming from a Serial Port (like COM1 or /dev/ttyUSB0) in a CSV file. 

Seriuslogger expects arrays of bytes, where every recognized '\n' is considered a new line in the CSV file, categorizing a Row. A row can also have an array of content. This inner array will be the CSV columns, and they are recognized by a separator coming from the serial data, as default ';'. 

For the sake of example, the following data coming from the serial port:

>"time;q_1;q_2\n1001;10.2;0.0\n1002;10.7;0.3\n"

Or in a more expressive form:

"time;q_1;q_2\n"

"1001;10.2;0.0\n"

"1002;10.7;0.3\n"

Will be interpreted by Seriuslogger and saved in the CSV as:

| time |  q_1  | q_2 |
|:----:|:----:|:---:|
| 1001 | 10.2 |  0.0 |
| 1002 | 10.7 |  0.3 |

# Usage
## First Steps
(Optional) Create a virtualenv, by your preference, and jump to it.

Install all dependencies using the following command

> pip install -r requirements.txt

Python version 3.7.7

## Firing up

Simple run

> py serius_logger.py [-h] [-p PORT_DEVICE] [-b BAUDRATE] [-n NAME] [-s SEP]

## Arguments
For help on-the-go, simple use

> py seriuslogger.py -h

-  -h, --help            show this help message and exit
-  -p PORT_DEVICE, --port_device PORT_DEVICE
                        Port where device is connected (default: COM1)
-  -b BAUDRATE, --baudrate BAUDRATE
                        Device baudrate in bps (default: 9600)
-  -n NAME, --name NAME  Files Output name (default is dynamic) (default:
                        YYmmddHHMMSS.csv)
-  -s SEP, --sep SEP     String separator coming from serial (default: ;)
