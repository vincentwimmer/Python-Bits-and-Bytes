from PIL import Image

# Open background and foreground and ensure they are RGB (not palette)
bg = Image.open('background.png').convert('RGB')
fg = Image.open('overlay.png').convert('RGBA')

# Resize foreground down from 500x500 to 200x200
fg_resized = fg.resize((200,200))

# Overlay foreground onto background at top right corner, using transparency of foreground as mask
bg.paste(fg_resized,box=(0,0),mask=fg_resized)

# Save result
bg.show()
#bg.save('result.png')
