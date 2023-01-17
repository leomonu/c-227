print("Welcome to the world of crytography")

def main():
    print()
    print("Choose any one option : ")
    choose = int(input("1.encryption\n2.decryption\nchoose(1,2)  "))
    if(choose==1):
        encryption()
    elif(choose==2):
        decryption()
    else:
        print("wrong chose")    

def encryption():
    print("Encryption")
    msg = input("enter your msg : ")
    key=int(input("Enter Key(1-94) : "))
    encrypted_txtmsg = ""
    for i in range(len(msg)):
        oderingmsg=(ord(msg[i])+key)
        if(oderingmsg>126):
            oderingmsg=oderingmsg-127+32
        encrypted_txtmsg+=chr(oderingmsg)
    print("encrypted messages: "+encrypted_txtmsg)
    main()
def decryption():
    print("Decryption started")
    print("msg can only be lower and upper case alphabets")
    encrypted_txtmsg= input("enter the encrypted text:")
    secretkey=int(input("Enter Key(1-94) : "))
    decrypted_textmsg=""

    for i in range(len(encrypted_txtmsg)):
        orderingmsg=(ord(encrypted_txtmsg[i])-secretkey)
        if(orderingmsg<32):
            orderingmsg=orderingmsg+127-32
        decrypted_textmsg+=chr(orderingmsg)
    print("decrypted msg : "+decrypted_textmsg)

if __name__ == "__main__":
    main()