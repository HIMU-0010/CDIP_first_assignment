fruitsList = ['lichi', 'mango', 'orange', 'kiwi', 'blueberry']

#new list using list comprehension
fruitsLenList = [len(x) for x in fruitsList]
print(fruitsLenList)

#insert new item ina list
fruitsList.append('watermelon')
print(fruitsList)

#sort list
fruitsList.sort()
print(fruitsList)

#change in the file for new commit