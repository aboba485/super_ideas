mail = input("Well done! Now we'll do a quick registration. Input your mail: ")

while mail[-11:]!='@gmail.com' or mail[-9:] !='@mail.ru' or mail[-11:]!='@yandex.ru':
    mail = input("Your mail is not correct, input it again: ")
print("ok")