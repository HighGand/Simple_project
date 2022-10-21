from PIL import Image, ImageDraw, ImageFont
import time
import os

'''Paste the data on the photo'''


folder = os.getcwd()  # Path
zdjecia = os.listdir(folder)  # listing files with the path

for a in zdjecia:
    if '.jpg' in a:
        data = time.ctime(os.path.getctime(a))  # Pobiera datę utworzenia pliku
        image = Image.open(a)  # Otwiera plik
        image_kopia = image.copy()  # Utworzenie kopi
        image_napis = ImageDraw.Draw(image_kopia)  # Przekazanie gdzie ma być wykonany napis
        font = ImageFont.truetype('arial.ttf', 75)  # Parametry napisu
        image_napis.text((20, 60), data, font=font, fill='black')  # Umieszcza napis na obrazie
        image_kopia.save(os.path.join(r'C:\Users\TKO\Desktop\Programowanie\Własne_projekty\Data', a),
                         'JPEG')  # Zapisuje obraz
