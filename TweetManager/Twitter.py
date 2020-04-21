# Tweet Manager assignment by Dylan Lade

from Tweet import Tweet
import time
import os.path

def main():

    feed = []
    loop = 1

    if os.path.isfile("feed.txt"):
        file = open("feed.txt", "r")
        for line in file:
            print(line)
            tokens = line.split('+')
            print(tokens[0])
            print(tokens[1])
            print(tokens[2])
            oldTweet = Tweet(tokens[0], tokens[2], float(tokens[1]))
            feed.append(oldTweet)
        file.close()

    name = str()
    text = str()

    while(loop):

        print("\n\nTweet Menu")
        print("----------")
        print("1. Make a Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit\n")
        
        choosing = True 
        while(choosing):
            try:
                choice = int(input("What would you like to do? "))
                if(choice in range(1,5)):
                    choosing = False
                    break
                print("Please select a valid option")
                choosing = True
            except ValueError:
                print("Please enter a numeric value")
                choosing = True
        
        if choice is 1:
            name = input("\nWhat is your name? ")
            text = input("What would you like to tweet? ")
            
            if(len(text) > 140):
                print("Tweets can only be 140 characters!")
            else:
                newTweet = Tweet(name, text, 0)
                feed.insert(0, newTweet)

        if choice is 2:
            print("Recent Tweets")
            print("-------------")

            if len(feed) is 0:
                print("There are no recent tweets")
            else:
                for tweet in feed:
                    tempAge = time.time() - tweet.get_age()
                    print(tempAge)
                    if (tempAge) < 60:
                        age = str(int(tempAge)) + 's'
                    if 60 < (tempAge) < 3600:
                        age = str(int(tempAge/60)) + 'm'
                    if 3600 < (tempAge):
                        age = str(int(tempAge/3600)) + 'h'

                    print(tweet.get_author() + ' - ' + age)
                    print(tweet.get_text())
        
        if choice is 3:
            token = input("What would you like to search for? ")
            found = 0
            while token is 0:
                token = input("What would you like to search for? ")

            print("Search Tweets")
            print("-------------")

            if len(feed) is 0:
                print("There are no recent tweets")
            else:
                for tweet in feed:
                    if token in tweet.get_text():
                        tempAge = time.time() - tweet.get_age()
                        if (tempAge) < 60:
                            age = str(tempAge) + 's'
                        if 60 < (tempAge) < 3600:
                            age = str(tempAge/60) + 'm'
                        if 3600 < (tempAge):
                            age = str(tempAge/3600) + 'h'

                        print(tweet.get_author() + ' - ' + tempAge)
                        print(tweet.get_text())
                        found += 1

                if found is 0:
                    print("No search results")
                        
                    
        if choice is 4:
            try:
                file = open("feed.txt", "w")
            except:
                print("File failed to open.")

            for tweet in feed:
                file.write(tweet.get_author() + '+' + str(tweet.get_age()) + '+' + tweet.get_text() + '+\n')
            
            file.close()
            print("Thank you for using the Tweet Manager!")
            loop = 0


if __name__ == "__main__":
    main()       

