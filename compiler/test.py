word='calmrtyrt'
# get the first two characters
wordss=[]
for c in word:
    wordss.append(c)
l1=wordss[0]
l2=wordss[1]
word=word.replace(l1, '', 1)
word= word.replace(l2, '', 1)
print(word)


