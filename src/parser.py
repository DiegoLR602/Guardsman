import sys

def parseOutput():
    output = {
        "Drive Name" : "",
        "Engine" : "",
        "Scanned Directories" : "",
        "Scanned Files" : "",
        "Infected Files" : "",
        "Scan duration" : ""
    }

    # data = sys.stdin.readline()
    with open('ex.txt') as f:
    # read every line in data
        for key, line in zip(output, f):
            # save lines that contain a key in the dictionary
            if key in line:
                output[key] = line[len(key):]
            # print("Key: ", key, ", Line: ", line)


    return output

def main():
    scandict = parseOutput()
    for key in scandict:
        print(key, ": ", scandict[key])


if __name__ == "__main__":
    main()