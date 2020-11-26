f_in = open("rockyou.txt","r")
flines = f_in.readlines()

for i in range(1,287): # 286 characters is the longest password in rockyou.txt
    f_out = open("rockyou-split-length-"+str(i-1)+".txt","a")

    for fline in flines:
        if len(fline) == i:
            f_out.write(fline)
    
    f_out.close()

f_in.close()
print ("DONE")