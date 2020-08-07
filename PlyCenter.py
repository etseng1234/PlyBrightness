import sys

def main(argsBright, argsContrast, argsFile, argsSave):
    maxx = 0
    maxy = 0
    minx = 0
    miny = 0
    minz = 0
    maxz = 0
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
            maxx = max(maxx, int(x))
            minx = min(minx, int(x))
            maxy = max(maxy, int(y))
            miny = min(miny, int(y))
            maxz = max(maxz, int(z))
            minz = min(minz, int(z))

    print(minx, maxx)
    print(miny, maxy)
    print(minz, maxz)

    for line in lines:
        if(len(line.split(' ')) > 5):
            linearr = line.split(' ')
            x = linearr[0]
            y = linearr[1]
            z = linearr[2]
            r = linearr[3]
            g = linearr[4]
            b = linearr[5]
            op = line[6]
            newline = str(x) + ' ' + str(y) +  ' ' + str(z) + ' ' + str(r) + ' ' + str(g) + ' ' + str(b) + ' ' + '255' + ' '
            newfile.write(newline + "\n")
        else:
            newfile.write(line)
    file.close()
    newfile.close()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])