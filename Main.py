import cryponfurt

print("\nPress for Encrypt(1) or Decrypt(2) QUIT(Q or q)\n")

while True:
    proc=input("What is your process? ")

    if proc=="q" or proc=="Q":
        print("shutdown")
        break
    elif proc=="1":
        text=input("give me a text: ")
        cryponfurt.encrypt(text)
    elif proc=="2":
        text=input("give me a text: ")
        cryponfurt.decrypt(text)
    else:
        print("ERROR!! Try Again.")

