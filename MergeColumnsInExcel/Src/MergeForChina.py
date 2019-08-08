from NewExcels.NewExcelsPath import new_excels_path
from OldExcels.OldExcelsPath import old_excels_path
import pandas as pd


if __name__ == '__main__':
    data = pd.read_excel(old_excels_path + 'Id_China.xlsx', sheet_name=0, usecols=[0, 1, 2, 3],
                         dtype=str, index_col=None,)
    # print(data)
    s0 = data['NTLC']
    s1 = data['CHAPTER']
    s2 = data['NTLC_NAME']
    s3 = data['REV_CD']

    s_interchange = list()
    str1 = ''
    for i in range(len(s1)):

        str1 = ''
        str1 += s1[i]
        str1 += s2[i]
        s_interchange.append(str1)
    s_merge = pd.Series(s_interchange)
    d = {
        'NTLC': s0,
        'NTLC_NAME': s_merge,
        'REV_CD': s3
         }
    df = pd.DataFrame(d)

    df.to_excel(new_excels_path + 'Id_China.xlsx')

