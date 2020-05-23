import yaml

def write_yaml_file(yaml_file_path, contents):
    file = open(yaml_file_path, 'w', encoding='utf-8')
    yaml.dump(contents, file)
    file.close()

