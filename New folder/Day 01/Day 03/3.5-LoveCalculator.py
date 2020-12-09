print("Python Love Calculator!")
name1 = input("What's your name? ")
name2 = input("What's your partner's name? ")
# convert the names into lowercase letters
name1 = name1.lower()
name2 = name2.lower()
# combine the names
name = name1+name2
# sum of the number of occurences in T, R, U, E 
# concatenated with sum of the number of occurences in L, O, V, E 
# gives the love percentage

# count the number of times t, r, u, e, l, o, v, e occur in the combined name
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
# sum1 is sum of t, r, u, e
sum1 = t+r+u+e
# sum2 is sum of l, o, v, e
sum2 = l+o+v+e
# total percentage
print("Love Percentage is {}{}." .format(sum1, sum2))