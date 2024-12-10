import argparse
import configparser
import os

# main.py --templatenumber "33-1" --startdate "2024-09-03T12:00:00.000" --enddate "2024-09-03T12:02:00.000"

# get parent directory
parentDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))

parser = argparse.ArgumentParser()
parser.add_argument('--templatenumber',help='Template Number e.g 33-1' , required=True)
parser.add_argument('--startdate', help='Date format : yyyy-MM-ddThh:mm:ss.SSS', required=True)
parser.add_argument('--enddate', help='Date format : yyyy-MM-ddThh:mm:ss.SSS', required=True)
args = parser.parse_args()

templateNumber = args.templatenumber
starDate = args.startdate
endDate = args.enddate

# read config.ini
config = configparser.ConfigParser()
config.read('config.ini')

if __name__=="__main__":
    hexSource = config['hex_source'][templateNumber]
    
    ## Debuging ##
    # stringSource = ''.join([chr(int(hexSource[i:i+2], 16)) for i in range(0, len(hexSource), 2)])
    # print(stringSource)

    stringReplacer = '"startTime":"'+starDate+'+00:00","endTime":"'+endDate+'+00:00"'
    hexReplacer = stringReplacer.encode().hex()

    with open(templateNumber+'-source.mp4', 'rb') as f:
        content = f.read().hex()
    
    content = content.replace(hexSource, hexReplacer)
    with open(templateNumber+'-original.mp4', 'wb') as f:
        f.write(bytes.fromhex(content))

    with open(templateNumber+'-original.mp4', 'rb') as f:
        new_content = f.read().hex()