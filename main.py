
def meals(eggs):
    print("over easy eggs coming up")


def invalid():
    print("you entered an invalid input")

def print_hi(meal):
    while True:
        meal = input("What would you like for breakfast? (enter a number)\n 1. eggs\n 2. toast\n 3. smoothie\n")
        breakfast = ["1", "2", "3"]
        if meal == breakfast[0]:
            eggs = input("How would you like your eggs cooked? (enter a number 1-3)\n 1. over easy\n 2. scrambled\n 3. poached\n")
            egganswer = ["1", "2", "3"]
            if eggs == egganswer[0]:
                meals(eggs)
                break
           #   print("over easy eggs coming up.")
            elif eggs == egganswer[1]:
                print("scrambled eggs coming up")
                break
            elif eggs == egganswer[2]:
                print("poached egg coming up")
                break
            else:
                print("This was not an option choice")
        elif meal == breakfast[1]:
            toast = input("Would would you like on your toast? (enter a number 1-3)\n 1. avocado\n 2. peanut butter\n 3. cream cheese\n")
            toastanswer = ["1", "2", "3"]
            if toast == toastanswer[0]:
                print("Avocado toast coming up")
                break
            elif toast == toastanswer[1]:
                print("peanut butter toast coming up")
                break
            elif toast == toastanswer[2]:
                print("ew who puts cream cheese on their toast")
                break
            else:
                print("Enter a number 1-3")
        elif meal == breakfast[2]:
            smoothie = input("What kind of smoothie would you like? (enter a number 1-3)\n 1. Straberry banana\n 2. Mango Pinneapple\n 3. peanut butter protein\n")
            smoothieanswer = ["1", "2", "3"]
            if smoothie == smoothieanswer[0]:
                protein = input("would you like a scoop of protein? Enter 1 for yes and 2 for no\n")
                if protein == "1":
                    print("strawberry smoothie with protein coming up")
                    break
                else: print("You did not select 1 or 2")
            elif smoothie == smoothieanswer[1]:
                allergic = input("are you allergic to pineapple? enter 1 for yes or 2 no\n")
                if allergic == "1":
                    print("sorry you can't have it unless you have benadryl or an epipen")
                    break
                else:
                    print("Take your smoothie and pay up front ")
                    break
            elif smoothie == smoothieanswer[2]:
                print("peanut butter protein smoothie coming up")
                break

    else:
        invalid()



if __name__ == '__main__':
    print_hi('PyCharm')


