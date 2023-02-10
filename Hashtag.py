import re
kontni = "Changing the #world through #Social Enterprise"
def fonks(teks):
    return re.sub(r'#(\w+)', r'<a href="">#\1</a>', teks)
print(fonks(kontni))
