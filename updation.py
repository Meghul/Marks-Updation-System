import os


def help(x):
    c = x.split(":")
    return int(c[-1])


list1 = []
stu_no = int(input("No. of Students: "))
for i in range(stu_no):
    n = input("Name: ")
    m = input("Marks: ")
    print()
    c = n + ":" + m
    list1.append(c)
list1.sort(key=help, reverse=True)
print(list1)
print()
print()

############################   LOOP STARTS HERE       ########################

while True:
    c = 0
    print("Operations :")
    print()
    print('''0.) Display the Student's Marks with Rank ''')
    print('''1.) Update and display the student Rank''')
    print('''2.) Display the specific student's Rank''')
    print('''3.) Clear the screen''')
    print()
    a = input("Operations: ")
    print()
    if a == "0":
        #        print("Name:Marks")
        print()
        for i in list1:
            c = c + 1
            print("Rank =", c)
            zz = i.split(":")

            print("        Name:", zz[0])
            print("        Marks:", zz[-1])
            print()


    #######################     UPDATION MARKS       ########################

    elif a == "1":
        n = input("Name: ")
        m = input("Marks: ")
        print()
        ap = n + ":" + m
        print("The updated list :")
        for j in list1:
            if n in j:
                del list1[c]
                list1.append(ap)
                list1.sort(key=help, reverse=True)
                break
            c = c + 1
        print()
        #    print(list1)
        print()
        rank = 1
        for x in list1:
            print("Rank:", rank)
            zz = x.split(":")
            print("        Name:", zz[0])
            print("        Marks:", zz[-1])
            print()
            rank = rank + 1

    elif a == "2":
        nm_rank = 1
        n = input("Enter Name: ")
        print()
        for i in list1:
            if n in i:
                zz = i.split(":")

                print("Name:", zz[0])
                print("        Marks:", zz[-1])
                print("        Rank:", nm_rank)
            nm_rank = nm_rank + 1
        print()
    elif a == "3":
        os.system('cls')