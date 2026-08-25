f = open("f2.txt",mode="w")
f.write("Hello this is python session")
f.write("\ndevops sir how are you")

l = [f"This is line {i}\n" for i in range(50)]
f.writelines(l)
f.close()	

#f3 = open("f1.txt","w")

with open("f1.txt","r") as f1, open("f3.txt","w") as f2:
    #print(f1.readlines())
    f2.writelines(f1.readlines())
