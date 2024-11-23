import pip

def tryImport(i):
    #
    # try except to check if user has library installed
    #
    try:
        return __import__(i)
    except ModuleNotFoundError:
        print("Library:", i, "not found, would you like to install it? [y/n]")
        q = input("> ")

        if q.upper() == "Y":
            print("installing...")
            
            pip.main(["install", i]) # use pythons built in pip library to
                                     # install library from within the script
            print("Completed!")
            
            return __import__(i)
        else:
            print("Okay, but to run this script", i, "is requred.\nPlease manually install it before running again")

        

#                     #
# example use in code #
#                     #

def main():
    requests = tryImport("requests")

    r = requests.get("https://google.com")
    print(r)


main()
