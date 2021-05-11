def palindrome(String):
    reversed_string = String[::-1]
    status=1
    if(String!=reversed_string):
        status=0
    return status


String = input("Type in a string ")
print("You wrote:",String)
print((len(String)))

status = palindrome(String)
if(status):
    print("is a palindrome" )
else:
    print("is not a palindrome")


print(String[::-1])
