import qrcode
language = input("HI, here you need write your language: ")

if language=='Russian' or language=='russian' or language=='ru' or language=='Ru' or language=='rus' or language=='Rus' or language=='Ру' or language=='ру' or language=='Русский' or language=='русский':
    qr=input('Если вы хотите сгенерировать qr code, напишите <НАЧАТЬ>: ')
    if qr=='начать' or qr=='Начать' or qr =='НАЧАТЬ':
        ccilka = input("Введите ссылку к которой хотите сгенерировать QR - CODE: ")
        if ccilka[0] =='h' and ccilka[1]=='t' and ccilka[2]=='t' and ccilka[3]=='p':
            print("Ваш qr - code генирируется...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("qr - code готов")
        else:
            while ccilka[0] !='h' and ccilka[1]!='t' and ccilka[2]!='t' and ccilka[3]!='p':
                ccilka=input("Это не ссылка, вставьте ее еще раз: ")
            print("Ваш qr - code генирируется...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("qr - code готов")


elif language=='En' or language=='en' or language=='Eng' or language=='eng' or language=='English' or language=='english':
    qr=input("If you want to generate a qr code, write <START>: ")
    if qr =='start' or qr =='Start' or qr =='START':
        ccilka = input("Enter the link to which you want to generate a QR CODE: ")
        if ccilka[0] =='h' and ccilka[1]=='t' and ccilka[2]=='t' and ccilka[3]=='p':
            print("Your QR - code is generating...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("qr is ready")
        else:
            while ccilka[0] !='h' and ccilka[1]!='t' and ccilka[2]!='t' and ccilka[3]!='p':
                ccilka=input("This is not a link, try paste it again: ")
            print("Your QR - code is generating...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("qr is ready")
    
elif language=='Fr' or language=='fr' or language=='French' or language=='french' or language=='Francais' or language=='francais':
    qr=input("Si vous souhaitez générer un code qr, écrivez <COMMENCER>: ")
    if qr =='commencer' or qr=='Commencer' or qr=='COMMENCER':
        ccilka = input("Entrez le lien vers lequel vous souhaitez générer le QR-CODE: ")
        if ccilka[0] =='h' and ccilka[1]=='t' and ccilka[2]=='t' and ccilka[3]=='p':
            print("Votre code qr est généré...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("Qr code prêt")
        else:
            while ccilka[0] !='h' and ccilka[1]!='t' and ccilka[2]!='t' and ccilka[3]!='p':
                ccilka=input("Ce n'est pas un lien, collez-le à nouveau: ")
            print("Qr code généré...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("Qr code prêt")


else:
    language = input("""We dont have this language. Try input one of this:
    1) English
    2) French
    3) Russian
    input: """)
    if language=='Russian' or language=='russian' or language=='ru' or language=='Ru' or language=='rus' or language=='Rus' or language=='Ру' or language=='ру' or language=='Русский' or language=='русский':
        qr=input('Если вы хотите сгенерировать qr code, напишите <НАЧАТЬ>: ')
        if qr == 'начать' or qr =='Начать' or qr =='НАЧАТЬ':
            ccilka = input("Введите ссылку к которой хотите сгенерировать QR - CODE: ")
            while ccilka[:4]!='http':
                ccilka=input("Это не ссылка, вставьте ее еще раз: ")
            print("Ваш qr - code генирируется...")
            img = qrcode.make(ccilka)
            img.save('myQRcode.png')
            img.show()
            print("qr - code готов") 
            # if you next == print*('')
            #input()qwwimg == int ('')
            


    elif language=='En' or language=='en' or language=='Eng' or language=='eng' or language=='English' or language=='english':
        qr=input("If you want to generate a qr code, write <START>: ")
        if qr == 'start' or qr == 'Start' or qr == 'START':
            ccilka = input("Enter the link to which you want to generate a QR CODE: ") 
            if ccilka[0] =='h' and ccilka[1]=='t' and ccilka[2]=='t' and ccilka[3]=='p':
                print("Qr code généré...")
                img = qrcode.make(ccilka)
                img.save('myQRcode.png')
                img.show()
                print("qr is ready")
            else:
                while ccilka[0] !='h' and ccilka[1]!='t' and ccilka[2]!='t' and ccilka[3]!='p':
                    ccilka=input("This is not a link, try paste it again: ")
                print("Your QR - code is generating...")
                img = qrcode.make(ccilka)
                img.save('myQRcode.png')
                img.show()
                print("qr is ready")


    elif language=='Fr' or language=='fr' or language=='French' or language=='french' or language=='Francais' or language=='francais':
        qr=input("Si vous souhaitez générer un code qr, écrivez <COMMENCER>: ")
        if qr == 'commencer' or qr =='Commencer' or qr == 'COMMENCER':
            ccilka = input("Entrez le lien vers lequel vous souhaitez générer le QR-CODE: ")
            if ccilka[0] =='h' and ccilka[1]=='t' and ccilka[2]=='t' and ccilka[3]=='p':
                print("Qr code généré...")
                img = qrcode.make(ccilka)
                img.save('myQRcode.png')
                img.show()
                print("Qr code prêt")
            else:
                while ccilka[0] !='h' and ccilka[1]!='t' and ccilka[2]!='t' and ccilka[3]!='p':
                    ccilka=input("Ce n'est pas un lien, collez-le à nouveau: ")
                print("Qr code généré...")
                img = qrcode.make(ccilka)
                img.save('myQRcode.png')
                img.show()
                print("Qr code prêt")

                # if: 
                # elif:
                #