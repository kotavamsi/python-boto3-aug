l =["Ramesh","Ram","Somu"]
username = input("enter usernamr: ")
if  username  in l:
   y = input("Enter Password: ")
   if y == "welcome123":
       print("!!!Congrate login succed!!!")
   else:
       print("!!!Login Faild!!! Invalid password!!!")
else:
   print("!!!Invalid username!!!")
