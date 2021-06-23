a = A = "Alpha"
b = B = "Bravo"
c = C = "Charlie"
d = D = "Delta"
e = E = "Echo"
f = F = "Foxtrot"
g = G = "Golf"
h = H = "Hotel"
i = I = "India"
j = J = "Juliet"
k = K = "Kilo"
l = L = "Lima"
m = M = "Mike"
n = N = "November"
o = O = "Oscar"
p = P = "Papa"
q = Q = "Quebec"
r = R = "Romeo"
s = S = "Sierra"
t = T = "Tango"
u = U = "Uniform"
v = V = "Victor"
w = W = "Whiskey"
x = X = "Xray"
y = Y = "Yankee"
z = Z = "Zulu"


def split(text_to_split):
    return list(text_to_split)


text_to_convert = input("Enter the text you need to convert into NATO Phonetic Alphabet!\n")

text_list = (split(text_to_convert))


for letter in text_to_convert:
    print(eval(letter))
