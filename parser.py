def parseOutput():
    output = {
        "Drive name" : "",
        "Engine version" : "",
        "Scanned directories" : "",
        "Infected files" : "",
        "Data scanned" : "",
        "Time" : ""
    }

    with open('ex.txt') as f:
    # read every line in data
        for line in f:
            for key in output:
                # save lines that contain a key in the dictionary
                if key in line:
                    output[key] = line[len(key):]
                    break

    return output

def main():
    scandict = parseOutput()
    for key in scandict:
        print(key, scandict[key])


if __name__ == "__main__":
    main()