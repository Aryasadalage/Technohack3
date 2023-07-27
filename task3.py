print("***CURRENCY CONVERTER***")


while True:
    print("select your currency unit")
    print("1.Rupees")
    print("2.YEN")
    print("3.U.S.Doller")
    print("4.POUND")
    print("5.END")

    b=input("enter your currency here:")
    if b=="1":
        r=float(input("enter rupees here:"))



        while True:
            print("Select the currency unit")
            print("1.YEN")
            print("2.POUND")
            print("3.U.S.DOLLER")
            print("4.END")



            o=input("enter option here:")

            if o=="1":
                Y=r*1.71
                print(Y,"YEN")


            elif o=="2":
                p=r*0.0094
                print(p,"POUND")


            elif o=="3":
                d=r*0.012
                print(d,"U.S.Doller")


            elif o=="4":
                print("Thanks to visit")
                break

            else:
                print("enter correct option here")
    elif b=="2":
        r=float(input("enter YEN here:"))



        while True:
            print("Select the currency unit")
            print("1.RUPEES")
            print("2.POUND")
            print("3.U.S.DOLLER")
            print("4.END")
            o=input("enter option here:")

            if o=="1":
                Y=r*0.59
                print(Y,"Rupees")


            elif o=="2":
                p=r*0.0055
                print(p,"POUND")


            elif o=="3":
                d=r*0.0071
                print(d,"U.S.Doller")


            elif o=="4":
                print("Thanks to visit")
                break

            else:
                print("enter correct option here")

    elif b=="3":
        r=float(input("enter U.S.Doller here:"))

        while True:
            print("Select the currency unit")
            print("1.YEN")
            print("2.POUND")
            print("3.Rupees")
            print("4.END")
            o=input("enter option here:")

            if o=="1":
                Y=r*140.16
                print(Y,"YEN")


            elif o=="2":
                p=r*0.77
                print(p,"POUND")


            elif o=="3":
                d=r*81.98
                print(d,"Rupees")


            elif o=="4":
                print("Thanks to visit")
                break

            else:
                print("enter correct option here")

    elif b=="4":
        r=float(input("enter Pound here:"))

        while True:
            print("Select the currency unit")
            print("1.YEN")
            print("2.RUPEES")
            print("3.U.S.DOLLER")
            print("4.END")
            o=input("enter option here:")

            if o=="1":
                Y=r*181.49
                print(Y,"YEN")


            elif o=="2":
                p=r*106.16
                print(p,"Ruppes")


            elif o=="3":
                d=r*1.30
                print(d,"U.S.Doller")


            elif o=="4":
                print("Thanks to visit")
                break

            else:
                print("enter correct option here")

    elif b=="5":
        print("thanks to visit")
        break

    else:
        print("enter correct option")










