# History Behind this project
I build chat bots for discord and Twitch, recently a friend of mine wanted a bot for Twitch and one of the features he requested was that the bot would say hi to user when they say hi in chat or when they enter chat. The problem is, it takes the full username and mentions them whereas with this we can shorten the name because by default we shorten peoples name without even knowing it. Whereas you lover who you call Brit and not Brittany or friend you call Zach and not Zachary.

# How it works
This program works in conjunction of other libraries. It uses regular expression to find capital and common letters in names because online we usually split up names with underscores or just typing it like: `XxxxXxxx`. If regular expression can’t find anything it then letter by letter looks for words using PyEnchant, PyEnchant will also suggest words that can be used to match.
After that is done it uses whatever words that it finds, scores it as for percentage of the word used (The lower the better), it then determines the best word to be used, using spacy.

# Future Plans
Yea this works but i need to figure out how to run this with ML make it self dependent.

# Support
You want to help out? sure! My discord is: `RingoMär#7116` shoot me a message or just make a pull request!
