# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1761197
# Date: 2019/11/29

fail=0
passes=0
defer=0
count_exclude,count_progress,count_trailer,count_retriever=0,0,0,0
overall = 0
print("\n~~~~~~~~~~~~~~~Welcome to staff version~~~~~~~~~~~~~~~\n")
def start():
    global selection
    while True:    
        selection=input("Press 'S' to start the progarm.\nPress 'Q' to execute the program.\n\n")
        if selection=='s' or selection=='S':
            inputs()
        elif selection=='q' or selection=="Q":
            execute()
        else:
            print("Invalid selection")
            continue
def inputs():
    global fail,passes,defer
    try:
        passes=int(input("\nEnter your passed credits:"))
        checker(passes) #checker functaion has a parameter and it assign to vallue.
        fail=int(input("\nEnter your failed credits:"))
        checker(fail)
        defer=int(input("\nEnter your defer credits:"))
        checker(defer)
    except:
        print("\n~~~~~~~~~~~~Invalid input,integers required~~~~~~~~~~~~\n")
        inputs()
    logic()
def checker(value):#check the conditions,if pass or fail or defer not in a range and these inputs not modulus by 20,if value print range error and restart the program.
    if value>120 or value<0 or value%20!=0:
        print("\n~~~~~~~~~~~~Range error~~~~~~~~~~~~\n")
        inputs()
def logic():
    global fail,passes,defer,count_exclude,count_progress,count_trailer,count_retriever,overall
    if passes+fail+defer==120:
        if passes<=40 and fail>=80:
                    print("\n.....The student progression outcome is Excluded.....\n")
                    count_exclude+=1
        elif passes==120:
                    print("\n.....The student progression outcome is Progress.....\n")
                    count_progress+=1
        elif passes==100:
                    print("\n.....The stdent progression outcome is Do not progress Module trailer.....\n")
                    count_trailer+=1
        elif passes<=80 and fail<=60:
                    print("\n.....The student progression outcome is Do not progress Module retriever.....\n")
                    count_retriever+=1
        overall+=1
    else:
        print("\n~~~~~~~~Total incorrect~~~~~~~~\n")
    start()
def execute():
    global count_exclude,count_progress,count_trailer,count_retriever
    print("\n~~~~~~~~~~~~Vertical Histogram~~~~~~~~~~~~\n")
    print("\n~~~~~~~~~Overall Total = ",overall,"~~~~~~~~\n")
    print("   Pass  ","Retriever","Trailer","Exclude  ")
    while count_exclude + count_progress + count_trailer + count_retriever != 0:
        if count_progress!=0:
            print("    *\t" , end=' ')
            count_progress-=1
        else:
            print("     \t",end='')
        if count_retriever!=0:
            print("    *\t",end=' ')
            count_retriever-=1
        else:
            print("     \t" ,end='')
        if count_trailer!=0:
            print("    *\t",end=' ')
            count_trailer-=1
        else:
            print("     \t",end='')
        if count_exclude!=0:
            print("    *\t",end=' ')
            count_exclude-=1
        else:
            print("     \t",end='')
        print()    
    exit()



start() #call the function for the start the program.
