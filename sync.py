import tools as tools
import constants as constants
import settings as Setting
###
# This program synchronizes what is on the remarkable tablet to what is in the directory 
#
#
#
###
s = Setting.Settings()

def printOutDir():
    print(constants.outputDir)

def downloadRemarkable():
    print(tools.listDir('',s)[0])


if __name__ == "__main__":
    downloadRemarkable();

