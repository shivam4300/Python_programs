#/usr/bin/python3
import os 
import glob
p=os.getcwd()
print(p)
data=os.listdir(p)
print(data)
for f in data:
    file_path=os.path.join(p,f)
    backup_fp=os.path.join(p,'backup')
    if os.path.isfile(file_path) and f.endswith(".txt"):
#read the source file 
        with open(file_path,'r+') as src:
                x=src.read()
                print(x)
#write the content of the source file in backup files                
        backup=os.path.join(backup_fp,f)
        with open (backup,"a+") as des:
            y=des.write(x)
            print(y)
#truncate the data from the source file
        with open (file_path,'w') as src:
            src.truncate(0)

