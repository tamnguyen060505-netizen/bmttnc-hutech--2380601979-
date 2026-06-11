class RailFenceCipher:
    def __init__(self):
        pass
    
    def encrypt_text(self, plain_text, num_rails):
        # RÀNG BUỘC BACKEND: Số tầng phải >= 2 và không lớn hơn độ dài chuỗi
        if num_rails < 2:
            return "LỖI: Số hàng (Rails) phải lớn hơn hoặc bằng 2."
        if not plain_text:
            return "LỖI: Văn bản đầu vào không được để trống."
            
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1 
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def decrypt_text(self, cipher_text, num_rails):
        # RÀNG BUỘC BACKEND
        if num_rails < 2:
            return "LỖI: Số hàng (Rails) phải lớn hơn hoặc bằng 2."
        if not cipher_text:
            return "LỖI: Văn bản mã hóa không được để trống."
            
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(cipher_text[start:start + length])
            start += length
        
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            if not rails[rail_index]: # Phòng vệ bổ sung tránh lỗi rỗng mảng
                break
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return plain_text