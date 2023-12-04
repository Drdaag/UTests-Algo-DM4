##############################################################################################################################################
############################################################### - PARAMETERS - ###############################################################

#Your file. Leave blank to use the autofind file feature
myfile = ""

##############################################################################################################################################

import os
from time import time
import random

from algo_py import graph, queue

os.system('')

def autodetect():
    arr = os.listdir()
    for f in arr:
        if(len(f) >= 15 and f[-12:-1]+'y' == "_doublets.py"): #_prefixtrees.py
            return str(f)
    return ""

if myfile == "":
    tmp = autodetect()
    if (tmp == ""):
        print(f"NO FILE FOUND\n")
        exit()
    else :
        myfile = tmp
            

# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader
mycode = SourceFileLoader('mycode', myfile).load_module()

# # My handout
# myfile = 
# Load module. Same result as "import mycode"
from testSuiteUtils import *

#Implement it if DM uses custom types like Trees...
def testCustomTypes(name : str, got, expected, exactlyEqual : bool = True) -> bool:
    if type(got) == graph.Graph:
        got1 = got.labels
        got2 = got.order
        got3 = got.directed
        got4 = got.adjlists
    if type(expected) == graph.Graph:
        expected1 = expected.labels
        expected2 = expected.order
        expected3 = expected.directed
        expected4 = expected.adjlists
    from testSuiteUtils import test, bcolors
    
    print(f"{name:<30} : {bcolors.BOLD}")
    res = test("\t- labels", got1, expected1, exactlyEqual) and test("\t- order", got2, expected2, exactlyEqual) and test("\t- directed", got3, expected3, exactlyEqual) and test("\t- adjlists", got4, expected4, exactlyEqual)
    print(f"{bcolors.RESET}")
    
    return res

def tolabel(G, L):
    res = []
    for i in L:
        res.append(G.labels[i])
    return res


if __name__ == "__main__":
    
    clearSc()
    
    print(title)
    print(f"{bcolors.fg.Cyan}{version}{bcolors.RESET}")
    
    print(f"{bcolors.fg.PastelRed}PLEASE CHOOSE A CONFIG :{bcolors.RESET}\n")
    print("1 - All normal tests")
    print("2 - All normal tests + Random")
    print("3 - All normal tests + Random + Huge")
    print()
    print(f"{bcolors.fg.DarkGray}PS : Nothing = Same as set in the file{bcolors.RESET}")
    chose = input(">>>  ")
    if chose == "":
        chose = 0
    ichose = int(chose)
    testRandom = ichose >= 2
    testHuge = ichose >= 3
    
    if testRandom:
        tmpseed = input("SEED ? (press ENTER for random) ")
        if(tmpseed != ""):
            seed = int(tmpseed)
        else:
            seed = random.randint(0,100000)
    
    clearSc()
    print(title)
    print(f"{bcolors.fg.Cyan}{version}{bcolors.RESET}")
    
    if(printDetect(myfile)):
        a = input()
        exit()

    print(f"\n{bcolors.BOLD}{bcolors.fg.Yellow}########### FIXED TEST ##########{bcolors.RESET}")
        
    print("\n-----------buildgraph-----------\n")
    
    got = mycode.buildgraph("lexicons/lex_some.txt", 3)
    expected = graph.load("graphs\some3.gra")
    test("buildgraph_some3", got, expected)
    
    got = mycode.buildgraph("lexicons/lex_some.txt", 4)
    expected = graph.load("graphs\some4.gra")
    test("buildgraph_some4", got, expected)
    
    got = mycode.buildgraph("lexicons/lex_more.txt", 3)
    expected = graph.load("graphs\more3.gra")
    test("buildgraph_more3", got, expected)
    
    got = mycode.buildgraph("lexicons/lex_more.txt", 4)
    expected = graph.load("graphs\more4.gra")
    test("buildgraph_more4", got, expected)

    G3 = mycode.buildgraph("lexicons/lex_some.txt", 3)
    G4 = mycode.buildgraph("lexicons/lex_some.txt", 4)
    G3m = mycode.buildgraph("lexicons/lex_more.txt", 3)
    G4m = mycode.buildgraph("lexicons/lex_more.txt", 4)

    print("\n-----------mostconnected-----------\n")
    
    got = mycode.mostconnected(G3)
    expected = ['oat', 'sat']
    test("mostconnected_some3", got, expected)
    
    got = mycode.mostconnected(G4)
    expected = ['ford', 'fork']
    test("mostconnected_some4", got, expected)
    
    got = mycode.mostconnected(G3m)
    expected = ['sat']
    test("mostconnected_more3", got, expected)
    
    got = mycode.mostconnected(G4m)
    expected = ['cord', 'cork']
    test("mostconnected_more4", got, expected)
    
    print("\n-----------ischain-----------\n")
    
    got = mycode.ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'man'])
    expected = True
    test("mostconnected_some3_True", got, expected)
    
    got = mycode.ischain(G3, ['man', 'mat', 'sat', 'sit', 'pit', 'pig'])
    expected = False
    test("mostconnected_some3_False1", got, expected)
    
    got = mycode.ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'rat', 'oat', 'mat', 'man'])
    expected = False
    test("mostconnected_some3_False2", got, expected)
    
    got = mycode.ischain(G4, ['fore', 'fork', 'cork', 'work', 'word', 'wold', 'weld'])
    expected = True
    test("mostconnected_some4_True", got, expected)
    
    got = mycode.ischain(G4, ['fore', 'fork', 'work', 'feur', 'word', 'wold', 'weld'])
    expected = False
    test("mostconnected_some4_False", got, expected)
    
    got = mycode.ischain(G3m, ['rat', 'sat', 'set', 'wet', 'bet', 'bey', 'buy'])
    expected = True
    test("mostconnected_more3_True", got, expected)
    
    got = mycode.ischain(G3m, ['rat', 'sat', 'set', 'wet', 'bet', 'bey', 'bet'])
    expected = False
    test("mostconnected_more3_False", got, expected)
    
    got = mycode.ischain(G4m, ['poor', 'boor', 'book', 'cook', 'rook'])
    expected = True
    test("mostconnected_more4_True", got, expected)
    
    got = mycode.ischain(G4m, ['poor', 'boor', 'book','rick', 'cook', 'rook'])
    expected = False
    test("mostconnected_more4_False", got, expected)

    
    print("\n-----------alldoublets-----------\n")
    
    got = mycode.alldoublets(G3, "pen")
    expected = ['eel', 'een', 'ell', 'ilk', 'ill', 'ink', 'pie', 'pig', 'pin', 'pit']
    test("alldoublets_some3_pen", got, expected, False)
    
    got = mycode.alldoublets(G4, "ford")
    expected = ['food', 'fool', 'foot', 'fort', 'fore', 'fire', 'five', 'fork', 'cork', 'work', 'word', 'wold', 'weld', 'weed', 'feed', 'fled', 'flea', 'flee', 'flew', 'free', 'tree', 'wood', 'foul', 'four']
    test("alldoublets_some3_ford", got, expected, False)
    
    got = mycode.alldoublets(G3m, "set")
    expected = ['bet', 'bey', 'buy', 'bud', 'bid', 'aid', 'ail', 'aim', 'air', 'fir', 'far', 'ear', 'err', 'ere', 'ore', 'one', 'mar', 'man', 'mat', 'oat', 'oak', 'oar', 'sar', 'sat', 'rat', 'rot', 'hot', 'sot', 'sit', 'pit', 'pie', 'pig', 'pin', 'pen', 'een', 'eel', 'ell', 'all', 'ill', 'ilk', 'ink', 'elm', 'roe', 'rye', 'say', 'sty', 'opt', 'apt', 'ape', 'arm', 'ark', 'ask', 'ass', 'dey', 'dry', 'wet', 'sea', 'tea']
    test("alldoublets_more3_set", got, expected, False)
    
    got = mycode.alldoublets(G4m, "fool")
    expected = ['cool', 'cook', 'book', 'boom', 'boor', 'boot', 'foot', 'food', 'ford', 'cord', 'card', 'curd', 'ward', 'wald', 'weld', 'weed', 'feed', 'fled', 'flea', 'flee', 'flew', 'free', 'tree', 'wold', 'cold', 'coed', 'wolf', 'wood', 'wool', 'word', 'lord', 'wore', 'core', 'cork', 'bork', 'dork', 'fork', 'fore', 'fire', 'five', 'form', 'corm', 'corn', 'coin', 'chin', 'worn', 'work', 'pork', 'york', 'worm', 'warm', 'fort', 'cote', 'note', 'nose', 'poor', 'rook', 'rock', 'rick', 'rich', 'foul', 'four']
    test("alldoublets_more4_fool", got, expected, False)
    
    got = mycode.alldoublets(G4m, "amongus")
    expected = []
    test("alldoublets_more4_amongus", got, expected,False)
    
    ##############################################################
    # --------------------------WARNING--------------------------#
    ##############################################################
    print("\n"*2)
    print("-----------------------------------")
    print(f"|            {bcolors.fg.Yellow}! WARNING !{bcolors.RESET}          |")
    print("|  THE FOLLOWING  FUCNTIONS WILL  |")
    print("|    BE TESTED WITH SOME BEFORE   |")
    print("|   (so be sure that they work)   |")
    print("-----------------------------------")
    
    print("\n-----------nosolution-----------\n")

    tmp = mycode.nosolution(G3)
    got = tmp[0] not in mycode.alldoublets(G3, tmp[1])
    test("nosolution_some3", got, True)
    
    got = mycode.nosolution(G4)
    expected = (None, None)
    test("nosolution_some4", got, expected)
    
    tmp = mycode.nosolution(G3m)
    got = tmp[0] not in mycode.alldoublets(G3, tmp[1])
    test("nosolution_more3", got, True)
    
    got = mycode.nosolution(G4m)
    expected = (None, None)
    test("nosolution_more4", got, expected)
    
    
    print("\n-----------ladder-----------\n")

    got = mycode.ladder(G3, "ape", "man")
    expected = ['ape', 'apt', 'opt', 'oat', 'mat', 'man']
    test("ladder_some3", got, expected)
    
    got = mycode.ladder(G3, "man", "pig")
    expected = []
    test("ladder_some3_void", got, expected)
    
    got = mycode.ladder(G4, "work", "food")
    expected = ['work', 'fork', 'ford', 'food']
    test("ladder_some4", got, expected)
    
    got = mycode.ladder(G3m, "ape", "man")
    expected = ['ape', 'apt', 'opt', 'oat', 'mat', 'man']
    test("ladder_more3", got, expected)
    
    got = mycode.ladder(G4m, "wolf", "flea")
    expected = ['wolf', 'wold', 'weld', 'weed', 'feed', 'fled', 'flea']
    test("ladder_more4", got, expected)

    print("\n-----------mostdifficult-----------\n")

    tmp = mycode.mostdifficult(G3)
    got = mycode.ladder(G3, tmp[0], tmp[1]) != []
    test("mostdifficult_some3", [got,tmp[2]], [True, 10])
    
    tmp = mycode.mostdifficult(G4)
    got = mycode.ladder(G4, tmp[0], tmp[1]) != []
    test("mostdifficult_some4", [got,tmp[2]], [True, 13])
    
    tmp = mycode.mostdifficult(G3m)
    got = mycode.ladder(G3m, tmp[0], tmp[1]) != []
    test("mostdifficult_more3", [got,tmp[2]], [True, 14])
    
    tmp = mycode.mostdifficult(G4m)
    got = mycode.ladder(G4m, tmp[0], tmp[1]) != []
    test("mostdifficult_more4", [got,tmp[2]], [True, 16])

    if(not testRandom and not testHuge):
        exit()
    
    # ------------------------RANDOM TEST-------------------------#
    print(f"\n{bcolors.BOLD}{bcolors.fg.DarkCyan}########### RANDOM TEST ##########{bcolors.RESET}")

    print("We will run your function with random paramters") 
    print("It will take some data randomly from provided files") 
    print("(please keep in mind that it will not test everything)") 
    print("(way too complicated + no time + L + ratio)")
    print("Seed:",seed)
    print()
    
    w, leng, _ = get_random_words("lexicons/lex_all.txt", 300, "testSuitetmp.txt", seed, 3)
    randGraph = mycode.buildgraph("testSuitetmp.txt", 3)
    test("random_buildgraph_300", randGraph.labels, w, True)
    
    tmp = mycode.nosolution(randGraph)
    if(tmp[0] != None):
        got = tmp[0] not in mycode.alldoublets(randGraph, tmp[1])
        test("random_nosolution_300", got, True)
    else:
        test("random_nosolution_300", tmp, (None, None))
    
    w, leng, _ = get_random_words("lexicons/lex_all.txt", 500, "testSuitetmp.txt", seed, 5)
    randGraph = mycode.buildgraph("testSuitetmp.txt", 5)
    test("random_buildgraph_500", randGraph.labels, w, True)
    
    tmp = mycode.nosolution(randGraph)
    if(tmp[0] != None):
        got = tmp[0] not in mycode.alldoublets(randGraph, tmp[1])
        test("random_nosolution_500", got, True)
    else:
        test("random_nosolution_500", tmp, (None, None))
        
    os.remove("testSuitetmp.txt")
    
    if(not testHuge):
        exit()
        
    # ------------------------HUGE TEST-------------------------#
    print(f"\n{bcolors.BOLD}{bcolors.fg.Red}########### HUGE TEST ##########{bcolors.RESET}")
            
    print("We will use the lex all, that's all folks for today") 
    print("You WANT SOMETHING ELSE, GO COOK YOURSELF") 
    print()
    
    allg = mycode.buildgraph("lexicons/lex_all.txt", 5)

    expected = graph.load("graphs\lex_all.gra")
    test("buildgraph_all", allg, expected)
    
    got = mycode.mostconnected(allg)
    expected = ['share']
    test("mostconnected_all", got, expected)
    
    got = mycode.ischain(allg, ['shave', 'shape', 'shame', 'shake'])
    expected = True
    test("mostconnected_all_True", got, expected)
    
    got = mycode.alldoublets(allg, "amuse")
    expected = ['abuse', 'abase', 'abash', 'abate', 'agate', 'agape']
    test("alldoublets_all_amuse", got, expected, False)
    
    tmp = mycode.nosolution(allg)
    got = tmp[0] not in mycode.alldoublets(G3, tmp[1])
    test("nosolution_all", got, True)
    
    got = mycode.ladder(allg, "snake", "angel")
    expected = []
    test("ladder_all_empty", got, expected)
    
    got = mycode.ladder(allg, "snake", "quilt")
    expected = ['snake', 'slake', 'flake', 'flare', 'glare', 'glade', 'glide', 'guide', 'guile', 'guilt', 'quilt']
    test("ladder_all_quilt", got, expected)
    
    
    tmp = mycode.mostdifficult(allg)
    got = mycode.ladder(allg, tmp[0], tmp[1]) != []
    test("mostdifficult_all", [got,tmp[2]], [True, 38])