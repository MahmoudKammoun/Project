import subprocess
def actionn(x,y):
    if x==1 :
        subprocess.check_output(["sudo mkdir "+y],shell=True)
        print(y+" created ")
    elif x==2 :
        subprocess.check_output(["sudo rmdir "+y],shell=True)
        print(y +"dealeted")
    elif x==3:
        print(str(subprocess.check_output(["du -sh "+y],shell=True)))
    elif x==4:
        print(str(subprocess.check_output(["du -sh "+y],shell=True)))

