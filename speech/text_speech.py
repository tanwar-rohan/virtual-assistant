import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
g =input("Enter text : ") 

speak.Speak(g)
