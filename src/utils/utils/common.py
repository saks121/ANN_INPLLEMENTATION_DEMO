from src.utils.utils import yaml
def read_config(config_path):
    with open(config_path) as confiig_file:
        content =yaml.safe_load(confiig_file)

    return content 