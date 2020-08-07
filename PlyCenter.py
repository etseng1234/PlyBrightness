import sys

def main(argsFile, argsSave):
    maxx = -100000
    maxy = -100000
    maxz = -100000
    minx = 100000
    miny = 100000
    minz = 100000
    movex = 0
    movey = 0
    movez = 0

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

    movex = round((minx + maxx)/2)
    movey = round((miny + maxy)/2)
    movez = round((minz + maxz)/2)

    for line in lines:
        if(len(line.split(' ')) > 5):
            linearr = line.split(' ')
            x = int(linearr[0]) - movex
            y = int(linearr[1]) - movey
            z = int(linearr[2]) - movez
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
    main(sys.argv[1], sys.argv[2])