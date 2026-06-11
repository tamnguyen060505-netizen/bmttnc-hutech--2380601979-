# Trong file cipher/vigenere.py

class VigenereCipher:
    def __init__(self):
        pass

    # Đảm bảo đặt tên hàm chính xác là encrypt_text
    def encrypt_text(self, text, key):
        text = str(text)
        key = "".join([c.upper() for c in key if c.isalpha()])
        if not key:
            return "LỖI: Khóa không hợp lệ."
            
        result = []
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 65
                if char.isupper():
                    result.append(chr((ord(char) - 65 + shift) % 26 + 65))
                else:
                    result.append(chr((ord(char) - 97 + shift) % 26 + 97))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)

    # Đảm bảo đặt tên hàm chính xác là decrypt_text
    def decrypt_text(self, text, key):
        text = str(text)
        key = "".join([c.upper() for c in key if c.isalpha()])
        if not key:
            return "LỖI: Khóa không hợp lệ."
            
        result = []
        key_index = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - 65
                if char.isupper():
                    result.append(chr((ord(char) - 65 - shift) % 26 + 65))
                else:
                    result.append(chr((ord(char) - 97 - shift) % 26 + 97))
                key_index += 1
            else:
                result.append(char)
        return "".join(result)