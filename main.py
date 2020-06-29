#    useded for string function
import string
#    needed for random function
import random

if __name__ == "__main__":

    #   give ascii lowercase character from a-z sequentially
    asciiLowercase = string.ascii_lowercase
    #   print(asciiLowercase)

    #   give ascii uppercase character from a-z sequentially
    asciiUppercase = string.ascii_uppercase
    #   print(asciiUppercase)

    # give ascii digits from 1-9-0 sequentially
    asciiDigits = string.digits
    #   print(asciiDigits)

    # give ascii punctuation
    asciiPunctuation = string.punctuation
    #   print(asciiPunctuation)

    # give ascci lowercase + uppercase + digits + punctuation and make a group
    asciiPrintable = string.printable
    #   print(asciiPrintable)

    #   ask user for password length
    passwordLength = int(input("Enter Your Password Length: "))

    emptyString = []  # take an empty string

    #   add ascii lowercase elements to emptyString
    emptyString.extend(list(asciiLowercase))
    #   add ascii uppercase elements to emptyString
    emptyString.extend(list(asciiUppercase))
    #   add ascii digits elements to emptyString
    emptyString.extend(list(asciiDigits))
    #   add ascii punctuation elements to emptyString
    emptyString.extend(list(asciiPunctuation))

    #   print emptyString that has lowercase + uppercase + digits + punctuation elements
    #   print(emptyString)

    print("Your Password Is: ")

    #   method 1
    #   random.shuffle(emptyString) #   shuffle elements of emptyString
    #   print(emptyString)  #   prints random string that is shuffled
    #   print("".join(emptyString[0:passwordLength])) #   print random string according from emptyString that starts from length 0 to passwordLength

    #   method 2
    #   print random string according from emptyString that starts from length 0 to passwordLength
    #   join function join the elements with given delimeters
    print("".join(random.sample(emptyString, passwordLength)))
