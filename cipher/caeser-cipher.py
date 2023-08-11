alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(txt,num):
    cipher= " "
    for i in txt:   
        if i in alphabet:
            position=alphabet.index(i)
            new_position= position + num
            cipher_text=alphabet[new_position]
            cipher += cipher_text
        else:
            cipher+= i
    print(f" The Encoded Message is {cipher}")


def decrypt (txt, num):
    cipher=" "
    for i in txt:
        if i in alphabet:
            position=alphabet.index(i)
            new_position= position - num
            cipher_text=alphabet[new_position]
            cipher += cipher_text
        else:
            cipher += i
    print(f"The Decoded Message is {cipher}")

remain_continue= True
while remain_continue :
    direction = input("Type 'encode' to encrytion or 'decode' for decryption\n")
    text=input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift % 26

    if direction=="encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    result = input('tyoe yes continue or no for end')
    if result=='no':
        remain_continue= False
        print('Good Bye😂😘')


#//////////////////// 2nd Solution 

# def encrypt(txt,num):
#     cipher= " "
#     for char in txt:
#         if char in alphabet:
#             position=alphabet.index(char)
#             if direction=="encode":
#                 new_position= position + num
#             else:
#                 new_position= position - num
#             cipher_text=alphabet[new_position]
#             cipher += cipher_text
#         else:
#             cipher += char
#     print(f"The {direction}d Message is {cipher}")


# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrytion or 'decode' for decryption\n")
#     text=input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     shift = shift % 26

#     if direction=="encode":
#         encrypt(text, shift)
#     else:
#         encrypt(text, shift)
#     result=input("if you want to play agian type 'Yes' or otherwise 'No'")
#     if result=='no':
#         should_continue = False
#         print('Good Bye')