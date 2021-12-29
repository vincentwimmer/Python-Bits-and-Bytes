#pip install pyperclip
import pyperclip as pc
a1 = "This is now in your clipboard!"
pc.copy(a1)

a2 = pc.paste()
print(a2)
