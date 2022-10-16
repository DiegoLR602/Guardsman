from parser import parseLog
from post_to_database import input_dictionary, post_to_database
import sys

def main():
    n = len(sys.argv)
    if(n != 1):
        post_to_database(parseLog(sys.argv[1]))
    else:
        post_to_database(parseLog())

if(__name__ == "__main__"):
    main()
