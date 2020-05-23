from utils.yaml_methods import *


class Note:
    """所有笔记本基类"""

    def __init__(self, path):
        contents = read_yaml_file(path + '/info.yaml')
        note_info = contents
        note_info.setdefault('current_chapter', [])
        self.chapters_list = note_info['chapters_list']
        self.note_name_en = note_info['note_name_en']
        self.note_name_cn = note_info['note_name_cn']
        self.current_chapter = note_info['current_chapter']

    def print_chapters_list(self):
        for index, item in enumerate(self.chapters_list):
            item.setdefault('chapter_name_cn', 'Warning:没有设置中文名')
            try:
                print(index + 1, '-', item['chapter_name_en'], '-', item['chapter_name_cn'])
            except KeyError:
                print("KeyError：没有合适的找到Key")

    def get_chapters_list(self):
        chapters_list = []
        for index, item in enumerate(self.chapters_list):
            item.setdefault('chapter_name_cn', 'Warning:没有设置中文名')
            item_message = str(index + 1) + "-" + "chapter:" + item['chapter_name_en'] + "-" + item['chapter_name_cn']
            try:
                chapters_list.append(item_message)
            except KeyError:
                print("KeyError：没有合适的找到Key")
        return chapters_list


class Notes:
    """所有笔记本包基类"""

    def __init__(self, path):
        contents = read_yaml_file(path + '/info.yaml')
        notes_info = contents
        self.notes_list = notes_info['notes_list']
        self.notes_name_en = notes_info['notes_name_en']
        self.notes_name_cn = notes_info['notes_name_cn']
        self.current_note = notes_info['current_note']

    def print_notes_list(self):
        for index, item in enumerate(self.notes_list):
            item.setdefault('note_name_cn', 'Warning:没有设置中文名')
            try:
                print(index + 1, '-', item['note_name_en'], '-', item['note_name_cn'])
            except KeyError:
                print("KeyError：没有合适的找到Key")

    def get_notes_list(self):
        notes_list = []
        for index, item in enumerate(self.notes_list):
            item.setdefault('note_name_cn', '!Warning:没有设置中文名，请马上设置')
            item_message = str(index + 1) + "-《" + item['note_name_en'] + "》" + item['note_name_cn']
            try:
                notes_list.append(item_message)
            except KeyError:
                print("KeyError：没有合适的找到Key")
        return notes_list
