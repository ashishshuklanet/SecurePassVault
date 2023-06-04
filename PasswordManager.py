
#1. ask user name,ask password
#2.save username,password in a dictionary
#3.save these details to db/file
#3.1 search username in the file and print username/password
#4.encrypt the details before saving
#5. decrypt the details saved 
import re
import csv
import os
import pandas

class User:
    password_file="pwds_copy1.csv"
    headerList=['name', 'password','username','url']
    def __init__(self):
         self.us1ername=''#user_to_search
         self.password=''
         self.url=''  
         self.name=''#app_to_search
         self.Users={}
         self.app_name=''
         self.allusers=[]
         #self.password_file=None

    def SearchUser(self,user,app):
         self.username=user
         self.app_to_search=app
         usersFile=open(self.password_file,"r")
         reader=csv.DictReader(usersFile)
         counter=0
         user_counter=0
         for row in reader:
          counter=counter+1
         #match=re.findall(
          match= re.search(self.username, row['name'])
          print(match)
          #if(row[0]==self.user or row[1]==self.app_name):
          if match is not None:
            found=True
            user_counter=user_counter+1
            print('Password for user %s is %s \n'%(row['name'],row['password']))
            

    def AddUser(self,password,user,filename='',iscopy=False):
        self.password=password;
        self.username=user
        self.Users[user]=password
        if filename:
         self.password_file=filename
        if self.password_file is not None:
            self.AddUsersToFile()
            print('user added to file')
        else:
            print('file name is not defined')
        
        #self.AddUsersToFile()
        #self.Users[username]=password
       
       #dont know if file exists or not
       #if file exists do not add header else add header
    def AddUsersToFile(self):
        if os.path.isfile(self.password_file):
            has_header=True
        else:
            has_header=False
        usersFile=open(self.password_file,"r")

        # csv_test_bytes = usersFile.read(1024)  # Grab a sample of the CSV for format detection.
        # usersFile.seek(0)  # Rewind
        # has_header =False
        # if len(csv_test_bytes)>0:
        #  has_header = csv.Sniffer().has_header(csv_test_bytes)
        #  print(f'has header={has_header}')
        

        with open(self.password_file,"a+") as usersFile:
          writer=csv.DictWriter(usersFile,self.headerList)
          if not has_header:
            writer.writeheader()
          writer.writerow({"name":self.username,"password":self.password})
    @staticmethod
    def HasHeader(filename):
        usersFile=open(filename,"r")
        csv_test_bytes = usersFile.read(1024)  # Grab a sample of the CSV for format detection.
        usersFile.seek(0)  # Rewind
        return csv.Sniffer().has_header(csv_test_bytes)

    @staticmethod
    def WriteHeader(writer):
        #with open(filename,"a+") as usersFile:
          #writer=csv.DictWriter(usersFile,User.headerList)
          if not User.HasHeader(filename):
            writer.writeheader()
         
         
    
    def DeleteUsersinFile(self):
      is_delete=input("going to delete users.Confirm (Y/N)")
      if is_delete.upper()=="Y":
        file=open(self.password_file,"w")
        file.truncate()
        file.close()

    def ReadAllUsers(self):
        with open(self.password_file,"r") as usersFile:
          reader=csv.DictReader(usersFile)
          self.allusers=list(reader)

    def CopyUsers(self,old_file,new_file):
        oldusers=self.ReadAllUsers()
          
        with open(old_file,"r") as usersFile:
           reader=csv.DictReader(usersFile)
           oldusers=list(reader)

        #if not User.HasHeader():
       

        with open(new_file,"w") as userfile:
           writer=csv.DictWriter(userfile,User.headerList) 
          # if not User.HasHeader(new_file):
           writer.writeheader()
           for i in oldusers:
                 writer.writerow(i)
         
pattern='user'
Users={}
username=''
choice=''
while choice!='10':
    if len(Users)>0:
       print('adding user to file')
       #AddUsersToFile(Users)
       Users={}
    print('in outer loop')   
    choice=int(input('''1.Add user\n2.Search user\n3.Delete users\n4.Show all users\n \n5.Copy from one file to another\n
    10.Exit''').strip())
    if(choice== 1):
            
            username=input("Please enter user name  ?").strip()
            #username=username.strip()
            password=input("Please enter password   ?").strip()
            file=input("Please enter filename.Default file name is pwds_copy1.csv?").strip()
            user=User()
            user.AddUser(password,username,file)
            print("\n[bold green]User added[/bold green]!")
            #print('[bold green on blue][/]')
    elif choice ==2:  
            user_name_to_search=input("enter user name to find?").strip()
            app_to_search=input("enter app name to find?").strip()
            user=User()
            user.SearchUser(user_name_to_search,app_to_search)
            #SearchUsersinFile(input("enter user name to find?").strip(),input("enter app name to find?").strip())
    elif choice==3:
            user=User()
            user.DeleteUsersinFile()
    elif choice==4:
            user=User()
            user.ReadAllUsers()  
            allusers=f'Password for users is {user.allusers} \n'
            #pnl1 = [blue]"+allusers+"[/blue]", expand=False, border_style="white")
            #console=Console()
            print(allusers)
            #print('\n[blue]Password for users is %s [/blue]\n'%(user.allusers))
    elif choice==5:
            user=User()
            file1=input("Enter first file")
            file2=input("Enter second file")
            #"imp_pwds.csv" "copyfile1.csv"
            user.CopyUsers(file1,file2)    
    elif choice==10:
            print('exiting the application')
            break
        
