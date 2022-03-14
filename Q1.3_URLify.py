# Q3: write a method to replace all spaces in a string with '%20'
# You may assume that the string has sufficient space at the end to hold the additional characters,
# # and that you are given the "true" lenghth of the string.
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def URLify_replace(str, length):
    str=str.rstrip()
    str=str.replace(" ", "%20")
    print(str)

#"space" mentioned below including: whitespace, newline and tab
#strip: remove the space in the beginning and the ending of the string
#strip("xyz"): remove all the x y z in the string
#rstrip: remove the space in the ending of the string
#lstrip: remove the space on a string beginning


URLify_replace("Mr John Smith ",13)
URLify_replace("much ado about nothing      ", 22)
URLify_replace( " a b       ", 5)