import yaml


def write_yaml_file(yaml_file_path, contents):
    file = open(yaml_file_path, 'w', encoding='utf-8')
    yaml.dump(contents, file, allow_unicode=True, sort_keys=False)
    file.close()


def read_yaml_file(yaml_file_path):
    file = open(yaml_file_path, 'r', encoding='utf-8')
    contents = yaml.load(file.read(), Loader=yaml.FullLoader)
    return contents
