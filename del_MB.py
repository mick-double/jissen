# csvファイルを読み込んで指定文字列を削除してファイルを出力する
# 最初は固定ファイル名で

with open('memory.csv','r') as in_f :
    with open('D_memory.csv','w') as out_f:
        count = 0
        ocount = 0
        # test[]=''
        l = in_f.readlines()
        for i in range(len(l)):
            # print(l[i])
            str01 = l[i].replace(" MB","")
            print(str01)
            out_f.write(str01)

