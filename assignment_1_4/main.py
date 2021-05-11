
Word = input("Type in your word: ")
String = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for C in range (0, 26):

    B1 = str(String[C])
    B2 = str(Word.count(String[C]))

    def Funk(string):
        return "'{}'".format(string)

    B3 = Funk(B1)
    print(B3 + " : " + B2)