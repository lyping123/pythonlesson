# regex
import re


# RegEx function




txt ="this is orange, the price is RM20.15"


time="8:00 - 17:00"

result=re.sub("[-]","to",time)

print(f"Our working hour is {result}")



price1="RM20.50"
price2="RM20.15"

newprice1=re.findall("\d+\.\d+",price1)
newprice2=re.findall("\d+\.\d+",price2)


information="name=peter, age=25, gender=male , name=jane,age=30,gender=female"


sentent="The sun dipped below the horizon, painting the sky in hues of orange and pink as the evening breeze whispered through the trees"



# print(float(newprice1[0])+float(newprice2[0]))






# txt = "The rain in Spain"
# Returns a match if the specified characters are at the beginning of the string
# fa = re.findall(r"\AThe", txt)
# seach=re.search(r"\AThe", txt)
# split=re.split(r"\AThe", txt)
# sub=re.sub(r"\AThe","It's", txt)


# Returns a match if the specified characters are at the end of the string
# fa = re.findall(r"ain\b", txt)
# seach=re.search(r"ain\b", txt)
# split=re.split(r"ain\b", txt)
# sub=re.sub(r"ain\b","ed", txt)

# print(split)

# Returns a match where the string contains digits (numbers from 0-9)
# txt = "1 plus 1 equals 2" 
# fa = re.findall(r"\d", txt)
# seach=re.search(r"\d", txt)
# # split=re.split("\d", txt)

# Returns a match where the string contains a white space character

# fa = re.findall("\s", txt)
# seach=re.search("\d", txt)
# split=re.split("\d", txt)
# sub=re.sub("\d", txt)
# print(fa)


# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# fa = re.findall("\w", txt)
# seach=re.search("\w", txt)
# split=re.split("\w", txt)
# sub=re.sub("\w", txt)

# print(fa)

# txt = "h i j d jf j k l k l l r d" 
# x = re.findall("[arg]", txt)
# x = re.findall("[a-n]", txt)
# x = re.findall("[^arn]", txt)
# x = re.findall(r"\w",txt)

# print(x)

