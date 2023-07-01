import actions as action
import menu


def run():
    input_from_user = ''
    while input_from_user != '7':
        menu.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            action.show('all')
        if input_from_user == '2':
            action.add()
        if input_from_user == '3':
            action.show('all')
            action.id_edit_del_show('del')
        if input_from_user == '4':
            action.show('all')
            action.id_edit_del_show('edit')
        if input_from_user == '5':
            action.show('date')
        if input_from_user == '6':
            action.show('id')
            action.id_edit_del_show('show')
        if input_from_user == '7':
            print("Программа завершена")
            break