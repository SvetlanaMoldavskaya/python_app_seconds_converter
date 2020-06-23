# 2. The user inputs time in seconds. Trabnslate the given time into hours, minutes and seconds in the hh:mm:ss format. Use string formating.  

def translate():
    user_seconds = int(input("Input the seconds: "))
    hrs = user_seconds / 3600  #how many times the input can be divided by 1hr
    mins = (user_seconds % 3600) // 60
    secs = (user_seconds % 3600) % 60
    print("The time you have entered is {}:{}:{}".format(hrs, mins, secs))

translate()
