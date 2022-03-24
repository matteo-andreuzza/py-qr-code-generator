import qrcode
img = qrcode.make('prova 123 codici a caso')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")