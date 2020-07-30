import sys

def main(argsBright, argsFile, argsSave):
    changeInt = argsBright
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
            r = checkBright(int(linearr[3]) + int(changeInt))
            g = checkBright(int(linearr[4]) + int(changeInt))
            b = checkBright(int(linearr[5]) + int(changeInt))
            op = line[6]
            newline = str(x) + ' ' + str(y) +  ' ' + str(z) + ' ' + str(r) + ' ' + str(g) + ' ' + str(b) + ' ' + '255' + ' '
            newfile.write(newline + "\n")
        else:
            newfile.write(line)
    file.close()
    newfile.close()

def checkBright(brightness):
    if(brightness > 255):
        return 255
    else:
        return brightness

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])