import os
#print(dir(os))
import subprocess

a=os.system("uname -r")
#b=os.system("grep -E '^(VERSION|NAME)=' /etc/os-release")
#print("coco"+str(a))
#print(type(a))
#os.chdir("//home/mahmoud")

#print(os.getcwd())
#print(type(os.getcwd()))

#print(os.listdir())
c=subprocess.check_output(["grep -E '^(VERSION|NAME)=' /etc/os-release"],shell=True)
#print(type(c).decode("utf-8"))
print(c)

encoding = 'utf-8'




#print(str(c,'utf-8'))

