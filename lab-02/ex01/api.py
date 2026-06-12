from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

def call_dynamic_method(instance, method_names, *args):
    """Hàm bổ trợ tự động tìm và gọi hàm có sẵn trong đối tượng"""
    for name in method_names:
        if hasattr(instance, name):
            return getattr(instance, name)(*args)
    raise AttributeError(f"Không tìm thấy hàm mã hóa/giải mã phù hợp trong {instance.__class__.__name__}")

# ==========================================
# 1. CAESAR CIPHER ALGORITHM
# ==========================================
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = call_dynamic_method(caesar_cipher, ['encrypt_text', 'encrypt', 'caesar_encrypt'], plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = call_dynamic_method(caesar_cipher, ['decrypt_text', 'decrypt', 'caesar_decrypt'], cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})  

# ==========================================
# 2. VIGENERE CIPHER ALGORITHM
# ==========================================
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = call_dynamic_method(vigenere_cipher, ['encrypt_text', 'encrypt', 'vigenere_encrypt'], plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = call_dynamic_method(vigenere_cipher, ['decrypt_text', 'decrypt', 'vigenere_decrypt'], cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ==========================================
# 3. RAILFENCE CIPHER ALGORITHM
# ==========================================
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    # ĐÃ SỬA: Tự động dò tìm tên hàm cho Rail Fence
    encrypted_text = call_dynamic_method(railfence_cipher, ['rail_fence_encrypt', 'encrypt_text', 'encrypt'], plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    # ĐÃ SỬA: Tự động dò tìm tên hàm cho Rail Fence
    decrypted_text = call_dynamic_method(railfence_cipher, ['rail_fence_decrypt', 'decrypt_text', 'decrypt'], cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ==========================================
# 4. PLAYFAIR CIPHER ALGORITHM
# ==========================================
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key'] # Đây là chuỗi chữ (String) nhận từ PyQt5
    
    # SỬA Ở ĐÂY: Truyền trực tiếp 'key' (String) thay vì truyền playfair_matrix (List)
    encrypted_text = call_dynamic_method(playfair_cipher, ['playfair_encrypt', 'encrypt_text', 'encrypt'], plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key'] # Đây là chuỗi chữ (String) nhận từ PyQt5
    
    # SỬA Ở ĐÂY: Truyền trực tiếp 'key' (String) vào hàm giải mã
    decrypted_text = call_dynamic_method(playfair_cipher, ['playfair_decrypt', 'decrypt_text', 'decrypt'], cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)