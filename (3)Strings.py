str = "Lorem ipsum is placeholder text COMMONLY used in the graphic, PRINT, and publishing industries for PREVIEWING layouts and visual mockups."

print(str.upper()) #Convert to Uppercase 
print(str.lower()) #Convert to lowercase

# Spliting the sentence
words = str.split(" ")
print(words)

print(len(str)) #Length of the sentence

print(str.replace("ipsum", "muspi")) #Replace the word ipsum with muspi