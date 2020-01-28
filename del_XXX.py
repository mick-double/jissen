# csvファイルを読み込んで指定文字列を削除してファイルを出力する
# 進歩してコマンドライン指定できるようにした

import sys

in_fname = sys.argv[1]
with open(in_fname,'r') as in_f :
    out_fname = in_fname + '.txt'
    with open(out_fname,'w') as out_f:
        count = 0
        ocount = 0
        # test[]=''
        l = in_f.readlines()
        for i in range(len(l)):
            # print(l[i])
            d_st = sys.argv[2]
            str01 = l[i].replace(d_st,"")
            print(str01)
            out_f.write(str01)

