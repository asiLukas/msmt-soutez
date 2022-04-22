from os import listdir, walk
from os.path import isfile, join
from glob import glob
import unidecode # WARNING: pip install Unidecode

files_dict = dict()
def autoradio(files, desired_dir):
    # pokud jeste nejsem u korenove slozky, pokracuju v rekurzi
    if desired_dir in files[0]:
        for i in range(len(files)):
            # ziska posledni konecny soubor/slozku v adresari
            last_file = files[i][files[i].rfind("\\")+1: ]
            result_file = unidecode.unidecode(last_file)

            # kvuli duplikatum prirazuji do hashmapy cestu jako klic a hodnotu jako pozadovanou zmenu nazvu
            files_dict[files[i]] = result_file

            # po vypsani, zapsani hodnot do hashmapy mazu posledni soubor/slozku v ceste vymazat
            files[i] = files[i].replace('\\' + last_file, '')
        try:
            autoradio(files, desired_dir)
        except RecursionError:
            print('please, remove the last backslash')
            quit()
    else:
        # osetreni toho, ze i pres ten if to probehne jeste jednou, takze to proste odstranim
        files_dict.pop(files[0])

if __name__ == '__main__':
    path = input('Zadej absolutni cestu ke slozce: ')
    # ziskam jmeno slozky, ve ktere chce uzivatel pracovat
    des_dir = path[path.rfind('\\')+1: ]

    # vybere vsechny soubory i z podslozek v danem adresari
    files = [y for x in walk(path) for y in glob(join(x[0], '*.*'))]

    autoradio(files, des_dir)

    for k, v in files_dict.items():
        print(f'{k} -> {v}')
