
filename = "answerToBin"
fileOut = "text"

hexReader = open(filename, 'r')
hexString = hexReader.read()

text = int(hexString, 2)

print(text)

toWrite = open(fileOut, 'w')
toWrite.write(text)
