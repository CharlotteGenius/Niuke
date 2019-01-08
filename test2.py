

files = {}
name_rows = []
try:
    while True:
        string = input().strip().split()
        if string == '':
            break
        print(string)
        direc = string[0]
        name = direc.split('\\')[-1][-16:]
        row = str(string[-1])
        name_row = name+' '+row
        if name_row not in files.keys():
            name_rows.append(name_row)
            files[name_row]=1
        else:
            files[name_row] = files[name_row]+1
        for item in name_rows[-8:]:
            print(item,str(files[name_row]),sep=' ')
except:
    pass
