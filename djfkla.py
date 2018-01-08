import string
def caesar(s, k, decode = False):
   if decode: k = 26 - k
   return s.translate(
       str.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
           string.ascii_lowercase[k:] + string.ascii_lowercase[:k]
           )
       )
c = input("Please input message to encode: ")
v = eval(input("Please input a shift value: "))


enc = caesar(c, v)
print("CaesarCipher : ",enc)
print("Caesar Decipher: ", caesar(enc, v, decode = True))


