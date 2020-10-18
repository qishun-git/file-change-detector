import yaml
import logging
from detect import Detector


config_dir = './'
# Load configuration.
config_file_path = config_dir + 'config.yml'
config = yaml.safe_load(open(config_file_path, 'r'))

# start_detect(config)

if __name__ == "__main__":
    print("====================================FCD Started====================================")
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='logs.log', level=logging.DEBUG, format=LOG_FORMAT)
    detector = Detector(config)
    detector.start_detect()