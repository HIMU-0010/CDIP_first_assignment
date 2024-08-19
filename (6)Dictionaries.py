bookDict = {'title': 'To kill a Mockingbird', 'author': 'Harper Lee', 'year': '1968'}

#printing the values in the dictionary
print(bookDict['title'])
print(bookDict['author'])
print(bookDict['year'])

#adding a new item in the dictionary
bookDict['genre'] = 'Thriller'

#using loop to print the items in the dictionary
for items in bookDict:
    print(f"{items}: {bookDict[items]}")