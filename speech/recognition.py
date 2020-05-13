flag='y'
while flag=='y':
    print("\tthis program is used to covert text to speech & vice versa")
    print("\n \t enter you choice:")
    print("\t 1.text to speech ")
    print("\t 2. speech to text")
    a=input("\t choice : ")
    if a=='1':
        import text_speech
    elif a=='2':
        import speech_text
    else:
        exit()
    print("\t \n want to continue ")
    flag=input("\t 'y' or 'n' :")
