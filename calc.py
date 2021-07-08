# testing git
name=str(input("What is your name?\n"))
print("Welcome to the most reliable fortune simulator, " + name + "!")
import time
time.sleep(3)
Question = input("Do you want your fortune to be read?\n")
if Question == "yes":
    print("Great to have you! Let's get started.")
    Question = input("How are you feeling today?\n ")
    if Question == "happy":
        print ("Shame on you for thinking a cookie is psychic")
    elif Question == "sad":
        print ("A light heart carries you through all the hard times")
    elif Question == "mad":
        print ("Clench your anger with a bottle of champagne")
    elif Question == "anxious":
        print("Breathe in, breathe out. Take as many breaths as you need to calm down.")
    elif Question == "tired":
        print("We're tired, too.")
    else:
        print ("A lifetime of happiness lies ahead of you")
    time.sleep(3)
    Question = input("Which of the following are you most concerned about right now (love, money, job)?\n ")
    if Question == "love":
        print ("Shame on you for thinking we can predict your love life")
    elif Question == "money":
        print ("The next left turn you make, you will find something more valuable than gold")
    else:
        print ("A golden egg of opportunity falls into your lap this month.")
    time.sleep(3)
    Question = input("What do you look forward to doing after the pandemic (traveling, eating out, partying)?\n ")
    if Question == "traveling":
        print ("Traveling this year will bring your life into greater perspective this year.")
    elif Question == "eating out":
        print ("To eat is a necessity, but to eat intelligently is an art")
    else:
        print ("Beer is proof that God loves us.")
    time.sleep(3)
    print("Thank you for using our services! Enjoy the rest of your day!!")
elif Question == "no":
    print("That's too bad. You may silently walk out the door")