class PlayFairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        # Chuyển viết hoa và thay thế J bằng I
        key = key.upper().replace("J", "I")
        
        # Lọc bỏ ký tự trùng trong khóa
        seen = set()
        matrix_letters = []
        for char in key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                matrix_letters.append(char)
                
        # Bảng chữ cái chuẩn 25 ký tự (Gộp J vào I)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in seen:
                seen.add(letter)
                matrix_letters.append(letter)
        
        # Trả về ma trận cấu trúc mảng 2 chiều 5x5
        return [matrix_letters[i:i+5] for i in range(0, 25, 5)]
    
    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return 0, 0
                
    def encrypt_text(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        plain_text = "".join([c.upper() for c in plain_text if c.isalpha()]).replace("J", "I")
        
        # Chuẩn bị chuỗi: Tách cặp trùng bằng X, điền X vào cuối nếu lẻ
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            prepared_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    prepared_text += "X"
                    i += 1
                else:
                    prepared_text += plain_text[i+1]
                    i += 2
            else:
                prepared_text += "X"
                i += 1

        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2: # Cùng hàng -> Dịch phải
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: # Cùng cột -> Dịch xuống
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else: # Khác hàng cột -> Đổi góc chéo vuông
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text
    
    def decrypt_text(self, cipher_text, key):
        matrix = self.create_playfair_matrix(key)
        cipher_text = "".join([c.upper() for c in cipher_text if c.isalpha()])
        
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            if len(pair) < 2: break
                
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2: # Cùng hàng -> Dịch trái
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2: # Cùng cột -> Dịch lên
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else: # Khác hàng cột -> Đổi góc chéo vuông
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        # Khôi phục bản rõ (Bỏ các ký tự X đệm xen kẽ nếu có)
        final_plain_text = ""
        idx = 0
        while idx < len(decrypted_text):
            final_plain_text += decrypted_text[idx]
            if idx + 2 < len(decrypted_text) and decrypted_text[idx] == decrypted_text[idx+2] and decrypted_text[idx+1] == "X":
                final_plain_text += decrypted_text[idx+2]
                idx += 3
            else:
                idx += 1
                
        if final_plain_text.endswith("X"):
            final_plain_text = final_plain_text[:-1]
            
        return final_plain_text