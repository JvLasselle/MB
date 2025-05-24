#Authon:  Jared Lasselle
#Purpose:  The purpose of this file is to be an assignment for the programming merit badge.


#Write this function.
#This function takes in one argument sortMe and sorts it.
#sortMe is an array.
#Do not modify the function declaration.  Only modify the function body.
def sortFunction(sortMe):
    return []













###
#Do not modify anything below this line, but feel free to read through it and learn from it.
###

#This allows me to place colors in the printout text from the testing
class bcolors: #print with these in the string that is printed and we get colored text.  endc is the end of what ever color you are using.
    PASS = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'
    BLUE = '\033[96m'
    BOLD = '\033[1m'

#import statements are should be at the top of the file.  However, I put them here to reduce clutter at the top
import random
import time

def main():
    #The main function will run when the python file is run.
    #For this program the main function will facilitate testing your code.
    print(f"\n{bcolors.BLUE}Running tests on sortFunctionn.  Results will be shown below{bcolors.ENDC}\n")
    tests = [[],                    #Test one for the empty list
             [1],                   #Test two for the list with one element
             [1,2],                 #Test three for the list with more than one element
             [2,1],                 #Test four for the list in reverse order
             [5,4,3,2,1],           #Test five the list of five elements in reverse order
             [3,5,1,2,4],           #Test six for the list that is not allready sorted
             [3,5,1],               #Test seven for the list not containing consecutive elements
             [-1,3,-5],             #Test seven for the list containing negative numbers
             [4,4,4,4,4,6,3,2]]     #Test eight for the list containing duplicates
   
    testNine = []                   #Test nine for the list containing random numbers
    for i in range(10):
        testNine.append(random.randint(-15,15))
    tests.append(testNine)
    testTen = []                    #Test ten for the list of random length
    for i in range(random.randint(10,20)):
        testTen.append(random.randint(-15,15))
    tests.append(testTen)

    failCounter = 0
    counter = 0
    for test in tests:
        if counter % 3 == 0:
            time.sleep(0.5)
        if failCounter >= 4:
            quit()
        counter += 1
        try:
            if sortFunction(test) == sorted(test):
                print(f"{bcolors.PASS}Test {counter} passed!{bcolors.ENDC}")
            elif sortFunction(test) == sorted(test, reverse=True):
                print(f"{bcolors.WARNING}Test {counter} failed.\nThe sort function works, but is sorting in reverse order.{bcolors.ENDC}\nThe input list was:\t\t\t{test}\nThe output from your function was:\t{sortFunction(test)}\nThe desired output was:\t\t\t{sorted(test)}")
                failCounter += 0.5
            else:
                print(f"{bcolors.FAIL}Test {counter} failed.  See below for debugging information.{bcolors.ENDC}\nThe input list was:\t\t\t{test}\nThe output from your function was:\t{sortFunction(test)}\nThe desired output was:\t\t\t{sorted(test)}")
                failCounter += 1
        except IndexError as err:
            print(f"{bcolors.FAIL}{bcolors.BOLD}TEST {counter} GAVE AN INDEX ERROR.  This happens when you access a point in the list that does not exist.  See below for an example.{bcolors.ENDC}\naList = [0,1,2,3,4,5]\naList[6]\nThe error message is: {err}\n\n{bcolors.FAIL}The other tests will not run{bcolors.ENDC}\n")
            quit()

    if failCounter > 0:
        quit()
    else:
        time.sleep(1.7)
        print()
        time.sleep(1.7)
        print()
        time.sleep(1.7)
   
    for i in range(30,37):
        print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Initializing speed test.{bcolors.ENDC}")
    for i in range(90,97):
        print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Initializing speed test.{bcolors.ENDC}")

    speedTest = []                  #Test eleven for speed
    for i in range(20000):
        speedTest.append(random.randint(-2000000000,2000000000))
   
    print("\n\n")
    for i in range(30,37):
        print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Running speed test.{bcolors.ENDC}")
    for i in range(90,97):
        print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Running speed test.{bcolors.ENDC}")
    start = time.perf_counter()
    sortFunction(speedTest)
    end = time.perf_counter()
    theTime = end-start
    print("\n\n")
    try:
        if sortFunction(test) == sorted(test):
            for i in range(30,37):
                print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Speed test passed in {theTime} seconds!{bcolors.ENDC}")
            for i in range(90,97):
                print(f"{'\033' + f'[{99}m'}{'\033' + f'[{i}m'}Speed test passed in {theTime} seconds!{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Speed test failed.  The list is too long to print debugging information.{bcolors.ENDC}")
    except IndexError as err:
        print(f"{bcolors.FAIL}{bcolors.BOLD}SPEED TEST GAVE AN INDEX ERROR.  This happens when you access a point in the list that does not exist.  See below for an example.{bcolors.ENDC}\naList = [0,1,2,3,4,5]\naList[6]\nThe error message is: {err}\n\n{bcolors.FAIL}The other tests will not run{bcolors.ENDC}\n")
        quit()

#This will run the main function
if __name__ == "__main__":
    main()