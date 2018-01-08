import string
def caesarcipher(message, shift, decode = False):
   if decode: shift = 26 - shift
   return message.translate(
       str.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift] +
           string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
           )
       )


def caesardecipher(message, shift,decode = True):
   if decode: shift = 26 - shift
   return message.translate(
       str.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift] +
           string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
           )
       )
  

def main():
   

   message = input("Please input message to encode: ")
   shift = eval(input("Please input a shift value: "))


   enc = caesarcipher(message, shift)
   print("CaesarCipher : ",enc)
   print("CaesarDecipher: ", caesardecipher(message, shift, decode = True))

main()

