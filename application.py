import yaml
from detect import Detector


config_dir = './'
# Load configuration.
config_file_path = config_dir + 'config.yml'
config = yaml.safe_load(open(config_file_path, 'r'))

# start_detect(config)

if __name__ == "__main__":
    print("====================================FCD Started====================================")
    detector = Detector(config)
    detector.start_detect()