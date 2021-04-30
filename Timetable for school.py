class Time:
    s=[]
    td={}# DICTIONARY FOR TEACHER AND CORRESPIONDING TAUGHT SUBJECTS
  
    t=[] #LIST OF TEACHERS
    t1=[] # LIST OF TEACHERS (ABSENT + PRESENT)

    
    # DUMMY LISTS FOR DISPLAYING SUBJECTS AS  "" IN TIMETABLE FOR WHICH SUBJECTS TEACHER IS ABSENT

    c01=[] # DUMMY LIST OF CLASS 1 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING SUBJECTS NAME
    c02=[] # DUMMY LIST OF CLASS 2 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING SUBJECTS NAME
    c03=[] # DUMMY LIST OF CLASS 3 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING SUBJECTS NAME
    c04=[] # DUMMY LIST OF CLASS 4 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING SUBJECTS NAME
    c05=[] # DUMMY LIST OF CLASS 5 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING SUBJECTS NAME
    
   
    c6=[] # DUMMY LIST OF CLASS 1 TIMETABE FOR DISPLAYING INCLUDING SUBJECTS RATHER THEN TEACHER NAME
    c7=[] # DUMMY LIST OF CLASS 2 TIMETABE FOR DISPLAYING INCLUDING SUBJECTS RATHER THEN TEACHER NAME
    c8=[] # DUMMY LIST OF CLASS 3 TIMETABE FOR DISPLAYING INCLUDING SUBJECTS RATHER THEN TEACHER NAME
    c9=[] # DUMMY LIST OF CLASS 4 TIMETABE FOR DISPLAYING INCLUDING SUBJECTS RATHER THEN TEACHER NAME
    c10=[] # DUMMY LIST OF CLASS 5 TIMETABE FOR DISPLAYING INCLUDING SUBJECTS RATHER THEN TEACHER NAME


    

    c1=[] # LIST OF CLASS 1 TIMETABLE INCLUDING TEACHERS NAME
    c2=[] # LIST OF CLASS 2 TIMETABLE INCLUDING TEACHERS NAME
    c3=[] # LIST OF CLASS 3 TIMETABLE INCLUDING TEACHERS NAME
    c4=[] # LIST OF CLASS 4 TIMETABLE INCLUDING TEACHERS NAME
    c5=[] # LIST OF CLASS 5 TIMETABLE INCLUDING TEACHERS NAME


    c11=[] # LIST OF CLASS 1 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING TEACHERS NAME
    c21=[] # LIST OF CLASS 2 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING TEACHERS NAME
    c31=[] # LIST OF CLASS 3 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING TEACHERS NAME
    c41=[] # LIST OF CLASS 4 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING TEACHERS NAME
    c51=[] # LIST OF CLASS 5 TIMETABLE WITH ABSENT TEACHERS MARKED AS  "" INCLUDING TEACHERS NAME
    

    p1=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 1 WITH ABSENT TEACHERS MARKED AS  ""
    p2=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 2 WITH ABSENT TEACHERS MARKED AS  ""
    p3=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 3 WITH ABSENT TEACHERS MARKED AS  ""
    p4=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 4 WITH ABSENT TEACHERS MARKED AS  ""
    p5=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 5 WITH ABSENT TEACHERS MARKED AS  ""
    p6=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 6 WITH ABSENT TEACHERS MARKED AS  ""
    p7=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 7 WITH ABSENT TEACHERS MARKED AS  ""
    p8=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 8 WITH ABSENT TEACHERS MARKED AS  ""


    p11=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 1 WITH FULL ATTENDENCE
    p21=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 2 WITH FULL ATTENDENCE
    p31=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 3 WITH FULL ATTENDENCE
    p41=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 4 WITH FULL ATTENDENCE
    p51=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 5 WITH FULL ATTENDENCE
    p61=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 6 WITH FULL ATTENDENCE
    p71=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 7 WITH FULL ATTENDENCE
    p81=[] # LIST OF TEACHERS ENGAGED IN  PERIOD 8 WITH FULL ATTENDENCE

    
    Buffer1=set() # SET OF TEACHERS FREE IN PERIOD 1
    Buffer2=set() # SET OF TEACHERS FREE IN PERIOD 2
    Buffer3=set() # SET OF TEACHERS FREE IN PERIOD 3
    Buffer4=set() # SET OF TEACHERS FREE IN PERIOD 4
    Buffer5=set() # SET OF TEACHERS FREE IN PERIOD 5
    Buffer6=set() # SET OF TEACHERS FREE IN PERIOD 6
    Buffer7=set() # SET OF TEACHERS FREE IN PERIOD 7
    Buffer8=set() # SET OF TEACHERS FREE IN PERIOD 8


    l=8 # LENGTH OF TEACHERS LIST (t)
    # DICTIONARY INCLUDING TEACHERS NAME AS KEY AND SUBJECTS AS VALUE(FIRST VALUE PRESENT  IN LIST (IN VALUEPART) IS PRIMARY SUBJECT TAUGHT BY TEACHER PRESENT IN KEY)
    td={"Rani":["English","Hindi"],"Fida":["Maths","CS"],"Giri":["Hindi","English"],"Lalita":["Music","SS"],"Mani":["SS","Hindi","PE"],"Kiran":["Science","Maths"],"Jonita":["CS","Science"],"Anint":["PE","Music","English"]}
    
    t=["Rani","Fida","Giri","Lalita","Mani","Kiran","Jonita","Anint"] # LIST OF TEACHERS
    t2=["English","Maths","Hindi","Music","SS","Science","CS","PE"] #LIST OF SUBJECTS TAUGHT BY TEACHERS IN LIST (t)



# CODE JUST FOR DISPLAYING  TIMETABLE WITH SUBJECTS WITH FULL ATTENDENCE
    def displayclass(self):
        if((Time.c6 and Time.c7 and Time.c8 and Time.c9 and Time.c10) !=[]): # this code will help not to apppend again and again lists when this function is called
            print("I am inside display blank")
            print("\n\nClass 1 --->  ",Time.c6)
            print("\n\nClass 2 --->  ",Time.c7)
            print("\n\nClass 3 --->  ",Time.c8)
            print("\n\nClass 4 --->  ",Time.c9)
            print("\n\nClass 5 --->  ",Time.c10)
            
        else:
            print(" \n        Timetable of All Classes INCLUDING SUBJECTS NAME  WITH FULL ATTENDENCE     ")
            for i in Time.t2:
                #print(i)
                Time.c6.append(i)
            print("\n\nClass 1 --->  ",Time.c6)
            for i in range (1,8):
                Time.c7.append(Time.t2[i])
                count=0
                if (Time.l==i+1):
                    while(count!=1):
                        Time.c7.append(Time.t2[count])
                        count=count+1
            print("Class 2 --->  ",Time.c7)
            for i in range (2,8):
                Time.c8.append(Time.t2[i])
                count=0
                if (Time.l==i+1):
                    while(count!=2):
                        Time.c8.append(Time.t2[count])
                        count=count+1
            print("Class 3 --->   ",Time.c8)
            for i in range (3,8):
                Time.c9.append(Time.t2[i])
                count=0
                if (Time.l==i+1):
                    count=0
                    while(count!=3):
                        Time.c9.append(Time.t2[count])
                        count=count+1
            print("Class 4 --->  ",Time.c9)
            for i in range (4,8):
                Time.c10.append(Time.t2[i])
                count=0
                if (Time.l==i+1):
                    while(count!=4):
                        Time.c10.append(Time.t2[count])
                        count=count+1
            print("Class 5 --->  ",Time.c10)
            print("\n")



# CODE JUST FOR DISPLAYING TIMETABLE WITH SUBJECTS---( TEACHER ABSENT MARKED AS ABSENT)
    def absenttimetable(self):
        if((Time.c01 and Time.c02 and Time.c03 and Time.c04 and Time.c05) !=[]):# this code will help not to append lists when calling this function again and again
            print("I am in blank")
            print("\n\nClass 1 --->  ",Time.c01)
            print("\n\nClass 2 --->  ",Time.c02)
            print("\n\nClass 3 --->  ",Time.c03)
            print("\n\nClass 4 --->  ",Time.c04)
            print("\n\nClass 5 --->  ",Time.c05)
        else:
            print("        \n Timetable of All Classes INCLUDING SUBJECTS with Teachers ABSENT MARKED AS ABSENT       ")
            for i in Time.t1:
                if(i==""):
                    Time.c01.append("__")
                    continue
                else:pass
                Time.c01.append((Time.td[i])[0])
            print("\n\nClass 1  --->   ",Time.c01)
            for i in range (1,8):
                if(Time.t1[i]==""):
                    Time.c02.append("__")
                    continue
                else:pass
                Time.c02.append((Time.td[Time.t1[i]])[0])
                count=0
                if (Time.l==i+1):
                    while(count!=1):
                        if(Time.t1[count]==""):
                            Time.c02.append("__")
                            count=count+1
                            continue
                        else:pass
                        Time.c02.append((Time.td[Time.t1[count]])[0])
                        count=count+1
            print("Class 2 --->   ",Time.c02)
            for i in range (2,8):
                if(Time.t1[i]==""):
                    Time.c03.append("__")
                    continue
                else:pass
                Time.c03.append((Time.td[Time.t1[i]])[0])
                count=0
                #print("hi")
                if (Time.l==i+1):
                    #print("i m in length")
                    while(count!=2):
                        #print(count)
                        if(Time.t1[count]==""):
                            Time.c03.append("__")
                            #print("Absent")
                            count=count+1
                            continue
                        else:pass
                        Time.c03.append((Time.td[Time.t1[count]])[0])
                        #print("Time")
                        count=count+1
            print("Class 3 --->  ",Time.c03)
            for i in range (3,8):
                if(Time.t1[i]==""):
                    Time.c04.append("__")
                    continue
                else:pass
                Time.c04.append((Time.td[Time.t1[i]])[0])
                count=0
                if (Time.l==i+1):
                    count=0
                    while(count!=3):
                        if(Time.t1[count]==""):
                            Time.c04.append("__")
                            count=count+1
                            continue
                        else:pass
                        Time.c04.append((Time.td[Time.t1[count]])[0])
                        count=count+1
            print("Class 4 --->  ",Time.c04)
            #print("Hello")
            for i in range (4,8):
                if(Time.t1[i]==""):
                    Time.c05.append("__")
                    #print("Absent")
                    continue
                else:pass
                Time.c05.append((Time.td[Time.t1[i]])[0])
                #print("TMA")
                count=0
                if (Time.l==i+1):
                    while(count!=4):
                        if(Time.t1[count]==""):
                            Time.c05.append("__")
                            count=count+1
                            continue
                        else:pass
                        Time.c05.append(((Time.td[Time.t1[count]]))[0])
                        count=count+1
            print("Class 5 --->  ",Time.c05)
            print("\n")




#CODE FOR DISPLAYING TEACHERS WITH THEIR SUBJECTS
    def showteachers(self):
        print("\nTeachers List with Subjects taught by them")
        print("===========================================\n")
        for i in Time.td.keys():
            x=[]
            x=Time.td[i]
            print("\n",i,"---->",end="")
            for j in x:
                print(j," , ",end="")
        print("\n\n")


                
#CODE FOR DISPLAYING TEACHERS FOR PROXY FOR ENTERED SUBJECT
    def sub(self):
        proxy=input("Enter Subject for which you are searching proxy teachers")
        x=[]
        for i in Time.td.keys():
            x=Time.td[i]
            le=len(x)
            for j in range(1,le):
                   if (proxy==x[j]):
                       print("\nTeacher who teaches",proxy,"is ",i) 
                       break
                   else:pass
            

    
#CODE FOR TIMETABLE OF ALL CLASSES INCLUSDING TEACHERS NAME WITH FULL ATTENDENCE--------------------------------

    def c(self):
        #print(" \n        Timetable of All Classes  INCLUDING TEACHERS NAME WITH FULL ATTENDENCE        ")
        for i in Time.t:
           # print(i)
            Time.c1.append(i)
        #print("\n\nClass 1 --->  ",Time.c1)
        for i in range (1,8):
            Time.c2.append(Time.t[i])
            count=0
            if (Time.l==i+1):
                while(count!=1):
                    Time.c2.append(Time.t[count])
                    count=count+1
        #print("Class 2 --->  ",Time.c2)
        for i in range (2,8):
            Time.c3.append(Time.t[i])
            count=0
            if (Time.l==i+1):
                while(count!=2):
                    Time.c3.append(Time.t[count])
                    count=count+1
        #print("Class 3 --->   ",Time.c3)
        for i in range (3,8):
            Time.c4.append(Time.t[i])
            count=0
            if (Time.l==i+1):
                count=0
                while(count!=3):
                    Time.c4.append(Time.t[count])
                    count=count+1
        #print("Class 4 --->  ",Time.c4)
        for i in range (4,8):
            Time.c5.append(Time.t[i])
            count=0
            if (Time.l==i+1):
                while(count!=4):
                    Time.c5.append(Time.t[count])
                    count=count+1
        #print("Class 5 --->  ",Time.c5)
        #print("\n")




        
#CODE FOR TIMETABLE OF ALL CLASSES INCLUDING TEACHERS NAME WITH absentees teachers MARKED AS ""--------------------------

    def newc(self):
        if((Time.c11 and Time.c21 and Time.c31 and Time.c41 and Time.c51)!=[]): # this code helps not to replicate lists when function called again and again
            print("\n\nClass 1  --->   ",Time.c11)
            print("\n\nClass 2  --->   ",Time.c21)
            print("\n\nClass 3  --->   ",Time.c31)
            print("\n\nClass 4  --->   ",Time.c41)
            print("\n\nClass 5  --->   ",Time.c51)
        else:
            # print("        \n Timetable of All Classes INCLUDING TEACHERS NAME with Absent Teachers MARKED AS ""    ")
            for i in Time.t1:
                Time.c11.append(i)
            print("\n\nClass 1  --->   ",Time.c11)
            for i in range (1,8):
                Time.c21.append(Time.t1[i])
                count=0
                if (Time.l==i+1):
                    while(count!=1):
                        Time.c21.append(Time.t1[count])
                        count=count+1
            print("Class 2 --->   ",Time.c21)
            for i in range (2,8):
                Time.c31.append(Time.t1[i])
                count=0
                if (Time.l==i+1):
                    while(count!=2):
                        Time.c31.append(Time.t1[count])
                        count=count+1
            print("Class 3 --->  ",Time.c31)
            for i in range (3,8):
                Time.c41.append(Time.t1[i])
                count=0
                if (Time.l==i+1):
                    count=0
                    while(count!=3):
                        Time.c41.append(Time.t1[count])
                        count=count+1
            print("Class 4 --->  ",Time.c41)
            for i in range (4,8):
                Time.c51.append(Time.t1[i])
                count=0
                if (Time.l==i+1):
                    while(count!=4):
                        Time.c51.append(Time.t1[count])
                        count=count+1
            print("Class 5 --->  ",Time.c51)
            print("\n")



# CODE FOR Period list with absent TEACHERS CREATED WITH LIST OF CLASS TIMETABLE WITH ABSENT TEACHERS(c11--c51)
    
    def p(self):                              
            a=Time.c11[0]
            Time.p1.append(a)
            a=Time.c21[0]
            Time.p1.append(a)
            a=Time.c31[0]
            Time.p1.append(a)
            a=Time.c41[0]
            Time.p1.append(a)
            a=Time.c51[0]
            Time.p1.append(a)
            #print("Period 1 in all classes= ",Time.p1)

            a=Time.c11[1]
            Time.p2.append(a)
            a=Time.c21[1]
            Time.p2.append(a)
            a=Time.c31[1]
            Time.p2.append(a)
            a=Time.c41[1]
            Time.p2.append(a)
            a=Time.c51[1]
            Time.p2.append(a)
            #print("Period 2= ",Time.p2)

            a=Time.c11[2]
            Time.p3.append(a)
            a=Time.c21[2]
            Time.p3.append(a)
            a=Time.c31[2]
            Time.p3.append(a)
            a=Time.c41[2]
            Time.p3.append(a)
            a=Time.c51[2]
            Time.p3.append(a)
            #print("Period 3= ",Time.p3)

            a=Time.c11[3]
            Time.p4.append(a)
            a=Time.c21[3]
            Time.p4.append(a)
            a=Time.c31[3]
            Time.p4.append(a)
            a=Time.c41[3]
            Time.p4.append(a)
            a=Time.c51[3]
            Time.p4.append(a)
           # print("Period 4= ",Time.p4)

            a=Time.c11[4]
            Time.p5.append(a)
            a=Time.c21[4]
            Time.p5.append(a)
            a=Time.c31[4]
            Time.p5.append(a)
            a=Time.c41[4]
            Time.p5.append(a)
            a=Time.c51[4]
            Time.p5.append(a)
           # print("Period 5= ",Time.p5)

            a=Time.c11[5]
            Time.p6.append(a)
            a=Time.c21[5]
            Time.p6.append(a)
            a=Time.c31[5]
            Time.p6.append(a)
            a=Time.c41[5]
            Time.p6.append(a)
            a=Time.c51[5]
            Time.p6.append(a)
           # print("Period 6= ",Time.p6)

            a=Time.c11[6]
            Time.p7.append(a)
            a=Time.c21[6]
            Time.p7.append(a)
            a=Time.c31[6]
            Time.p7.append(a)
            a=Time.c41[6]
            Time.p7.append(a)
            a=Time.c51[6]
            Time.p7.append(a)
           # print("Period 7= ",Time.p7)

            a=Time.c11[7]
            Time.p8.append(a)
            a=Time.c21[7]
            Time.p8.append(a)
            a=Time.c31[7]
            Time.p8.append(a)
            a=Time.c41[7]
            Time.p8.append(a)
            a=Time.c51[7]
            Time.p8.append(a)
            # print("Period 8= ",Time.p8)


            
# CODE FOR original period list with COMPLETE ATTENDENCE TEACHERS CREATED WITH CLASS TIMETABLE LISTS(c1--c5)
            
    #@staticmethod
    def pe(self) :                                         
            a=Time.c1[0]
            Time.p11.append(a)
            a=Time.c2[0]
            Time.p11.append(a)
            a=Time.c3[0]
            Time.p11.append(a)
            a=Time.c4[0]
            Time.p11.append(a)
            a=Time.c5[0]
            Time.p11.append(a)
            #print("Period 1  Presentees = ",Time.p11)

            a=Time.c1[1]
            Time.p21.append(a)
            a=Time.c2[1]
            Time.p21.append(a)
            a=Time.c3[1]
            Time.p21.append(a)
            a=Time.c4[1]
            Time.p21.append(a)
            a=Time.c5[1]
            Time.p21.append(a)
            #print("Period 2= ",Time.p2)

            a=Time.c1[2]
            Time.p31.append(a)
            a=Time.c2[2]
            Time.p31.append(a)
            a=Time.c3[2]
            Time.p31.append(a)
            a=Time.c4[2]
            Time.p31.append(a)
            a=Time.c5[2]
            Time.p31.append(a)
            #print("Period 3= ",Time.p31)

            a=Time.c1[3]
            Time.p41.append(a)
            a=Time.c2[3]
            Time.p41.append(a)
            a=Time.c3[3]
            Time.p41.append(a)
            a=Time.c4[3]
            Time.p41.append(a)
            a=Time.c5[3]
            Time.p41.append(a)
           # print("Period 4= ",Time.p4)

            a=Time.c1[4]
            Time.p51.append(a)
            a=Time.c2[4]
            Time.p51.append(a)
            a=Time.c3[4]
            Time.p51.append(a)
            a=Time.c4[4]
            Time.p51.append(a)
            a=Time.c5[4]
            Time.p51.append(a)
           # print("Period 5= ",Time.p5)

            a=Time.c1[5]
            Time.p61.append(a)
            a=Time.c2[5]
            Time.p61.append(a)
            a=Time.c3[5]
            Time.p61.append(a)
            a=Time.c4[5]
            Time.p61.append(a)
            a=Time.c5[5]
            Time.p61.append(a)
           # print("Period 6= ",Time.p6)

            a=Time.c1[6]
            Time.p71.append(a)
            a=Time.c2[6]
            Time.p71.append(a)
            a=Time.c3[6]
            Time.p71.append(a)
            a=Time.c4[6]
            Time.p71.append(a)
            a=Time.c5[6]
            Time.p71.append(a)
           # print("Period 7= ",Time.p7)

            a=Time.c1[7]
            Time.p81.append(a)
            a=Time.c2[7]
            Time.p81.append(a)
            a=Time.c3[7]
            Time.p81.append(a)
            a=Time.c4[7]
            Time.p81.append(a)
            a=Time.c5[7]
            Time.p81.append(a)
            # print("Period 8= ",Time.p8)





# CODE FOR JUST DISPLAYING FREE TEACHERS IN RESPECTED PERIODS (DIFF BETWEEN LIST OF TEACHERSPRESENT THAT DAY(t1)~ LIST OF PERIOD NO INCLUDING ABSENT TEACHERS(p1---p8))
            
    def freebuffer(self):
        period=int(input("Enter Period no for getting names of free teachers"))
        if (period==1):
            s=set(Time.t1)
            s1=set(Time.p1)
            Time.Buffer1= s.difference(s1)
            print("\n\n Free Teachers for Period 1 ",Time.Buffer1)
        elif(period==2):
            s=set(Time.t1)
            s2=set(Time.p2)
            Time.Buffer2= s.difference(s2)
            print(" Free Teachers for Period 2 ",Time.Buffer2)
        elif(period==3):
            s=set(Time.t1)
            s3=set(Time.p3)
            Time.Buffer3= s.difference(s3)
            print(" Free Teachers for Period 3 ",Time.Buffer3)
        elif(period==4):
            s=set(Time.t1)
            s4=set(Time.p4)
            Time.Buffer4= s.difference(s4)
            print(" Free Teachers for Period 4 ",Time.Buffer4)
        elif(period==5):
            s=set(Time.t1)
            s5=set(Time.p5)
            Time.Buffer5= s.difference(s5)
            print(" Free Teachers for Period 5 ",Time.Buffer5)
        elif(period==6):
            s=set(Time.t1)
            s6=set(Time.p6)
            Time.Buffer6= s.difference(s6)
            print(" Free Teachers for Period 6 ",Time.Buffer6)
        elif(period==7):
            s=set(Time.t1)
            s7=set(Time.p7)
            Time.Buffer7= s.difference(s7)
            print(" Free Teachers for Period 7 ",Time.Buffer7)
        elif(period==8):
            s=set(Time.t1)
            s8=set(Time.p8)
            Time.Buffer8= s.difference(s8)
            print(" Free Teachers for Period 8 ",Time.Buffer8)

                

# COPY OF  FREE TEACHERS SET USED TO FIND OUT DIFFERENCE B/W LIST OF TECAHERS(LIST OF TEACHERS PRESENT THE DAY(t1) ~ PERIOD NO- TEACHERS LIST(p1-p8)INCLUDING ABSENT TEACHERS)
    def freebuffer1(self):
                s=set(Time.t1)
                s1=set(Time.p1)
                Time.Buffer1= s.difference(s1)
                #print("\n\n Free Teachers for Period 1 ",Time.Buffer1)
                
                s2=set(Time.p2)
                Time.Buffer2= s.difference(s2)
                #print(" Free Teachers for Period 2 ",Time.Buffer2)
                
                s3=set(Time.p3)
                Time.Buffer3= s.difference(s3)
                #print(" Free Teachers for Period 3 ",Time.Buffer3)
                
                s4=set(Time.p4)
                Time.Buffer4= s.difference(s4)
                #print(" Free Teachers for Period 4 ",Time.Buffer4)
                
                s5=set(Time.p5)
                Time.Buffer5= s.difference(s5)
                #print(" Free Teachers for Period 5 ",Time.Buffer5)
                
                s6=set(Time.p6)
                Time.Buffer6= s.difference(s6)
                #print(" Free Teachers for Period 6 ",Time.Buffer6)
            
                s7=set(Time.p7)
                Time.Buffer7= s.difference(s7)
                #print(" Free Teachers for Period 7 ",Time.Buffer7)
                
                s8=set(Time.p8)
                Time.Buffer8= s.difference(s8)
                #print(" Free Teachers for Period 8 ",Time.Buffer8)

                

    # CODE FOR ASSIGNING  FREE TEACHERS IN PERIOD 1---------------------
    def af1(self):
            #print("\n\n*************  BUFFER for Period -1  **************\n")
            subjects=[] # LIST OF SUBJECTS TAUGHT BY ABSENT TEACHER
            flag=0
            keys=[]     # SUBJECTS TAUGHT BY FREE TEACHERS FOR PERIOD 1
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer1)  # CONVERTING SET OF FREE TEACHERS  FOR PERIOD 1 TO LIST
            l=len(w)              # LENGTH OF LIST
            '''for m in Time.Buffer1:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list1=",l)
            if("" not in Time.p1):                              # IF IN PERIOD LIST NO "" PRESENT MEANS ALL TEACHERS ARE PRESENT FOR PERIOD 1
                print("\nAll Teachers Present for Period 1")
                
    
            for i in Time.p1: # SCANNING THROUGH PERIOD LIST WITH ABSENT TEACHERS MARKED(p1)
                j=0
                count=count+1
                #print (count)
                if(i==""):# IF ABSENT TEACHER IS THERE IN p1 LIST
                    ind=Time.p1.index(i)
                    if(Time.Buffer1==set()):   # CHECK FOR FREE TEACHER FOR PERIOD 1
                         print("\nNo Teacher Present for Period 1 ")
                         break
                    if(j==l):
                        print ("No Teacher Free for Period 1")
                        break
                    if (w[j]==""): # IF FREE TEACHERS LIST HAS "" ie ABSENT TEACHER PRESENT THEN INCREMENT j
                        j=j+1
                    
                    
                    #print(count)
                    teacher= Time.p11[count-1] # FIND OUT WHICH TEACHER IS ABSENT, FROM LIST OF PERIOD 1 MADE OF WITH ALL TEACHERS MARKED(p11) 
                    #print(teacher)
                    subjects = Time.td.get(teacher) # GET SUBJECTS OF THAT TEACHER FROM td DICTIONARY
                    #print (subjects)
                    while(flag!=1):
                      keys=Time.td.get(w[j]) # SUBJECTS TAUGHT BY TEACHERS IN LIST OF FREE TEACHERS IN PERIOD 1 AS OUR PRIORITY IS TO ASSIGN SAME SUBJECT TEACHER
                      #print(keys)

                      #print(w[j])
                      for inc in keys: # SCANNING THROUGH SUBJECTS OF TEACHER IN FREE TEACHERS (keys ARE SUBJECTS)
                        #print (inc)
                        if(subjects[0]==inc): # CHECKING WHETHER THE SUBJECT IN keys MATCHES SUBJECTS OF ABSENT TEACHER'S SUBJECT(subjects)
                        
                           #print(w[j])
                           flag=1 # WHEN SUBJECTS MATCHES FLAG IS RAISED
                           ind=Time.p1.index(i)
                           break
                      if (flag==0):
                          #print(l)
                          j=j+1              # INCREMENTING j FOR GETTING NEXT TEACHER FROM FREE LIST, WHOSE SUBJECT CAN BE MATCHED WITH ABSENT TEACHER
                          if(j==l):          # IF j VALUE REACHES TILL LAST OF LIST OF FREE TEACHERS FOR PERIOD 1(w) ASSIGN LAST TEACHERS ie (l) FOR FREE PERIOD
                              #print(l)
                               j=j-1
                               ind=Time.p1.index(i)
                               flag=1
                                    
                               #print("Im ",j)
                               #print(l)
                               break
                               
                               #print(j)
                               #print("Hello")
                               cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                            
                    i=w[j]
                    #print(i)
                    Time.p1[ind]=w[j] # for inserting alloted teacher to timetable
                    #print(Time.p1)
                    #print (w[j])
                    #print (count)
                    #Time.c0[count]=w[j]
                    #print(Time.c01,w[j])
                    #print(Time.c01[0])
                    if(count==1):
                        Time.c01[0]=w[j]
                    elif(count==2):
                        Time.c02[0]=w[j]
                    elif(count==3):
                        Time.c03[0]=w[j]
                    elif(count==4):
                        Time.c04[0]=w[j]
                    elif(count==5):
                        Time.c05[0]=w[j]
                    
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 1")
                    w.remove(w[j])
                    l=l-1
                    flag=0
                    # print (Time.Buffer1)


                   
                    
    # CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 2--------------------------------------------------------------------
    def af2(self):
            #print("\n\n*************  BUFFER for Period -2  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer2)
            l=len(w)
            #print(w)
            '''for m in Time.Buffer2:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list2=",l)
            
              
            if("" not in Time.p2):
                #print (Time.p2)
                print("\nAll Teachers Present for Period 2")              
            for i in Time.p2:
                j=0
                count=count+1
                if(i==""):
                    if(Time.Buffer2==set()):
                         print("\nNo Teacher Present for Period 2 ")
                         break
                    if(j==l):
                        print ("No Teacher Free for Period 2")
                        break
                    if (w[j]==""):
                        j=j+1
                    
                    
                     
                    teacher= Time.p21[count-1]
                    #print(teacher)
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                      keys=Time.td.get(w[j])
                      #print(keys)
                      #print(w[j])
                      for inc in keys:
                       # print (inc)
                        if(subjects[0]==inc):
                            ind=Time.p2.index(i)
                            flag=1
                            break
                      if (flag==0):
                          #print(l)
                          j=j+1
                          if(j==l):
                              #print(l)
                               j=j-1
                               ind=Time.p2.index(i)
                               flag=1
                                    
                               #print("Im ",j)
                               #print(l)
                               break
                               
                               #print(j)
                               #print("Hello")
                               cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                             
                    i=w[j]
                    Time.p2[ind]=w[j]
                    if(count==1):
                        Time.c01[1]=w[j]
                    elif(count==2):
                        Time.c02[1]=w[j]
                    elif(count==3):
                        Time.c03[1]=w[j]
                    elif(count==4):
                        Time.c04[1]=w[j]
                    elif(count==5):
                        Time.c05[1]=w[j]
                    #print (w[j])
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 2")
                    w.remove(w[j])
                    l=l-1
                    flag=0
                    #print (Time.Buffer2)




# CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 3---------------------------------------------------------------------------------------------------
    def af3(self):
            #print("\n\n*************  BUFFER for Period -3  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer3)
            l=len(w)
            '''for m in Time.Buffer3:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list3=",l)
            if("" not in Time.p3):
                print("\nAll Teachers Present for Period 3")
                       
            for i in Time.p3:
                    j=0
                    count=count+1
                    if(i==""):
                        if(Time.Buffer3==set()):
                             print("\nNo Teacher Present for  Period 3 ")
                             break
                        if(j==l):
                                 print ("No Teacher Free for Period-3")
                                 break
                        if (w[j]==""):
                            j=j+1
                        
                        
                     
                        teacher= Time.p31[count-1]
                        #print(teacher)
                        subjects = Time.td.get(teacher)
                        #print (subjects)
                        while(flag!=1):
                            keys=Time.td.get(w[j])
                            #print(keys)
                            #print(w[j])
                            for inc in keys:
                                #print (inc)
                                if(subjects[0]==inc):
                                    ind=Time.p3.index(i)
                                    flag=1
                                    break
                            if (flag==0):
                                #print(l)
                                j=j+1
                                if(j==l):
                                    #print(l)
                                    j=j-1
                                    ind=Time.p3.index(i)
                                    flag=1
                                    
                                    #print("Im ",j)
                                    #print(l)
                                    break
                               
                                #print(j)
                                #print("Hello")
                                cont=cont+1
                                #print(cont)
                                    
                       
                        i=w[j]
                        Time.p3[ind]=w[j]
                        if(count==1):
                            Time.c01[2]=w[j]
                        elif(count==2):
                            Time.c02[2]=w[j]
                        elif(count==3):
                            Time.c03[2]=w[j]
                        elif(count==4):
                            Time.c04[2]=w[j]
                        elif(count==5):
                            Time.c05[2]=w[j]
                        #print (w[j])
                        print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 3")
                        w.remove(w[j])
                        l=l-1
                        #print(Time.Buffer3)
                        flag=0


   # CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 4-----------------------------------------------------
    def af4(self):
            #print("\n\n*************  BUFFER for Period -4  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer4)
            l=len(w)
            '''for m in Time.Buffer4:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list4=",l)
            if("" not in Time.p4):
                print("\nAll Teachers Present for Period 4")
            
            for i in Time.p4:
                j=0
                count=count+1
                if(i==""):
                    if(Time.Buffer4==set()):
                       print("NO Teacher Present for Period-4")
                       break
                    if(j==l):
                        print ("No Teacher Free for Period-4")
                        break
                    if (w[j]==""):
                        j=j+1
                        
                    teacher= Time.p41[count-1]
                    #print(teacher)
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                      keys=Time.td.get(w[j])
                      #print(keys)
                      #print(w[j])
                      for inc in keys:
                        #print (inc)
                        if(subjects[0]==inc):
                           ind=Time.p4.index(i)
                           #print(w[j])
                           flag=1
                           break
                      if (flag==0):
                          #print(l)
                          j=j+1
                          if(j==l):
                              #print(l)
                               j=j-1
                               ind=Time.p4.index(i)
                               flag=1
                                    
                               #print("Im ",j)
                               #print(l)
                               break
                               
                               #print(j)
                               #print("Hello")
                               cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                                
                    i=w[j]
                    Time.p4[ind]=w[j]
                    if(count==1):
                        Time.c01[3]=w[j]
                    elif(count==2):
                        Time.c02[3]=w[j]
                    elif(count==3):
                        Time.c03[3]=w[j]
                    elif(count==4):
                        Time.c04[3]=w[j]
                    elif(count==5):
                        Time.c05[3]=w[j]
                    #print (w[j])
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 4")
                    w.remove(w[j])
                    l=l-1
                    # print (Time.Buffer4)
                    flag=0


                    

 # CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 5 --------------------------------------------------------------------   
    def af5(self):
            #print("\n\n*************  BUFFER for Period -5 **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer5)
            l=len(w)
            '''for m in Time.Buffer5:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list5=",l)
            if("" not in Time.p5):
                print("\nAll Teachers Present for Period 5")
            
                
    
            for i in Time.p5:
                j=0
                count=count+1
                #print(count)
                if(i==""):
                    if(Time.Buffer5==set()):
                       print("No Teacher Present for Period-5")
                       break
                    if(j==l):
                        print ("No Teacher Free for Period-5")
                        break
                    if (w[j]==""):
                        j=j+1
                    
                    
                    #print(j)
                    teacher= Time.p51[count-1]
                    #print(teacher)
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                     #     print(flag)
                          keys=Time.td.get(w[j])
                      #    print(keys)
                       #   print(w[j])
                          for inc in keys:
                        #    print (inc)
                            if(subjects[0]==inc):
                                ind=Time.p5.index(i)
                                #print(w[j])
                                flag=1
                                break
                          if (flag==0):
                                #print(l)
                                j=j+1
                                if(j==l):
                                    #print(l)
                                    j=j-1
                                    ind=Time.p5.index(i)
                                    flag=1
                                    
                                    #print("Im ",j)
                                    #print(l)
                                    break
                               
                                    #print(j)
                                    #print("Hello")
                                    cont=cont+1
                                    #print(cont)
                              
                   
                    i=w[j]
                    Time.p5[ind]=w[j]
                    if(count==1):
                        Time.c01[4]=w[j]
                    elif(count==2):
                        Time.c02[4]=w[j]
                    elif(count==3):
                        Time.c03[4]=w[j]
                    elif(count==4):
                        Time.c04[4]=w[j]
                    elif(count==5):
                        Time.c05[4]=w[j]
                    #print (w[j])
                    #print (count)
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 5")
                    w.remove(w[j])
                    l=l-1
                    flag=0
                   #print (Time.Buffer5)



# CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 6-----------------------------------------------------------------------------
    
    def af6(self):
            #print("\n\n*************  BUFFER for Period -6  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer6)
            l=len(w)
            '''for m in Time.Buffer6:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list6=",l)
            if("" not in Time.p6):
                print("\nAll Teachers Present for Period 6")
                
    
            for i in Time.p6:
                j=0
                #print(Time.p6)
                count=count+1
                #print (count)
                if(i==""):
                    if(Time.Buffer6==set()):
                       print("No Teacher Present for Period-6")
                       break
                    if(j==l):
                        print ("No Teacher Free for Period-6")
                        break
                    if (w[j]==""):
                        j=j+1
                        break
                    
                    
                    
                    #print(count)
                    teacher= Time.p61[count-1]
                    
                    
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                     # print(flag)
                      keys=Time.td.get(w[j])
                      #print(keys)
                      #print(w[j])
                      for inc in keys:
                       # print (inc)
                        if(subjects[0]==inc):
                           ind=Time.p6.index(i)
                        #   print(w[j])
                           flag=1
                           break
                      if (flag==0):
                          #print(l)
                          j=j+1
                          if(j==l):
                              #print(l)
                               j=j-1
                               ind=Time.p6.index(i)
                               flag=1
                                    
                               #print("Im ",j)
                               #print(l)
                               break
                               
                               #print(j)
                               #print("Hello")
                               cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                             
                    i=w[j]
                    Time.p6[ind]=w[j]
                    #print (w[j])
                    if(count==1):
                        Time.c01[5]=w[j]
                    elif(count==2):
                        Time.c02[5]=w[j]
                    elif(count==3):
                        Time.c03[5]=w[j]
                    elif(count==4):
                        Time.c04[5]=w[j]
                    elif(count==5):
                        Time.c05[5]=w[j]
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 6")
                    w.remove(w[j])
                    l=l-1
                    flag=0
                    #print (Time.Buffer6)




 # CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 7------------------------------------------------------------------------------------ 
    def af7(self):
            #print("\n\n*************  BUFFER for Period -7  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            
            count=0
            cont=0
            w=list(Time.Buffer7)
            l=len(w)
            '''for m in Time.Buffer7:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list7=",l)
            if("" not in Time.p7):
                print("\nAll Teachers Present for Period 7")
                
    
            for i in Time.p7:
                j=0
                count=count+1
                if(i==""):
                    if(Time.Buffer7==set()):
                       print("No Teacher Present for Period-7")
                       break
                    if(j==l):
                        print ("No Teacher Free for Period-7")
                        break
                    
                    if (w[j]==""):
                        j=j+1
                        break
                    teacher= Time.p71[count-1]
                    #print(teacher)
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                        keys=Time.td.get(w[j])
                        #print(keys)
                        #print(keys)
                        #print(w[j])
                        for inc in keys:
                            if(subjects[0]==inc):
                                ind=Time.p7.index(i)
                                flag=1
                                break
                        if (flag==0):
                            #print(l)
                            j=j+1
                            if(j==l):
                                #print(l)
                                j=j-1
                                ind=Time.p7.index(i)
                                flag=1
                                    
                                #print("Im ",j)
                                #print(l)
                                break
                               
                               #print(j)
                               #print("Hello")
                                cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                             
                    i=w[j]
                    Time.p7[ind]=w[j]
                    if(count==1):
                        Time.c01[6]=w[j]
                    elif(count==2):
                        Time.c02[6]=w[j]
                    elif(count==3):
                        Time.c03[6]=w[j]
                    elif(count==4):
                        Time.c04[6]=w[j]
                    elif(count==5):
                        Time.c05[6]=w[j]
                    #print (w[j])
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 7")
                    w.remove(w[j])
                    l=l-1
                    #print (Time.Buffer7)
                    flag=0




# CODE FOR ASSIGNING FREE TEACHERS IN PERIOD 8----------------------------------------------------------------------------------------
    def af8(self):
            #print("\n\n*************  BUFFER for Period -8  **************\n")
            subjects=[]
            flag=0
            keys=[]
            j=0
            count=0
            cont=0
            w=list(Time.Buffer8)
            l=len(w)
            '''for m in Time.Buffer8:
                if (m==""):
                  l=l-1'''
            
            #print(w)
            #print(" Length of Buffer list8=",l)
            if("" not in Time.p8):
                print("\nAll Teachers Present for Period 8")
                
    
            for i in Time.p8:
                j=0
                count=count+1
                #print (count)
                if(i==""):
                    if(Time.Buffer8==set()):
                       print("No Teacher Free for Period-8")
                       break
                    if(j==l):
                        print ("No Teacher Present for Period-8")
                        break
                    
                    if (w[j]==""):
                        j=j+1
                        return
                    
                    
                    #print (count)
                    teacher=Time.p81[count-1]
                    #print(teacher)
                    subjects = Time.td.get(teacher)
                    #print (subjects)
                    while(flag!=1):
                      keys=Time.td.get(w[j])
                     # print(keys)
                      #print(w[j])
                      for inc in keys:
                       # print (inc)
                        if(subjects[0]==inc):
                        
                        #   print(w[j])
                           ind=Time.p8.index(i)
                           flag=1
                           break
                      if (flag==0):
                          #print(l)
                          j=j+1
                          if(j==l):
                              #print(l)
                               j=j-1
                               ind=Time.p8.index(i)
                               flag=1
                                    
                               #print("Im ",j)
                               #print(l)
                               break
                               
                               #print(j)
                               #print("Hello")
                               cont=cont+1
                               #print(cont)
                                                   
                                
                                #print(l)
                             
                             
                    i=w[j]
                    Time.p8[ind]=w[j]
                    if(count==1):
                        Time.c01[7]=w[j]
                    elif(count==2):
                        Time.c02[7]=w[j]
                    elif(count==3):
                        Time.c03[7]=w[j]
                    elif(count==4):
                        Time.c04[7]=w[j]
                    elif(count==5):
                        Time.c05[7]=w[j]
                    # print (w[j])
                    print ("\n\nAllot Teacher ",w[j] ,"for Class" , count," for  Period 8")
                
                    w.remove(w[j])
                    l=l-1
                   # print (Time.Buffer8)
                    flag=0





 # CODE FOR MANUAL ALLOTEMENT OF TEACHERS INTO FREE PERIODS  (1-8) --------------------------------------------------------------------------  
    def manual1(self):
        
        print("Period 1 Teachers list ",Time.p1)
        w=list(Time.Buffer1)
        #d=[x.lower() for x in Time.p1]       trying for making case insensitive 
        #print(d)
       
        
        for i in Time.p1:
            if(i==""):
                #print ("I m in empty")
              
                ind= Time.p1.index("")
                #print(ind)
                print("\nFree Teachers are ",w)
                if(w==[]):
                    break
                tname="abc"
                #tname=input("\nEnter teacher to be alloted from buffer ----->    ")
                #tname.casefold()
                while(tname not in  w):
                    tname=input("\nEnter teacher to be alloted from buffer ----->    ")
                    print("Try Again")
                    #tname=input("\nEnter teacher to be alloted from buffer ----->    ") 
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p1[ind]=allot
                
                #print(Time.p1)
                #print(w)
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")
    def manual2(self):
        free=[]
        k=0
        print("Period 2 Teachers list ",Time.p2)
        w=list(Time.Buffer2)
        for i in Time.p2:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p2.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer------>")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p2[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")
    def manual3(self):
        free=[]
        k=0
        print("Period 3 Teachers list ",Time.p3)
        w=list(Time.Buffer3)
        for i in Time.p3:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p3.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer------>")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p3[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy") 
            
    def manual4(self):
        free=[]
        k=0
        print("Period 4 Teachers list ",Time.p4)
        w=list(Time.Buffer4)
        for i in Time.p4:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p4.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer--------->")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p4[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")    
        
    def manual5(self):
        free=[]
        k=0
        print("Period 5 Teachers list ",Time.p5)
        w=list(Time.Buffer5)
        for i in Time.p5:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p5.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer------->")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p5[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")       
          
    def manual6(self):
        free=[]
        k=0
        print("Period 6 Teachers list ",Time.p6)
        w=list(Time.Buffer6)
        for i in Time.p6:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p6.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer-------->")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p6[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
            continue

    def manual7(self):
        free=[]
        k=0
        print("Period 7 Teachers list ",Time.p7)
        w=list(Time.Buffer7) # CONVERTING SET OF FREE TEACHERS TO LIST
        for i in Time.p7:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p7.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer------->")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p7[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")    
    def manual8(self):
        free=[]
        k=0
        print("Period 8 Teachers list ",Time.p8)
        w=list(Time.Buffer8)
        for i in Time.p8:
            #print(i)
            if(i==""):
                #print ("I m in empty")
            
                ind= Time.p8.index("")
                print("\nFree Teachers are ",w)
                #print(ind)
                #print(w)
                if(w==[]):
                    break
                tname=input("\nEnter teacher to be alloted from buffer--------->")
                indx=w.index(tname)
                allot=w.pop(indx)
                #print(w)
                #print(allot)
                Time.p8[ind]=allot
                print ("\nTeacher  alloted ",allot ," for Class ",ind+1)
        else:print("All periods are busy")                





# ----------------------------------------------------------------   MAIN CODE RUNNING --------------------------------------------------------------------------------------------------------------------

t5=Time() # OBJECT CREATED FOR CALLING FUNCTIONS        
print ("\n\n#############################################################   Welcome to XYZ School Timetable         ##########################################\n")
#l2=len(Time.t)
'''print("Teachers List with Subjects taught by them")
print("===========================================\n")
for i in Time.td.keys():
    x=[]
    x=Time.td[i]
    print("\n",i,"---->",end="")
    for j in x:
        print(j," , ",end="")'''
    
#print("\n\nTeacher's List : ", Time.t)
print("\n______________________________________________________________________________________________________________________________________________")
print("\n\nEnter  Teacher's Attendence ")
for i in Time.t:
    print ("\n" , i)
    u=int(input(" Enter 1 if this teacher is Present and 0 for absent "))
    if(u==1):
        Time.t1.append(i)
    else :Time.t1.append("")
    #print(Time.t1)
    #print(Time.t)
set1=set(Time.t1) # SET  OF TEACHERS PRESENT (INCLUDING ABSENT)
#print(set1)
set2=set(Time.t)  # SET OF  ALL TEACHERS
#print(set2)
at=set2.difference(set1)  # SET OF ABSENT TEACHERS

print("\n\n")
absentteachers=list(at)
if(absentteachers==[]):
    print("All Teachers present Today")
#print(absentteachers)
subindict=[]          # LIST OF SUBJECTS TAUGHT BY ABSENT TEACHERS
for i in absentteachers:
    subindict=Time.td[i]
    print (" Absent teacher name is  ",i ,"and subject taken -->  ",subindict[0])


#--------------------------------------------------------------------------------------------------

# OBJECT CALLING FUNCTIONS
#t5.displayclass()    # FOR DISPLAYING CLASS TIMETABLE INCLUDING SUBJECTS NAME WITH COMPLETE ATTENDENCE
#t5.absenttimetable() # FOR DISPALYING CLASS TIMETABLE INCLUDING SUBJECTS NAME WITH TEACHERS absent MARKED AS "ABSENT"


t5.c()               # FOR CREATING  CLASS TIMETABLE LISTS INCLUDING TEACHERS NAME
t5.newc()            # FOR CREATING CLASS TIMETABLE LISTS WITH ABSENT TEACHERS INCLUDING TEACHERS NAME


t5.pe() #CALLING FOR GETING PERIOD LIST WITH NO ABSENTEES INCLUDING TEACHERS NAME (STATIC METHOD)
t5.p()    # CALLING FOR GETTING PERIOD LIST WITH ABSENTEES  INCLUDING TEACHERS NAME

t5.absenttimetable()
t5.displayclass()



while(True):
    
    print("\nEnter  1   for Alloting Teacher for Period 1 ")
    print("Enter    2   for Alloting Teacher for Period 2")
    print("Enter    3   for Alloting Teacher for Period 3")
    print("Enter    4   for Alloting Teacher for Period 4")
    print("Enter    5   for Alloting Teacher for Period 5")
    print("Enter    6   for Alloting Teacher for Period 6 ")
    print("Enter    7   for Alloting Teacher for Period 7")
    print("Enter    8   for Alloting Teacher for Period 8")
    print("Enter    9   for geting list of all free Teachers Period wise")
    print("Enter   10   for Manually alloting Teachers for free period")
    print("Enter   11   for finding proxy Teachers for any subject")
    print("Enter   12   for complete teachers List with subjects taken")
    print("Enter   13   for displaying Absent teachers")
    print("Enter   14   for displaying Class time table")
    print("Enter   15   for displaying Class timetable with free classes")
    print("Enter   16   for displaying Class timetable with proxy teachers")
    
    val=int(input("\n <-------  Enter any  option --------->  "))

    
    if(val==1):
        t5.freebuffer1()
        t5.af1()
    if(val==2):
        t5.freebuffer1() 
        t5.af2()
    if(val==3):
        t5.freebuffer1()
        t5.af3()
    if(val==4):
        t5.freebuffer1()
        t5.af4()
    if(val==5):
        t5.freebuffer1()
        t5.af5()
    if(val==6):
        t5.freebuffer1()
        t5.af6()
    if(val==7):
        t5.freebuffer1()
        t5.af7()
    if(val==8):
        t5.freebuffer1()
        t5.af8()
    if(val==9):
        t5.freebuffer()# function just for displaying free teachers list
    if(val==10):
        print("Enter 1 for Manual assignment of teacher to Period 1")
        print("Enter 2 for Manual assignment of teacher to Period 2")
        print("Enter 3 for Manual assignment of teacher to  Period 3")
        print("Enter 4 for Manual assignment of teacher to  Period 4")
        print("Enter 5 for Manual assignment of teacher to  Period 5")
        print("Enter 6 for Manual assignment of teacher to  Period 6")
        print("Enter 7 for Manual assignment of teacher to  Period 7")
        print("Enter 8 for Manual assignment of teacher to  Period 8")
        opt=int(input("\nEnter period no to allot teacher------>"))
        if(opt== 1):
            t5.freebuffer1()
            t5.manual1()
        if(opt==2):
            t5.freebuffer1()
            t5.manual2()
        if(opt==3):
            t5.freebuffer1()
            t5.manual3()
        if(opt==4):
            t5.freebuffer1()
            t5.manual4()
        if(opt==5):
            t5.freebuffer1()
            t5.manual5()
        if(opt==6):
            t5.freebuffer1()
            t5.manual6()
        if(opt==7):
            t5.freebuffer1()
            t5.manual7()
        if(opt==8):
            t5.freebuffer1()
            t5.manual8()
    if(val==11):
        t5.sub()
    if(val==12):
        t5.showteachers()# FUNCTION FOR SHOWING LIST OF ALL TEACHERS
    if(val==13):
        if(absentteachers==[]):
            print("\nAll Teachers present Today")
        else:pass
        subindict=[]          # LIST OF SUBJECTS TAUGHT BY ABSENT TEACHERS
        for i in absentteachers:
            subindict=Time.td[i]
            print ("\n Absent teacher name is  ",i ,"and subject taken --> ",subindict[0])
    if(val==14):
        t5.displayclass()
    if(val==15):
        t5.newc()
    if(val==16):
        t5.absenttimetable()
    if(val==0):
        print ("\n\n**************************    Thanks for visiting our Timetable Portal      *******************************")
        break
    
       
       
'''t5.af1()
t5.af2()
t5.af3()
t5.af4()
t5.af5()
t5.af6()
t5.af7()
t5.af8()'''
        
