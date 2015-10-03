
filename = "binFileLine5"
filename2 = "binFileLine6"
fileOut = "temp"

binReader1 = open(filename, 'r')
binString1 = binReader1.read()

binReader2 = open(filename2, 'r')
binString2 = binReader2.read()

print("Length of " + filename + ": " + str(len(binString1)))
print("Length of " + filename2 + ": " + str(len(binString2)))
stream = ""
for i in range(0, len(binString1)):
    if i < len(binString2):
        if int(binString1[i]) == 1:
            if int(binString2[i]) == 1:
                stream += "0"
            else:
                stream += "1"
        else:
            stream += binString2[i]

#binString = bin(int(hexString, 16))[2:]
print(stream)

toWrite = open(fileOut, 'w')
toWrite.write(stream)