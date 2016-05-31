import os, sys, shutil

def main():
    #execution code here
    arguements = sys.argv[1:len(sys.argv)]
    path = ''

    create = checkCreate(arguements)
    if create:

        if len(arguements)  <=2:
            simplifyMain(arguements)
    else:
        if checkIfRelative(arguements[0]):
            path = os.path.abspath(arguements[0])
        else:
            path = arguements[0]
        lines = readFile(path)
        linestoprint = []
        for line in lines:
            arguements[0] = line
            linestoprint.append( simplifyMain(arguements))

        if checkIfRelative(arguements[1]):
            writepath = os.path.join(os.getcwd(),arguements[1])
        else:
            writepath = arguements[1]
        writeFile(linestoprint, writepath)



def simplifyMain(arguements):
    print(str(arguements))
    if checkCreate(arguements):
        if checkIfRelative(arguements[0]):
            if not checkPath(arguements[0], True):

                return makePath(arguements[0], True)

            else:

                print('Folder already exists.')
        else:
            if not checkPath(arguements[0], False):

                return makePath(arguements[0], False)
            else:

                print('Folder already exists.')
    else:
        if checkIfRelative(arguements[0]):
            if checkPath(arguements[0], True):

                print((os.getcwd()+arguements[0]))
                return (os.getcwd()+arguements[0])
            else:

                print('Folder Doesn\'t exist.')
        else:
            if checkPath(arguements[0], False):
                print(arguements[0])

                return arguements[0]
            else:

                print('Folder doesn\'t exist.')


def checkPath(folder , dir):
    if dir :
        path = (os.getcwd()+folder)

        if os.path.isdir(path):
            return True
        else:
            print('no such directory present')
            return False
    else:

        if os.path.isdir(folder):
            return True
        else:
            print('no such directory present')
            return False


def makePath(folder, dir):
    pieces = folder.split('/')

    if dir:
        workingdir =os.getcwd()+folder
        os.chdir(os.getcwd())
        if not os.path.isdir(workingdir):
            os.makedirs(workingdir)
            print('making folder(s)')
    else:
        workingdir = folder
        os.chdir(os.getcwd())
        if not os.path.isdir(folder):
            os.makedirs(folder)
            print('making folder(s)')


    os.chdir(workingdir)

    return workingdir

def readFile(filepath):
    with open(filepath) as file:
        contents = file.readlines()
        for line in contents:
           line.rstrip('/n')

    return contents

def writeFile(lines, writepath):
    if os.path.isfile(writepath):
        index = writepath.rindex('.')
        writepath = writepath[:index]+'1'+writepath[index:]
        filetowrite = open(writepath, 'w')
    else:
        filetowrite = open(writepath, 'w')

    filetowrite.writelines(lines)
    filetowrite.close()
    return writepath

def checkCreate(args):

    for arg in args:

        if arg == '-create':
            return True


    return False

def checkFile(path):
    if os.path.isfile(path):
        if path[path.rindex('.'):] == '.txt':
            return True
        else:
            return False
    else:
        print('Not a file')
        return None

def checkIfRelative(input):
    if ':' in input:
        return False
    else:
        return True


main()




