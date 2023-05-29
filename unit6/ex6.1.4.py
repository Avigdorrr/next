import base64

def main():
    encoded_string = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo="
    utf8_bytes = encoded_string.encode("utf-8")  # Encode the string to UTF-8 bytes
    decoded_bytes = base64.b64decode(utf8_bytes)  # Decode the UTF-8 bytes using Base64
    decoded_string = decoded_bytes.decode("utf-8")  # Convert the decoded bytes back to a string

    print(decoded_string)



if __name__ == '__main__':
    main()