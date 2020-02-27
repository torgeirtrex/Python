import wikipedia
import webbrowser
wikipage = wikipedia.random(4)
userchoice = input("Type which of these topic would you like to read more about?{}".format(wikipage))
wikiload = wikipedia.page(userchoice)

print(wikipedia.summary(userchoice))

readmore = input("Would you like to read more on the topic? Y/N" )
if(readmore == "Y" or readmore == "y"):
        webbrowser.open(wikiload.url,new=2)
else:
    exit(0)