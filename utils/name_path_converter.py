from config import ROOT_PATH,CURRENT_NOTE_NAME


def name_path_converter(option=None, name_en=None, name_path=None):
    if option == 'note':
        note_folder_name = name_en.title().replace(" ", "")
        type_in_note_name = name_en.title().strip()
        note_folder_path = ROOT_PATH + '/' + note_folder_name
        note_info = {
            'type_in_note_name': type_in_note_name,
            'note_folder_name': note_folder_name,
            'note_folder_path': note_folder_path
        }
        return note_info

    if option == 'chapter':
        note_folder_name = CURRENT_NOTE_NAME.title().replace(" ", "")
        note_folder_path = ROOT_PATH + '/' + note_folder_name

        chapter_folder_name = name_en.strip().lower().replace(" ", "_")
        chapter_folder_path = note_folder_path + '/src/chapters/' + chapter_folder_name

        note_info = {
            'type_in_chapter_name': name_en,
            'note_folder_name': note_folder_name,
            'note_folder_path': note_folder_path,
            'chapter_folder_name': chapter_folder_name,
            'chapter_folder_path': chapter_folder_path
        }
        return note_info
