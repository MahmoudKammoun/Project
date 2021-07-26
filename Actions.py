import subprocess
def create (x) :
    subprocess.check_output(["sudo mkdir "+x],shell=True)
    return
def delete (x) :
    subprocess.check_output(["sudo rmdir "+x],shell=True)
    return
def size (x):
    print(subprocess.check_output(["du -sh "+x],shell=True))
    return
def subfolders (x):
    print(subprocess.check_output(["du -h "+x],shell=True))
    return
a=size("/home/mahmoud/Documents/")

#print(str(c,'utf-8'))
print(str(size("/home/mahmoud/Documents/")))
print(a)
#subfolders("/home/mahmoud/Documents/")
print(type(str(size("/home/mahmoud/Documents/"))))
