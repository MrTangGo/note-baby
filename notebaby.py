import re
from os.path import isdir
from yaml_methods import write_yaml_file

import fire
import os
from config import ROOT_PATH


def nt(name_cn):
    # 显示所有的非隐藏的文件夹 方法1
    for item in os.listdir(ROOT_PATH):
        if isdir(ROOT_PATH + '/' + item) and not item.startswith('.'):
            pass

    # 根据传入的文件名，新建一个文件夹
    new_folder_name = name_cn.title().replace(" ", "")
    new_folder_path = ROOT_PATH + '/' + new_folder_name
    try:
        os.mkdir(new_folder_path)
    except IOError:
        print("Error: note文件已经存在")
    else:
        print('新建一个文件夹成功： {name}'.format(name=new_folder_name))

    # 在新建的文件中，建立配置文件
    note_name_en = re.sub("[A-Z]", lambda x: " " + x.group(0), new_folder_name).strip()
    contents = {'note_name_en': note_name_en}
    note_yaml_path = new_folder_path + '/' + "info.yaml"
    write_yaml_file(note_yaml_path, contents)

    # 建立src\img\config\chapters文件夹
    try:
        os.mkdir(new_folder_path + '/' + "src")
    except IOError:
        print("Error: src文件已经存在")
    else:
        print('新建src文件夹成功')

    try:
        os.mkdir(new_folder_path + '/src/' + "config")
    except IOError:
        print("Error: config文件已经存在")
    else:
        print('新建config文件夹成功')

    try:
        os.mkdir(new_folder_path + '/src/' + "img")
    except IOError:
        print("Error: img文件已经存在")
    else:
        print('新建img文件夹成功')

    try:
        os.mkdir(new_folder_path + '/src/' + "chapters")
    except IOError:
        print("Error: chapters文件已经存在")
    else:
        print('新建chapters文件夹成功')

    try:
        os.mkdir(new_folder_path + '/src/' + "main")
    except IOError:
        print("Error: main文件已经存在")
    else:
        print('新建main文件夹成功')

    # 新建一个main.tex 文件并打开
    main_tex_file = open(new_folder_path + '/src/main/main.tex', 'w')
    main_tex_file.write('\\documentclass[UTF8,a4paper]{ctexbook}\n'
                        '\n'
                        '\\input{../config/preamble.tex}\n'
                        '\n'
                        '\\begin{document}\n'
                        '\n'
                        '% start cover\n'
                        '% end cover\n'
                        '\n'
                        '% start catalog\n'
                        '% end catalog\n'
                        '\n'
                        '% start chapter\n'
                        '% end chapter\n'
                        '\n'
                        '% start working\n'
                        '% end working\n'
                        '\n'
                        '\\end{document}'
                        )
    main_tex_file.close()

    os.system('mvim '+new_folder_path+'/src/main/main.tex')


if __name__ == '__main__':
    fire.Fire()
