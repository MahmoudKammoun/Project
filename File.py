def create_file(name,cl):
    n=str(name)+".py"
    zz=open(n,'w')
    zz.write("import subprocess"+"\n")
    zz.write("print(str(subprocess.check_output(["+"'"+cl+"'"+"],shell=True)))")
    return()

create_file("nono" , "ls")
