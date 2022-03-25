import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

cipher = alphabet.copy()

print()
seed = int(input("Enter any integer (Will help generate key randomly):"))

random.seed(seed)
random.shuffle(cipher)

print("plaintext = ", end = "")
print(alphabet)
print("encrypted = ", end = "")
print(cipher)

#encryption step

message = input("Enter message to be encrypted (Use only lowercase letters):")
encrypted = ""

for x in range(0, len(message)):
    if message[x] == " ":
        encrypted = encrypted + " "
    else:
        for y in range(0,26):
            if message[x] == alphabet[y]:
                encrypted = encrypted + cipher[y]


print("\nplaintext message = " + message)
print("encrypted message = " + encrypted + "\n\n")

#decryption step

encMessage = input("Enter message to be decrypted (Use only lowercase letters):")
decrypted = ""

for x in range(0, len(encMessage)):
    if encMessage[x] == " ":
        decrypted = decrypted + " "
    else:
        for y in range(0,26):
            if encMessage[x] == cipher[y]:
                decrypted = decrypted + alphabet[y]


print("\nencrypted message = " + encMessage)
print("plaintext message = " + decrypted + "\n")


#ciphertext attack portion of assignment

#enter name of your file to be encrypted
with open("new1.txt", "r+") as file1:
    textfile=file1.read()

    encryptedfile= ""

    for x in range(0, len(textfile)):
        if textfile[x] == " ":
            encryptedfile = encryptedfile + " "
        else:
            for y in range(0,26):
                if textfile[x] == alphabet[y]:
                    encryptedfile = encryptedfile + cipher[y]

    frequency = list(range(26))
    for x in range(0,26):
        frequency[x]=0

    for x in range(0,len(encryptedfile)):
        for y in range(0,26):
            if encryptedfile[x]==alphabet[y]:
                frequency[y] = frequency[y]+1

    #open and create file
    newfile=open("output.txt","w+")

    newfile.write(encryptedfile)

    freqpercent=[]
    for number in frequency:
        freqpercent.append(number/len(textfile))

    def sort_zip(list1, list2):
        zippair = zip(list2, list1)
        z = [x for _, x in sorted(zippair)]
        return z


    format_list=sort_zip(alphabet,freqpercent)

    freqpercent.sort()

    output = "\n".join("{} {}".format(x, y) for x, y in zip(format_list, freqpercent))

    print(output)
    pass
