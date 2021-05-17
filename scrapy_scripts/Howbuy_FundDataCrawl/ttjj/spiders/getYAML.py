import yaml
import os

def getyaml(filename):
    yamlPath = 'yaml\\' + str(filename) + ".yaml"
    print(yamlPath)
    file = open(yamlPath, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    yaml_data = yaml.full_load(file_data)
    return yaml_data

def getyaml_Specifyname(filename):
    p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")) # 得到上4级的目录
    # print('p:'+ str(p))
    yamlPath = p + '\\yaml\\' + str(filename) + ".yaml"
    # yamlPath = 'yaml\\' + str(filename) + ".yaml"
    print(yamlPath)
    file = open(yamlPath, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    yaml_data = yaml.full_load(file_data)
    return yaml_data
    