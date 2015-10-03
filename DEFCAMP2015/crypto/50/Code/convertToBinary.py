
filename = "hexFile"
fileOut = "binFileLine6"

hexReader = open(filename, 'r')
hexString = hexReader.read()

binString = bin(int(hexString, 16))[2:]

print(binString)

toWrite = open(fileOut, 'w')
toWrite.write(binString)