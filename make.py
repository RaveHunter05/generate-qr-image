import qrcode


def create_qr(image_link):
    img = qrcode.make(image_link)
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python make.py <image_link>")
        sys.exit(1)
    image_link = sys.argv[1]
    create_qr(image_link)
