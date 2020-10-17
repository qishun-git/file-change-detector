import yaml
from detect import start_detect


config_dir = './'
# Load configuration.
config_file_path = config_dir + 'config.yml'
config = yaml.safe_load(open(config_file_path, 'r'))

if __name__ == "__main__":
    start_detect(config)