from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
answer = "y"
while answer == "y":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def ceaser(the_text, the_shift, the_direction):
    the_shift = the_shift % 26
    message=""
    if the_direction =="decode":
      the_shift = the_shift * (-1)
    for i in the_text:
      if i in alphabet:
        for n in range(26):
          if i == alphabet[n]:
            r=n+the_shift
            if r < 26:
              message = message + alphabet[r]
            else:
              r=n+the_shift-26
              message = message + alphabet[r]
      else:
        message = message + i

    print(f"The message is : {message}")
    
  ceaser(the_text=text, the_shift=shift, the_direction=direction)

  answer= input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
