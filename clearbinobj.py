import shutil, os


for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for dirname in dirnames:
        if dirname in ('bin', 'obj'):
            shutil.rmtree(dirpath + r'\\' + dirname)

print("Bin and obj were cleared")