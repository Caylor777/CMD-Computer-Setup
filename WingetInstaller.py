def fillProgramDictonary():
    with open(__file__.removesuffix("WingetInstaller.py") + "programs.txt") as inp:
        programsList = inp.read().splitlines()
    for i in programsList:
        programDictonary[i.split(" : ")[0]] = i.split(" : ")[1]
def fillinstallPending():
    for i in programDictonary:
        userInput = input(f"Do you wish to install \"{i}\": ")
        if userInput == "y":
            installPending.append(programDictonary[i])
        elif userInput == "n":
            pass
        else:
            print("Error: incorrect value entered")
            return
def installPrograms():
    for i in installPending:
        os.system(f"winget install {i}")
import os
programDictonary = {}
installPending = []
fillProgramDictonary()
fillinstallPending()
installPrograms()