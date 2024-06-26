import os
basedir = 'C:\\Users\\andre.ribeiro\\Desktop\\script\\New folder'
for fr in os.listdir(basedir):
    basedirs=os.path.join(basedir, fr)
    for fn in os.listdir(basedirs):
        print('e')
        if not os.path.isfile(os.path.join(basedirs, fn)):
            print('a')
            continue # Not a directory
        if ',' in fn:
            print('b')
            continue # Already in the correct form
        if ' ' not in fn:
            print('c')
            continue # Invalid format
        if '_' not in fn:
            print('i')
            continue # Invalid format
        print('d')
        firstname,_,surname = fn.rpartition('_')
        sur,_,ext=surname.rpartition('.')
        os.rename(os.path.join(basedirs, fn),
                    os.path.join(basedirs, firstname+'.'+ext))
    
print('h')