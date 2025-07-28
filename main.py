import qrcode

# Contenido que quieres codificar
data = "https://misitioweb.cl"  # o puede ser un texto, correo, etc.

# Crear objeto QR
qr = qrcode.QRCode(
    version=1,  # tamaño del QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Agregar datos al QR
qr.add_data(data)
qr.make(fit=True)

# Crear imagen del QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar imagen
img.save("codigo_qr.png")
