import re
from os.path import isdir
from utils.yaml_methods import write_yaml_file,read_yaml_file
from utils.name_path_converter import name_path_converter
import fire
import os
from config import ROOT_PATH, EDITOR_TOOL

# 新建一个章节
def nc(chapter_en):
    # 根据传入的章节名，生成对应的信息
    new_chapter = name_path_converter('chapter', name_en=chapter_en)
    new_chapter_name = new_chapter['chapter_folder_name']
    new_chapter_path = new_chapter['chapter_folder_path']
    note_folder_path = new_chapter['note_folder_path']
    if not os.path.exists(note_folder_path):
        print("Error: 当前没有指定正确的笔记本，请使用-nt 命令新建一个笔记本")
        return

    # 生成章节文件夹
    try:
        os.mkdir(new_chapter_path)
    except IOError:
        print("Warning: 该章节文件夹已经存在")
        # return
    else:
        print('新建一个章节文件夹： {name}'.format(name=new_chapter_name))

    # ----------Begin-----------
    # ------新建章节.tex文件------
    # --------------------------

    # 获得章节信息
    new_chapter_file_path = new_chapter_path + '/' + new_chapter_name + '.tex'

    # 保护原有不被重写
    if os.path.exists(new_chapter_file_path):
        print("Warning: 已经存在该章节.tex文件")
        return

    # 写入
    chapter_tex_file = open(new_chapter_file_path, 'w')
    chapter_tex_file.write('\\chapter{}\n')
    chapter_tex_file.close()

    # --------------------------
    # ------新建章节.tex文件------
    # -----------end------------

    # 打开新建章节.tex文件
    os.system(EDITOR_TOOL + ' ' + new_chapter_file_path)

    # 把新建的章节写入info.yaml文件夹
    note_info_file_path = note_folder_path + '/info.yaml'
    contents = read_yaml_file(note_info_file_path)
    new_chapter = {
        'chapter_name_en': chapter_en,
    }
    contents['chapter_list'].append(new_chapter)
    write_yaml_file(note_info_file_path,contents)


# 新建一个笔记本文件
def nt(name_en):
    # 显示所有的非隐藏的文件夹 方法1
    for item in os.listdir(ROOT_PATH):
        if isdir(ROOT_PATH + '/' + item) and not item.startswith('.'):
            pass

    # 根据传入的笔记英文名，获得笔记的正确文件夹名与文件路径
    new_folder = name_path_converter('note', name_en=name_en)
    new_folder_path = new_folder['note_folder_path']
    new_folder_name = new_folder['note_folder_name']
    type_in_note_name = new_folder['type_in_note_name']

    # 生成笔记文件夹
    try:
        os.mkdir(new_folder_path)
    except IOError:
        print("Error: note笔记已经存在")
        return
    else:
        print('新建一个文件夹成功： {name}'.format(name=new_folder_name))
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

    # 新建info.yaml文件
    note_name_en = re.sub("[A-Z]", lambda x: " " + x.group(0), new_folder_name).strip()
    contents = {
        'note_name_en': note_name_en,
        'chapter_list': [],
    }
    note_yaml_path = new_folder_path + '/' + "info.yaml"
    write_yaml_file(note_yaml_path, contents)

    # 新建main.tex文件
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
    # 打开main.tex文件
    # os.system(EDITOR_TOOL + ' ' + new_folder_path + '/src/main/main.tex')

    # 把新建的笔记本写入info.yaml文件夹
    notes_info_file_path = ROOT_PATH + '/info.yaml'
    contents = read_yaml_file(notes_info_file_path)
    new_note = {
        'note_name_en': type_in_note_name,
    }
    contents['notes_list'].append(new_note)
    write_yaml_file(notes_info_file_path, contents)


if __name__ == '__main__':
    fire.Fire()
