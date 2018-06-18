# https://apps.twitter.com
from textblob import TextBlob

x = input("Introduce aqui tu texto en ingles ")
wiki = TextBlob(x)
wiki.tags
wiki.words
print(str(wiki.tags))
y= wiki.sentiment.polarity
if y >= 0.5:
	print('Eres feliz ' + str(y))
	pass
else:
	print('No eres feliz ' + str(y))