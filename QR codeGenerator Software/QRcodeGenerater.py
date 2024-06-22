import qrcode as qr # type: ignore

img = qr.make('https://github.com/saadahmedacademy')
img.save('github.png')
