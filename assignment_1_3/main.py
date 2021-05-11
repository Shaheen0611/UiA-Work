

String1 = input("Type in your first word: ")
String2 = input("Type in your second word: ")
if String1 == String2:
    print("are equal")
else:
    print("are not equal")

if String1 in String2 or String2 in String1:
    print("is a substring")
else:
    print("is not a substring")
