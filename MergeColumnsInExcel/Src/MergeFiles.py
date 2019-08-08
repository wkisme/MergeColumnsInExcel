from os import listdir
from os.path import isfile, join
from FilePath.FilePath import chapter_file_path
from FilePath.FilePath import old_excels_path
from FilePath.FilePath import new_excels_path
import os
import pandas as pd


if __name__ == '__main__':
    chapter_info = pd.read_excel(chapter_file_path + 'Chapter+List.xlsx', sheet_name=0, usecols=[0, 1],
                                 dtype=str, index_col=None,)
    chapter_nums = chapter_info['Chapter ']
    description = chapter_info['Description']
    # print(chapter, description)
    only_files = [f for f in listdir(old_excels_path) if isfile(join(old_excels_path, f))]
    counter = 0

    for i in only_files:
        data = pd.read_excel(old_excels_path + i, sheet_name=0, usecols=[0, 1, 2],
                             dtype=str, index_col=None, header=4)
        s0 = data['NTLC']
        s1 = data['NTLC_NAME']
        s2 = data['REV_CD']
        str1 = ''
        for j in range(len(s0)):
            str1 = ''
            str1 += s0[j][0]
            str1 += s0[j][1]
            for chapter_counter in range(len(chapter_nums)):
                if str1 in chapter_nums[chapter_counter]:
                    if isinstance(description[chapter_counter], str):
                        if isinstance(s1[j], str):
                            s1[j] = description[chapter_counter] + s1[j]
                            break
                        else:
                            print('国家', i)
                            print('列表顺序', j)
                            print('章节', chapter_counter + 1)
                            break
        d = {
            'NTLC': s0,
            'NTLC_NAME': s1,
            'REV_CD': s2
        }
        df = pd.DataFrame(d)

        df.to_excel(new_excels_path + i)

        counter += 1




