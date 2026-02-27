# #  STRING METHODS (VERY IMPORTANT)

text1="       hello python learners       "

#Remove Spaces
# print("Orignal text:", (text1) )
# print("Remove spaces:", text1.strip())


# #Covert to capital letters
# print("Orignal text:", (text1) )
# print("Capital Letters :", text1.upper().strip())

# #Covert to proper case
# print("Orignal text:", (text1) )
# print("Proper Letters :", text1.title().strip())

# #Covert to Lower case
# print("Orignal text:", (text1) )
# print("Lower Letters :", text1.lower().strip())

# #Replace
# print("Replace python word with SQL",text1.replace("python","SQL"))

# #Coutn occurrences of a letter of word
# print("Count of o", text1.count("s"))



#msg="Welcome to Python Course"
# #Split string into list of words
# words=msg.split()
# print( words)
# #Join back with hyphen
# joined_text="-".join(words)
# print("Joined text:", joined_text)

# # Find position of letter
# print("Index of P :",msg.find("P"))




# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: ₹3500/-" → "3500"
price_text = "Price: ₹3500/-"
clean_price = price_text.replace("Price:", "") \
                        .replace("₹", "") \
                        .replace("/-", "") \
                        .strip()
print("Clean Price:", clean_price)