myDict = {
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item" 
}
print("options are: ", myDict.keys())
a=input("Enter the hindi word: \n")
print("The meaning of the word is: ", myDict.get(a))