import os
basedir = 'C:\\Users\\andre.ribeiro\\Desktop\\script\\New folder'
for fn in os.listdir(basedir):
  print('e')
  if not os.path.isdir(os.path.join(basedir, fn)):
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
 
  os.rename(os.path.join(basedir, fn),
            os.path.join(basedir, firstname))
  
print('h')