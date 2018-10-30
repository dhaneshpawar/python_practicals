"""

python demo program for class and object 

""""
import msvcrt
import re

class Student(object):
    static_total_students = 0
    static_department = "Information Technology"
    static_college = "MITAOE"

    @staticmethod
    def s_t_s():
        print "Total students are = ",Student.static_total_students," "
        return ""

    @staticmethod
    def static_depart_method():
        print "Department of students is ", Student.static_department
        return ""

    @staticmethod
    def static_college_method():
        print "college is ", Student.static_college    
        return ""

    def __init__(self, prn,rollNo,name,surname,contact,dob,email):
        self.__prn = prn 
        self.__rollNo = rollNo 
        self.__name = name 
        self.__surname = surname 
        self.__contact = contact
        self.__dob = dob 
        self.__email = email

        def __str__(self):
            return str(self.prn) + str(self.rollNo) + str(self.name) + str(self.surname) + str(self.contact) + str(self.dob) + str(self.email)

        @property
        def prn(self):
            return self.__prn

        @property
        def rollNo(self):
            return self.__rollNo

        @property
        def name(self):
            return self.__name

        @property
        def surname(self):
            return self.__surname

        @property
        def contact(self):
            return self.__contact

        @property
        def dob(self):
            return self.__dob

        @property
        def email(self):
            return self.__email
            
        @prn.setter
        def prn(self, prn):
            print "setter is called"
            if prn == "":
                print "Please Enter some value"
            else:
                self.__prn = prn

        @rollNo.setter
        def rollNo(self, rollNo):
            print "setter is called"
            if rollNo == "":
                print "Please Enter some value"
            else:
                self.__rollNo = rollNo
                
        @name.setter
        def name(self, name):
            print "setter is called"
            if name == "":
                print "Please Enter some value"
            else:
                self.__name = name

        @surname.setter
        def surname(self, surname):
            print "setter is called"
            if surname == "":
                print "Please Enter some value"
            else:
                self.__surname = surname

        @contact.setter
        def contact(self, contact):
            print "setter is called"
            if contact == "":
                print "Please Enter some value"
            else:
                self.__contact = contact
                
        @dob.setter
        def dob(self, dob):
            print "setter is called"
            if dob == "":
                print "Please Enter some value"
            else:
                self.__dob = dob

        @email.setter
        def email(self, email):
            print "setter is called"
            if email == "":
                print "Please Enter some value"
            else:
                self.__email = email


choiceofuser = 0

while choiceofuser != 7:
    print "*********************************************************************************************************"
    print "*                                       STUDENT DATABASE                                                *"
    print "********************                ------------------------                          *******************"
    print "---------------------------------------------------------------------------------------------------------"
    print "     1.New Database     2.Insert     3.Delete     4.Search     5.Update     6.Display All     7.Exit     "
    print "---------------------------------------------------------------------------------------------------------" 
    choiceofuserflag = 0
    while choiceofuserflag == 0:
        choiceofuserstring = raw_input("     Enter your choice : ")
        if choiceofuserstring == "":
            print "Please Enter something..."
        else:
            choiceofuser = int(choiceofuserstring)
            choiceofuserflag = 1    

    if choiceofuser == 1:
        totalStudentsFlag = 0
        
        while totalStudentsFlag == 0:
            totalStudentsstring = raw_input("     Enter how many students you want : ")
            if totalStudentsstring == "":
                print "Please enter something..."
            else:
                totalStudentsFlag = 1
                totalStudents = int(totalStudentsstring)    

        Student.static_total_students = totalStudents        
        print "Now, ",Student.s_t_s()

        all_students = []

        studentdeptflag = 0
        studentdeptchar = 0

        while studentdeptflag == 0:
            studentdept = raw_input("     Enter the Name of dept : ")
            for char in studentdept:
                if(char.isalpha()):
                    pass
                else:
                    studentdeptchar = 1

            if studentdeptchar == 1:
                print "invalid dept name , please enter alphabets only..."      
                studentdeptchar = 0
            elif studentdept == "":
                print "Please Enter something..."
            else:
                studentdeptflag = 1    
                Student.static_department = studentdept

        print "student dept = ",Student.static_depart_method()        

        studentcollegeflag = 0
        studentcollegechar = 0

        while studentcollegeflag == 0:
            studentcollege = raw_input("     Enter the Name of college : ")
            for char in studentcollege:
                if(char.isalpha()):
                    pass
                else:
                    studentcollegechar = 1

            if studentcollegechar == 1:
                print "invalid dept name , please enter alphabets only..."      
                studentcollegechar = 0
            elif studentcollege == "":
                print "Please Enter something..."
            else:
                studentcollegeflag = 1    
                Student.static_college = studentcollege

        print "student college = ",Student.static_college_method()        

        for i in range(totalStudents):

            studentprnflag = 0
            studentprnchar = 0

            while studentprnflag == 0:
                studentprn = raw_input("\n     Enter the PRN : ")                
                for char in studentprn:
                    if(char.isdigit()):
                        pass
                    else:
                        studentprnchar = 1

                if studentprnchar == 1:
                    print "invalid prn , please enter numbers only..."      
                    studentprnchar = 0
                elif studentprn == "":
                    print "Please Enter something..."
                else:
                    studentprnflag = 1    

            studentrollnoflag = 0
            studentrollnochar = 0

            while studentrollnoflag == 0:
                studentrollno = raw_input("     Enter the Roll Number : ")
                for char in studentrollno:
                    if(char.isdigit()):
                        pass
                    else:
                        studentrollnochar = 1

                if studentrollnochar == 1:
                    print "invalid rollno , please enter numbers only..."      
                    studentrollnochar = 0
                elif studentrollno == "":
                    print "Please Enter something..."
                else:
                    studentrollnoflag = 1    

            studentnameflag = 0
            studentnamechar = 0

            while studentnameflag == 0:
                studentname = raw_input("     Enter the Name : ")
                for char in studentname:
                    if(char.isalpha()):
                        pass
                    else:
                        studentnamechar = 1

                if studentnamechar == 1:
                    print "invalid name , please enter alphabets only..."      
                    studentnamechar = 0
                elif studentname == "":
                    print "Please Enter something..."
                else:
                    studentnameflag = 1    

            studentsurnameflag = 0
            studentsurnamechar = 0

            while studentsurnameflag == 0:
                studentsurname = raw_input("     Enter the Surname : ")
                for char in studentsurname:
                    if(char.isalpha()):
                        pass
                    else:
                        studentsurnamechar = 1

                if studentsurnamechar == 1:
                    print "invalid surname , please enter alphabets only..."      
                    studentsurnamechar = 0
                elif studentsurname == "":
                    print "Please Enter something..."
                else:
                    studentsurnameflag = 1    

            studentcontactflag = 0
            studentcontactchar = 0

            while studentcontactflag == 0:
                studentcontact = raw_input("     Enter the Contact Number : ")
                for char in studentcontact:
                    if(char.isdigit()):
                        pass
                    else:
                        studentcontactchar = 1

                if studentcontactchar == 1:
                    print "invalid contact , please enter numbers only..."      
                    studentcontactchar = 0
                elif studentcontact == "":
                    print "Please Enter something..."
                elif len(studentcontact) != 10:
                    print "contact must be 10 digits"    
                elif studentcontact[0] == "0":
                    print "First digit can't be zero"    
                else:
                    studentcontactflag = 1    

            studentdobflag = 0
            studentdobflagdate  = 0
            studentdobflagmonth  = 0
            studentdobflagyear  = 0
            
            while studentdobflag == 0:
                print "     Enter the Date of birth : "        
                
                while studentdobflagdate == 0:
                    studentdobdatestring = raw_input("          Enter the Day : ")
                    if studentdobdatestring == "":
                        print "Please Enter something"
                    else:
                        studentdobdate = int(studentdobdatestring)
                        if studentdobdate < 1 or studentdobdate > 31:
                            print "please enter valid date 0" 
                        else:
                            studentdobflagdate = 1    

                while studentdobflagmonth == 0:
                    studentdobmonthstring = raw_input("          Enter the Month : ")
                    if studentdobmonthstring == "":
                        print "Please Enter something"
                    else:
                        studentdobmonth = int(studentdobmonthstring)
                        if studentdobmonth < 1 or studentdobmonth > 12:
                            print "Please enter valid month"
                        else:
                            studentdobflagmonth = 1

                while studentdobflagyear == 0:
                    studentdobyearstring = raw_input("          Enter the Year : ")
                    if studentdobyearstring == "":
                        print "Please Enter something.."  
                    else:
                        studentdobyear = int(studentdobyearstring)    
                        if studentdobyear < 1900 or studentdobyear > 2018:
                            print "Please enter valid year"
                        else:
                            studentdobflagyear = 1    

                studentdobflag = 1        

            studentdob = str(studentdobdate) + "-" + str(studentdobmonth) + "-" + str(studentdobyear)
            print studentdob

            studentemailflag = 0 

            while studentemailflag == 0:
                studentemail = raw_input("     Enter the E-mail address : ")
                if re.search(r'\S+@\S+.[a-z]', studentemail):
                    studentemailflag = 1
                else:
                    print "Enter valid email"    

            all_students.append(Student(studentprn,studentrollno,studentname,studentsurname,studentcontact,studentdob,studentemail))

    elif choiceofuser == 2:

            studentprnflag = 0
            studentprnchar = 0

            while studentprnflag == 0:
                studentprn = raw_input("\n     Enter the PRN : ")                
                for char in studentprn:
                    if(char.isdigit()):
                        pass
                    else:
                        studentprnchar = 1

                if studentprnchar == 1:
                    print "invalid prn , please enter numbers only..."      
                    studentprnchar = 0
                elif studentprn == "":
                    print "Please Enter something..."
                else:
                    studentprnflag = 1    

            studentrollnoflag = 0
            studentrollnochar = 0

            while studentrollnoflag == 0:
                studentrollno = raw_input("     Enter the Roll Number : ")
                for char in studentrollno:
                    if(char.isdigit()):
                        pass
                    else:
                        studentrollnochar = 1

                if studentrollnochar == 1:
                    print "invalid rollno , please enter numbers only..."      
                    studentrollnochar = 0
                elif studentrollno == "":
                    print "Please Enter something..."
                else:
                    studentrollnoflag = 1    

            studentnameflag = 0
            studentnamechar = 0

            while studentnameflag == 0:
                studentname = raw_input("     Enter the Name : ")
                for char in studentname:
                    if(char.isalpha()):
                        pass
                    else:
                        studentnamechar = 1

                if studentnamechar == 1:
                    print "invalid name , please enter alphabets only..."      
                    studentnamechar = 0
                elif studentname == "":
                    print "Please Enter something..."
                else:
                    studentnameflag = 1    

            studentsurnameflag = 0
            studentsurnamechar = 0

            while studentsurnameflag == 0:
                studentsurname = raw_input("     Enter the Surname : ")
                for char in studentsurname:
                    if(char.isalpha()):
                        pass
                    else:
                        studentsurnamechar = 1

                if studentsurnamechar == 1:
                    print "invalid surname , please enter alphabets only..."      
                    studentsurnamechar = 0
                elif studentsurname == "":
                    print "Please Enter something..."
                else:
                    studentsurnameflag = 1    

            studentcontactflag = 0
            studentcontactchar = 0

            while studentcontactflag == 0:
                studentcontact = raw_input("     Enter the Contact Number : ")
                for char in studentcontact:
                    if(char.isdigit()):
                        pass
                    else:
                        studentcontactchar = 1

                if studentcontactchar == 1:
                    print "invalid contact , please enter numbers only..."      
                    studentcontactchar = 0
                elif studentcontact == "":
                    print "Please Enter something..."
                elif len(studentcontact) != 10:
                    print "contact must be 10 digits"    
                elif studentcontact[0] == "0":
                    print "First digit can't be zero"    
                else:
                    studentcontactflag = 1    

            studentdobflag = 0
            studentdobflagdate  = 0
            studentdobflagmonth  = 0
            studentdobflagyear  = 0
            
            while studentdobflag == 0:
                print "     Enter the Date of birth : "        
                
                while studentdobflagdate == 0:
                    studentdobdatestring = raw_input("          Enter the Day : ")
                    if studentdobdatestring == "":
                        print "Please Enter something"
                    else:
                        studentdobdate = int(studentdobdatestring)
                        if studentdobdate < 1 or studentdobdate > 31:
                            print "please enter valid date 0" 
                        else:
                            studentdobflagdate = 1    

                while studentdobflagmonth == 0:
                    studentdobmonthstring = raw_input("          Enter the Month : ")
                    if studentdobmonthstring == "":
                        print "Please Enter something"
                    else:
                        studentdobmonth = int(studentdobmonthstring)
                        if studentdobmonth < 1 or studentdobmonth > 12:
                            print "Please enter valid month"
                        else:
                            studentdobflagmonth = 1

                while studentdobflagyear == 0:
                    studentdobyearstring = raw_input("          Enter the Year : ")
                    if studentdobyearstring == "":
                        print "Please Enter something.."  
                    else:
                        studentdobyear = int(studentdobyearstring)    
                        if studentdobyear < 1900 or studentdobyear > 2018:
                            print "Please enter valid year"
                        else:
                            studentdobflagyear = 1    

                studentdobflag = 1        

            studentdob = str(studentdobdate) + "-" + str(studentdobmonth) + "-" + str(studentdobyear)
            print studentdob

            studentemailflag = 0 

            while studentemailflag == 0:
                studentemail = raw_input("     Enter the E-mail address : ")
                if re.search(r'\S+@\S+.[a-z]', studentemail):
                    studentemailflag = 1
                else:
                    print "Enter valid email"    

            all_students.append(Student(studentprn,studentrollno,studentname,studentsurname,studentcontact,studentdob,studentemail))
            Student.static_total_students = Student.static_total_students + 1         
            print "Now, ",Student.s_t_s()
    
    elif choiceofuser == 3:
        print("1.Delete by prn        2.Delete by Roll Number ")
        deletechoiceflag = 0 
        while deletechoiceflag == 0:
            deletechoicestring =  raw_input("     Enter your choice : ")
            if deletechoicestring == "":
                print "Plese Enter something"
            else:
                for char in deletechoicestring:
                    if(char.isdigit()):
                        pass
                    else:
                        deletechoiceflag = 1

        deletechoice = int(deletechoicestring)   
            if deletechoice == 1:
                deleteid = raw_input("     Enter the PRN : ")
                for obj in all_students:
                    if obj.prn == deleteid:
                        all_students.remove(obj)
            else:
                deleteid = raw_input("     Enter the Roll Number : ")    
                for obj in all_students:
                    if obj.rollNo == deleteid:
                        all_students.remove(obj)

    elif choiceofuser == 4:
        print "1.Search by PRN     2.Search by Name     3.Search by contact "
        searchchoice = input("     Enter your choice : ")                

        if searchchoice == 1:
            searchprn = raw_input("     Enter the PRN : ")

            for obj in all_students:
                
                if obj.prn == searchprn:
                    print "-----------------------------------------------------------------------------------------"
                    print "     PRN            : " + obj.prn + " "
                    print "     Roll Number    : " + obj.rollNo + " "
                    print "     Name           : " + obj.name + " "
                    print "     Surname        : " + obj.surname + " "
                    print "     Contact Number : ",obj.contact," "
                    print "     Date of Birth  : " + obj.dob + " "
                    print "     E-mail         : " + obj.email + " "
                    print "-----------------------------------------------------------------------------------------"
                    print "\n"
                    
        elif searchchoice == 2:
             searchname = raw_input("     Enter the Name of User : ")
            
             for obj in all_students:

                if obj.name == searchname:
                    print "-----------------------------------------------------------------------------------------"
                    print "     PRN            : " + obj.prn + " "
                    print "     Roll Number    : " + obj.rollNo + " "
                    print "     Name           : " + obj.name + " "
                    print "     Surname        : " + obj.surname + " "
                    print "     Contact Number : ",obj.contact," "
                    print "     Date of Birth  : " + obj.dob + " "
                    print "     E-mail         : " + obj.email + " "
                    print "-----------------------------------------------------------------------------------------"
                    print "\n"

        elif searchchoice == 3:
             searchcontact = raw_input("     Enter the Contact Number : ")

             for obj in all_students:

                if obj.contact == searchcontact:
                    print "-----------------------------------------------------------------------------------------"
                    print "     PRN            : " + obj.prn + " "
                    print "     Roll Number    : " + obj.rollNo + " "
                    print "     Name           : " + obj.name + " "
                    print "     Surname        : " + obj.surname + " "
                    print "     Contact Number : ",obj.contact," "
                    print "     Date of Birth  : " + obj.dob + " "
                    print "     E-mail         : " + obj.email + " "
                    print "-----------------------------------------------------------------------------------------"
                    print "\n"
    
    elif choiceofuser == 5: 
        updatastudent = raw_input("     Enter the PRN : ")
        
        for obj in all_students:
            if obj.prn == updatastudent:
                print("1.PRN     2.Roll Number     3.Name     4.Surname     5.Contact     6.Date of Birth     7.E-mail")
                updatechoice = input("     Enter your choice : ")

                if updatechoice == 1:
                    studentprnflag = 0
                    studentprnchar = 0

                    while studentprnflag == 0:
                        studentprn = raw_input("\n     Enter the PRN : ")                
                        for char in studentprn:
                            if(char.isalpha()):
                                studentprnchar = 1
                            else:
                                pass

                        if studentprnchar == 1:
                            print "invalid prn , please enter numbers only..."      
                            studentprnchar = 0
                        elif studentprn == "":
                            print "Please Enter something..."
                        else:
                            studentprnflag = 1    
                            obj.prn = studentprn

                elif updatechoice == 2:
                    studentrollnoflag = 0
                    studentrollnochar = 0

                    while studentrollnoflag == 0:
                        studentrollno = raw_input("     Enter the Roll Number : ")
                        for char in studentrollno:
                            if(char.isalpha()):
                                studentrollnochar = 1
                            else:
                                pass

                        if studentrollnochar == 1:
                            print "invalid rollno , please enter numbers only..."      
                            studentrollnochar = 0
                        elif studentrollno == "":
                            print "Please Enter something..."
                        else:
                            studentrollnoflag = 1    
                            obj.rollNo = studentrollno

                elif updatechoice == 3:
                    studentnameflag = 0
                    studentnamechar = 0

                    while studentnameflag == 0:
                        studentname = raw_input("     Enter the Name : ")
                        for char in studentname:
                            if(char.isalpha()):
                                pass
                            else:
                                studentnamechar = 1

                        if studentnamechar == 1:
                            print "invalid name , please enter alphabets only..."      
                            studentnamechar = 0
                        elif studentname == "":
                            print "Please Enter something..."
                        else:
                            studentnameflag = 1    
                            obj.name = studentname

                elif updatechoice == 4:
                    studentsurnameflag = 0
                    studentsurnamechar = 0

                    while studentsurnameflag == 0:
                        studentsurname = raw_input("     Enter the Surname : ")
                        for char in studentsurname:
                            if(char.isalpha()):
                                pass
                            else:
                                studentsurnamechar = 1

                        if studentsurnamechar == 1:
                            print "invalid surname , please enter alphabets only..."      
                            studentsurnamechar = 0
                        elif studentsurname == "":
                            print "Please Enter something..."
                        else:
                            studentsurnameflag = 1    
                            obj.surname = studentsurname

                elif updatechoice == 5:
                    studentcontactflag = 0
                    studentcontactchar = 0

                    while studentcontactflag == 0:
                        studentcontact = raw_input("     Enter the Contact Number : ")
                        for char in studentcontact:
                            if(char.isalpha()):
                                studentcontactchar = 1
                            else:
                                pass

                        if studentcontactchar == 1:
                            print "invalid contact , please enter numbers only..."      
                            studentcontactchar = 0
                        elif studentcontact == "":
                            print "Please Enter something..."
                        elif len(studentcontact) != 10:
                            print "contact must be 10 digits"    
                        elif studentcontact[0] == "0":
                            print "First digit can't be zero"    
                        else:
                            studentcontactflag = 1    
                            obj.contact = studentcontact

                elif updatechoice == 6:
                    studentdobflag = 0
                    studentdobflagdate  = 0
                    studentdobflagmonth  = 0
                    studentdobflagyear  = 0
            
                    while studentdobflag == 0:
                        print "     Enter the Date of birth : "        
                
                        while studentdobflagdate == 0:
                            studentdobdate = input("          Enter the Day : ")
                            if studentdobdate < 1 or studentdobdate > 31:
                                print "please enter valid date 0" 
                            else:
                                studentdobflagdate = 1    

                        while studentdobflagmonth == 0:
                            studentdobmonth = input("          Enter the Month : ")
                            if studentdobmonth < 1 or studentdobmonth > 12:
                                print "Please enter valid month"
                            else:
                                studentdobflagmonth = 1

                        while studentdobflagyear == 0:
                            studentdobyear = input("          Enter the Year : ")
                            if studentdobyear < 1900 or studentdobyear > 2018:
                                print "Please enter valid year"
                            else:
                                studentdobflagyear = 1    

                        studentdobflag = 1        

                    studentdob = str(studentdobdate) + "-" + str(studentdobmonth) + "-" + str(studentdobyear)
                    print studentdob
                    obj.dob = studentdob

                elif updatechoice == 7:
                    studentemailflag = 0 

                    while studentemailflag == 0:
                        studentemail = raw_input("     Enter the E-mail address : ")
                        if re.search(r'\S+@\S+.[a-z]', studentemail):
                            studentemailflag = 1
                        else:
                            print "Enter valid email"    
                            obj.email = studentemail

                else:
                    print("#@#@#@#@#@#@#@#@#@#@#@# INVALID CHOICE #@#@#@#@#@#@#@#@#@#@#@#")    

    elif choiceofuser == 6: 
            for obj in all_students:
                print "-----------------------------------------------------------------------------------------"
                print "     PRN            : " + obj.prn + " "
                print "     Roll Number    : " + obj.rollNo + " "
                print "     Name           : " + obj.name + " "
                print "     Surname        : " + obj.surname + " "
                print "     Contact Number : ",obj.contact," "
                print "     Date of Birth  : " + obj.dob + " "
                print "     E-mail         : " + obj.email + " "
                print "-----------------------------------------------------------------------------------------"
                print "\n"

    elif choiceofuser == 7:
        print "\n"
        print "-----------------------------------------------------------------------------------------"
        print "                       THANKS FOR USEING STUDENT DATABASE                                "
        print "-----------------------------------------------------------------------------------------"
        print "\n"
        
    else:
        print "#@#@#@#@#@#@#@#@#@#@#@# INVALID CHOICE #@#@#@#@#@#@#@#@#@#@#@#"

             

             