import view
import import_info
import data_mod

# Основной модуль


def mainFunction():
    a = view.choise()
    if a[1] == 1:
        import_info.create_data(a[0])
    elif a[1] == 2:
        view.res_find(data_mod.get_data(a[0]))
