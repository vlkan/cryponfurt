import hashlib

#a little pi number for encrypt and decrypt.
pi_numbers=[ 3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,
            6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,
            9,9,3,7,5,1,0,5,8,2,0,9,7,4,9,4,4,5,9,2,3,0,
            7,8,1,6,4,0,6,2,8,6,2,0,8,9,9,8,6,2,8,0,3,4,
            8,2,5,3,4,2,1,1,7,0,6,7,9,8,2,1,4,8,0,8,6,5,
            1,3,2,8,2,3,0,6,6,4,7,0,9,3,8,4,4,6,0,9,5,5,
            0,5,8,2,2,3,1,7,2,5,3,5,9,4,0,8,1,2,8,4,8,1,
            1,1,7,4,5,0,2,8,4,1,0,2,7,0,1,9,3,8,5,2,1,1,
            0,5,5,5,9,6,4,4,6,2,2,9,4,8,9,5,4,9,3,0,3,8,
            9,6,4,4,2,8,8,1,0,9,7,5,6,6,5,9,3,3,4,4,6,1,
            2,8,4,7,5,6,4,8,2,3,3,7,8,6,7,8,3,1,6,5,2,7,
            1,2,0,1,9,0,9,1,4,5,6,4,8,5,6,6,9,2,3,4,6,0,
            3,4,8,6,1,0,4,5,4,3,2,6,6,4,8,2,1,3,3,9,3,6,
            0,7,2,6,0,2,4,9,1,4,1,2,7,3,7,2,4,5,8,7,0,0,
            6,6,0,6,3,1,5,5,8,8,1,7,4,8,8,1,5,2,0,9,2,0,
            9,6,2,8,2,9,2,5,4,0,9,1,7,1,5,3,6,4,3,6,7,8,
            9,2,5,9,0,3,6,0,0,1,1,3,3,0,5,3,0,5,4,8,8,2,
            0,4,6,6,5,2,1,3,8,4,1,4,6,9,5,1,9,4,1,5,1,1,
            6,0,9,4,3,3,0,5,7,2,7,0,3,6,5,7,5,9,5,9,1,9,
            5,3,0,9,2,1,8,6,1,1,7,3,8,1,9,3,2,6,1,1,7,9,
            3,1,0,5,1,1,8,5,4,8,0,7,4,4,6,2,3,7,9,9,6,2,
            7,4,9,5,6,7,3,5,1,8,8,5,7,5,2,7,2,4,8,9,1,2,
            2,7,9,3,8,1,8,3,0,1,1,9,4,9,1,2,9,8,3,3,6,7,
            3,3,6,2,4,4,0,6,5,6,6,4,3,0,8,6,0,2,1,3,9,4]

def encrypt(text):

    irobot = hashlib.sha512(text.encode())
    foundation = "c257793861f9e834b0415dff04fb5c3d3eda379eb8aaee674f42df646a1dc7ad6b90c90e26af3cae0fb4f06202b9aecc6c7cded91670408a0a266988758169ab"

    # printing the equivalent hexadecimal value.
    #print(result.hexdigest())

    if (foundation == irobot.hexdigest()):
        print("\nIgniting the masses is something that gives man strength, but remember that people are unfaithful.")

    else:
        asimov = []
        length = len(text)

        #smash the word and add array.
        for i in range(length):
            asimov.append(text[i])
        print(str(asimov) + "   ENCODE VERSION...")

        for i in range(length):
            pindex = int(pi_numbers[i])

            # adding pi number and send new array.
            new = ord(asimov[i]) + pindex
            asimov[i] = new
        #print ascii and text version for crypto version
        print(str(asimov) + "   ASCII VERSION...")
        s = "".join([chr(c) for c in asimov])
        print(str(s) + "   CRYPTO VERSION..."+"\n")

def decrypt(text):

    irobot = hashlib.sha512(text.encode())
    empire = "d067505f26e5d46eb55d35f1539aff5a8cca00f1133a8a8f58a107a8a45b65738b25889e7d297322283132751b4e60241e2c5fe3d881f4d7c03c4469a7bab44f"

    if(empire == irobot.hexdigest()):
        print("\nThere is no flaw in the lie of the lover and diplomat.")
    else:
        my_list = []
        length = len(text)

        for i in range(length):
            my_list.append(text[i])
        print(str(my_list) + "   ENCODE VERSION...")

        for i in range(length):
            pindex = int(pi_numbers[i])

            new = ord(my_list[i]) - pindex
            my_list[i] = new

        print(str(my_list) + "   ASCII VERSION...")
        s = "".join([chr(c) for c in my_list])
        print(str(s) + "   DECODE VERSION..."+"\n")

#Isaac Asimov - "I'm not afraid of computers, but of their absence."
