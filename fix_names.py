from fontTools.ttLib import TTFont
from fontTools.otf2ttf import main as otf2ttf
import sys

# Fix font names
font = TTFont('Patched-NotoSansSC-Regular.otf')
name = font['name']
updates = {
    1:  'Noto Sans CJK SC Patched',
    4:  'Noto Sans CJK SC Patched Regular',
    16: 'Noto Sans CJK SC Patched',
    17: 'Regular',
}
for nameID, value in updates.items():
    name.setName(value, nameID, 3, 1, 0x0409)
    name.setName(value, nameID, 1, 0, 0)

font.save('Patched-NotoSansSC-Fixed.otf')
print('Names fixed — saved as Patched-NotoSansSC-Fixed.otf')

# Convert OTF to TTF
sys.argv = ['otf2ttf', 'Patched-NotoSansSC-Fixed.otf']
otf2ttf()
print('Converted to TTF — saved as Patched-NotoSansSC-Fixed.ttf')