from FilePath.FilePath import old_excels_path
from os import listdir
from os.path import isfile, join
import os
import pandas as pd
from FilePath.FilePath import project_path

if __name__ == '__main__':
    only_files = [f for f in listdir(old_excels_path) if isfile(join(old_excels_path, f))]
    dst = ''
    print(len(only_files))
    d = {
        'CountryName': only_files
    }
    df = pd.DataFrame(d)

    df.to_excel(project_path + 'CountryName.xlsx')
    # for i in only_files:
    #     dst = ''
    #     for j in i:
    #         if j.isalpha():
    #             dst += j
    #         elif j == ' ':
    #             dst += ' '
    #         else:
    #             break
    #     if os.path.exists(old_excels_path + 'Id_' + dst + '.xlsx'):
    #         print(dst)
    #
    #     os.rename(old_excels_path + i, old_excels_path + dst + '_International' + '.xlsx')
