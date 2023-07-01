import file_operations
import Note



def add():
    note = create_note
    array = file_operations.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operations.write_file(array, 'a')
    print('Заметка создана')


def show(text):
    logic = True
    array = file_operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.view_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.view_note(notes))
    if logic == True:
        print('Заметки отсутствуют')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operations.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = create_note
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operations.write_file(array, 'a')




def create_note():
    title = input('Введите Название заметки: ')
    body =  input('Введите Описание заметки: ')
    return Note.Note(title=title, body=body)