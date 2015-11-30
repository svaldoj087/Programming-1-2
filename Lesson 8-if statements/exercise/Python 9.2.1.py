# Jesus
# period 4
#11/23/15

#9.2.1
#this will name and grade level, and print out a greeding

name=input("What is your name? ")
grade = int(input("What grade are you in? "))

if grade ==9:
    print ("Hello, %s, welcome to your first year of high school." % (name))
elif grade ==10:
    print ("I hopeto see you in class %s." % (name))
elif grade==11:
    print("You are almost a senior, %s." % (name))
elif grade==12:
    print ("Whoo hoo last year I have to deal with you, %s." % (name))
else:
    print("Story invalid grade.")
        
