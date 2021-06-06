# HOMEWORK #4 Lists

myUniqueList = []
myLeftovers = []
Unique = True

print("Pirple.com Homework#4 LISTS")
Object = input("Enter new thing to add to the list:")


# Code for adding new things/objects to the list
def add_student():
    if Object in myUniqueList:
        print(False)
        global Unique
        Unique = False
    else:
        myUniqueList.append(Object)
        print(True)
        Unique = True


add_student()


# Code for adding rejected inputs into myLeftovers list
def rejects_list():
    if not Unique:
        myLeftovers.append(Object)
        print("Object already exists in myUniqueList, adding to myLeftovers list")
    else:
        print("Object has been added to myUniqueList")


rejects_list()

print("myUniqueList: ", myUniqueList)
print("myLeftovers:", myLeftovers)
