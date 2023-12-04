from test import testCustomTypes
import random
import os

class bcolors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE ='\033[7m'
    INVISIBLE ='\033[8m'
    STRIKE ='\033[9m'
    class fg :
        Black='\033[30m'
        Red='\033[31m'
        Green='\033[32m'
        Orange='\033[33m'
        Blue='\033[34m'
        Purple='\033[35m'
        DarkCyan='\033[36m'
        Gray='\033[37m'
        DarkGray='\033[90m'
        PastelRed='\033[91m'
        LightGreen='\033[92m'
        Yellow='\033[93m'
        PastelBlue='\033[94m'
        Pink='\033[95m'
        Cyan='\033[96m'
        White='\033[97m'
    class bg :
        Black='\033[40m'
        Red='\033[41m'
        Green='\033[42m'
        Orange='\033[43m'
        Blue='\033[44m'
        Purple='\033[45m'
        DarkCyan='\033[46m'
        Gray='\033[47m'
        DarkGray='\033[100m'
        PastelRed='\033[101m'
        LightGreen='\033[102m'
        Yellow='\033[103m'
        PastelBlue='\033[104m'
        Pink='\033[105m'
        Cyan='\033[106m'
        White='\033[107m'

#delta corps priest 1 
title = '''
    ███        ▄████████    ▄████████     ███             ▄████████ ███    █▄   ▄█      ███     
▀█████████▄   ███    ███   ███    ███ ▀█████████▄        ███    ███ ███    ███ ███  ▀█████████▄ 
   ▀███▀▀██   ███    █▀    ███    █▀     ▀███▀▀██        ███    █▀  ███    ███ ███▌    ▀███▀▀██ 
    ███   ▀  ▄███▄▄▄       ███            ███   ▀        ███        ███    ███ ███▌     ███   ▀ 
    ███     ▀▀███▀▀▀     ▀███████████     ███          ▀███████████ ███    ███ ███▌     ███     
    ███       ███    █▄           ███     ███                   ███ ███    ███ ███      ███     
    ███       ███    ███    ▄█    ███     ███             ▄█    ███ ███    ███ ███      ███     
   ▄████▀     ██████████  ▄████████▀     ▄████▀         ▄████████▀  ████████▀  █▀      ▄████▀ '''
   
#
version= '''
         __   _____             ___  _ _     _____ _         _   _           _       _       
        /  | |  _  |           / _ \| | |   |  ___(_)       | | | |         | |     | |      
__   __ `| | | |/' |  ______  / /_\ \ | |__ | |__  _ _ __   | | | |_ __   __| | __ _| |_ ___ 
\ \ / /  | | |  /| | |______| |  _  | | '_ \|  __|| | '_ \  | | | | '_ \ / _` |/ _` | __/ _ \\
 \ V /  _| |_\ |_/ /          | | | | | |_) | |___| | | | | | |_| | |_) | (_| | (_| | ||  __/
  \_/   \___(_)___/           \_| |_/_|_.__/\____/|_|_| |_|  \___/| .__/ \__,_|\__,_|\__\___|
                                                                  | |                        
                                                                  |_|                        
'''

#-----UTILITY FUNCTIONS-----
def clearSc():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def difList(L1 : list, L2 : list) -> (bool, list, list):
    """
    Takes two list in entry
    Return a 3-uple (bool, list, list)
    The bool is if the two list are equivalent (contains the same elements even if in different order)
    The first list returned contains the elements of L1 not contained in L2
    The second list returned contains the elements of L2 not contained in L1
    If bool is True, the two list are empty
    """
    lenL1, lenL2 = len(L1), len(L2)
    isListEq = lenL1 == lenL2
    L1Additions, L2Additions = [], []
    for e in L1:
        if not e in L2:
            L1Additions.append(e)
            isListEq = False
    for e in L2:
        if not e in L1:
            L2Additions.append(e)
            isListEq = False
    return (isListEq, L1Additions, L2Additions)

def basicTestPrint(name : str, res : bool) -> None:
    print(f"{name:<30} : {bcolors.BOLD}", end = "")
    print((f"{bcolors.fg.Green}[OK]" if res else f"{bcolors.fg.Red}-+-+-+-+-+-[NO]"), end = "")
    print(f"{bcolors.RESET}")

def test(name : str, got, expected, exactlyEqual : bool = True) -> bool:
    notEnumerable = (int, float, bool, complex, str, type(None)) #I know str is enumerable
    Enumerable = (list, tuple, range, dict, set)

    isGotEnumerable = type(got) in Enumerable
    isGotNotEnumerable = type(got) in notEnumerable
    isExpectedEnumerable = type(expected) in Enumerable
    isExpectedNotEnumerable = type(expected) in notEnumerable

    if isGotEnumerable and isExpectedEnumerable:
        if exactlyEqual:
            res = got == expected
            basicTestPrint(name, res)
            if not res:
                gotLen = len(got)
                expectedLen = len(expected)
                typegot = type(got)
                got = got if gotLen < 20 else (str(got[:20])[:-1]+", ...]")
                expected = expected if expectedLen < 20 else (str(expected[:20])[:-1]+", ...]")
                print(f"\tGot ({bcolors.fg.Cyan}{str(typegot)[8:-2]}{bcolors.RESET}):\t{got}\n\tExpected ({bcolors.fg.Cyan}{str(type(expected))[8:-2]}{bcolors.RESET}):\t{expected}")
                print(f"{bcolors.BOLD}{bcolors.fg.Red}", end = "")
                if type(got) != type(expected):
                    print(f"\tGot and Expected are not of the same type")
                if gotLen != expectedLen:
                    print(f"\tlen(Got)={gotLen} is different than len(Expected)={expectedLen}")
                print(f"{bcolors.RESET}")
            return res
        else:
            listDif = difList(got, expected)
            res = listDif[0] and type(got) == type(expected)
            basicTestPrint(name, res)
            if not res:
                gotLen = len(got)
                expectedLen = len(expected)
                typegot = type(got)
                got = got if gotLen < 20 else (str(got[:20])[:-1]+", ...]")
                expected = expected if expectedLen < 20 else (str(expected[:20])[:-1]+", ...]")
                print(f"\tGot ({bcolors.fg.Cyan}{str(typegot)[8:-2]}{bcolors.RESET}) and Expected ({bcolors.fg.Cyan}{str(type(expected))[8:-2]}{bcolors.RESET}) are not equivalents")
                print(f"\tGot: {got}\n\tExpected: {expected}")
                print(f"{bcolors.BOLD}{bcolors.fg.Red}", end = "")
                if typegot != type(expected):
                    print(f"\tGot and Expected are not of the same type")
                if gotLen != expectedLen:
                    print(f"\tlen(Got)={gotLen} is different than len(Expected)={expectedLen}")
                if listDif[2] != []:
                    print(f"\tGot is missing values: {listDif[2]}")
                if listDif[1] != []:
                    print(f"\tGot have unwanted values: {listDif[1]}")
                print(f"{bcolors.RESET}")
            return res
    
    if isGotNotEnumerable and isExpectedEnumerable:
        res = got in expected
        basicTestPrint(name, res)
        if not res:
            print(f"\tGot ({bcolors.fg.Cyan}{str(type(got))[8:-2]}{bcolors.RESET}): {got} is not in {bcolors.fg.Cyan}{str(type(expected))[8:-2]}{bcolors.RESET} Expected : {expected}")
        return res

    if isGotNotEnumerable and isExpectedNotEnumerable:
        res = got == expected
        basicTestPrint(name, res)
        if not res:
            print(f"\tGot ({bcolors.fg.Cyan}{str(type(got))[8:-2]}{bcolors.RESET}): {got}\n\tExpected ({bcolors.fg.Cyan}{str(type(expected))[8:-2]}{bcolors.RESET}): {expected}")
            print(f"{bcolors.BOLD}{bcolors.fg.Red}", end = "")
            if type(got) != type(expected):
                print(f"\tGot and Expected are not of the same type")
            print(f"{bcolors.RESET}")
        return res
    
    if isGotEnumerable and isExpectedNotEnumerable: #How
        basicTestPrint(name, False)
        print(f"\tHow did you manage to do that")
        print(f"\tGot ({bcolors.fg.Cyan}{str(type(got))[8:-2]}{bcolors.RESET}): {got}\n\tExpected ({bcolors.fg.Cyan}{str(type(expected))[8:-2]}{bcolors.RESET}): {expected}\n")
        return False
    
    #got and or expected are custom types
    return testCustomTypes(name, got, expected, exactlyEqual)

def loadFileInList(filename : str) -> list:
    res = []
    with open (filename, "r") as f:
        for x in f:
            res.append(x.strip())
        f.close()
    return res

def get_random_words(filename : str, max : int, fileres : str, seed:int, size = 0) -> (list, int, float):
    random.seed(seed)
    words = []
    leng = 0
    with open(filename, "r") as word_file, open(fileres, "w") as re_file:        
        for w in range(max):
            if(random.randint(0,1) == 0):
                wor = word_file.readline().strip()
                if(wor not in words and (size == 0 or len(wor) == size)):
                    words.append(wor)
                    leng += len(wor)
                    re_file.write(wor+"\n")
        word_file.close()
        re_file.close()
    
    words.sort()
    l = len(words)
    return (words, l, leng/l)

def printDetect(fil):
    fi = open(fil)
    c = fi.readline()
    l = 1
    while(c):
        if ("print" in c):
            print(f"\n{bcolors.BOLD}{bcolors.fg.Red}!!! PRINT DETECTED IN FILE !!!\nLine : {l}\n{c}{bcolors.RESET}")
            return True
        c = fi.readline()
        l += 1
    return False
