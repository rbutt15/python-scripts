filename=input("What do you want your file to be called?")
myfile=open(filename+".txt","w")
content=input("What do you want the contents to be?")
myfile.write(content)
myfile.close()
viewtf=input("The file has been saved and closed. Would you like to view it? (if yes please type YES)")
if viewtf == "YES" :
 myfile=open(filename+".txt","r")
 readcontent=myfile.read()
 print(readcontent)
 myfile.close()

    
