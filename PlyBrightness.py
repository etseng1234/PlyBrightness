import sys

def main(argsBright, argsContrast, argsFile, argsSave):
    changeInt = argsBright
    contrastInt = int(argsContrast)
    contrastFactor = (259 * (contrastInt + 255)) / (255 * (259 - contrastInt))
    file = open(argsFile, 'r')
    newfile = open(argsSave, 'w')
    newfile = open(argsSave, 'a')
    lines = file.readlines()
    for line in lines:
        if(len(line.split(' ')) > 5):
            linearr = line.split(' ')
            x = linearr[0]
            y = linearr[1]
            z = linearr[2]
            brightr = int(linearr[3]) + int(changeInt)
            brightg = int(linearr[4]) + int(changeInt)
            brightb = int(linearr[5]) + int(changeInt)
            r = int(round(checkValid(contrastFactor * (brightr - 128) + 128)))
            g = int(round(checkValid(contrastFactor * (brightg - 128) + 128)))
            b = int(round(checkValid(contrastFactor * (brightb - 128) + 128)))
            op = line[6]
            newline = str(x) + ' ' + str(y) +  ' ' + str(z) + ' ' + str(r) + ' ' + str(g) + ' ' + str(b) + ' ' + '255' + ' '
            newfile.write(newline + "\n")
        else:
            newfile.write(line)
    file.close()
    newfile.close()

def checkValid(brightness):
    if(brightness > 255):
        return 255
    elif(brightness < 0 ):
        return 0
    else:
        return brightness

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])