print("Welcome to Holiday Planner")
destination=input("Where are you going?")
myfile=open("holiday.txt","w")
myfile.write("Destination: "+destination+"\n")
print("You can add 10 items to your packing checklist")
pack1=input("What's your first item?")
pack2=input("What's your next item?(press enter to leave blank)")
pack3=input("What's your next item?(press enter to leave blank)")
pack4=input("What's your next item?(press enter to leave blank)")
pack5=input("What's your next item?(press enter to leave blank)")
pack6=input("What's your next item?(press enter to leave blank)")
pack7=input("What's your next item?(press enter to leave blank)")
pack8=input("What's your next item?(press enter to leave blank)")
pack9=input("What's your next item?(press enter to leave blank)")
pack10=input("What's your next item?(press enter to leave blank)")
myfile.write("Here's what to pack:"+"\n")
myfile.write("1."+pack1+"\n")
myfile.write("2."+pack2+"\n")
myfile.write("3."+pack3+"\n")
myfile.write("4."+pack4+"\n")
myfile.write("5."+pack5+"\n")
myfile.write("6."+pack6+"\n")
myfile.write("7."+pack7+"\n")
myfile.write("8."+pack8+"\n")
myfile.write("9."+pack9+"\n")
myfile.write("10."+pack10+"\n")
print("Here's your list:")
print(pack1)
print(pack2)
print(pack3)
print(pack4)
print(pack5)
print(pack6)
print(pack7)
print(pack8)
print(pack9)
print(pack10)
print("You will now be able to add preperation tasks to a seprate list")
prep1=input("What's your first item?")
prep2=input("What's your next item?(press enter to leave blank)")
prep3=input("What's your next item?(press enter to leave blank)")
prep4=input("What's your next item?(press enter to leave blank)")
prep5=input("What's your next item?(press enter to leave blank)")
prep6=input("What's your next item?(press enter to leave blank)")
prep7=input("What's your next item?(press enter to leave blank)")
prep8=input("What's your next item?(press enter to leave blank)")
prep9=input("What's your next item?(press enter to leave blank)")
prep10=input("What's your next item?(press enter to leave blank)")
myfile.write("Here's what to prep:"+"\n")
myfile.write("1."+prep1+"\n")
myfile.write("2."+prep2+"\n")
myfile.write("3."+prep3+"\n")
myfile.write("4."+prep4+"\n")
myfile.write("5."+prep5+"\n")
myfile.write("6."+prep6+"\n")
myfile.write("7."+prep7+"\n")
myfile.write("8."+prep8+"\n")
myfile.write("9."+prep9+"\n")
myfile.write("10."+prep10+"\n")
print("Here's your list:")
print(prep1)
print(prep2)
print(prep3)
print(prep4)
print(prep5)
print(prep6)
print(prep7)
print(prep8)
print(prep9)
print(prep10)
myfile.close()
print("Thanks for using this program")
print("You should now find a file conatining everything this program has asked for in the same folder you have ran this program from")
print("Enjoy your holiday")
