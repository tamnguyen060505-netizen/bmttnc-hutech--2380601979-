from flask import Flask, render_template, request

# Import các class thuật toán từ package cipher
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Hàm bổ trợ để tạo giao diện hiển thị kết quả hoặc lỗi chuẩn Bootstrap
def render_result_template(title, text, key, result_text, is_error=False, back_url="/"):
    color = "danger" if is_error else "success"
    title_color = "#dc3545" if is_error else "#28a745"
    
    content = f"""
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 600px; margin: 60px auto; padding: 30px; border: 1px solid #e0e0e0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); background-color: #fff;">
        <h3 style="color: {title_color}; border-bottom: 2px solid {title_color}; padding-bottom: 10px; margin-bottom: 20px;">{title}</h3>
        <div style="margin-bottom: 15px; font-size: 16px;">
            <p><b>Dữ liệu nhập (Text):</b> <code style="background:#f4f4f4; padding:2px 6px; border-radius:4px;">{text}</code></p>
            <p><b>Khóa (Key):</b> <code style="background:#f4f4f4; padding:2px 6px; border-radius:4px;">{key}</code></p>
        </div>
        <div style="background-color: {'#fff5f5' if is_error else '#f8f9fa'}; border-left: 5px solid {title_color}; padding: 15px; border-radius: 4px; margin-bottom: 25px;">
            <p style="margin: 0; font-size: 16px;"><b>{'Chi tiết lỗi:' if is_error else 'Kết quả đầu ra:'}</b></p>
            <p style="margin: 5px 0 0 0; font-size: 18px; font-weight: bold; color: {title_color}; word-break: break-all;">{result_text}</p>
        </div>
        <a href="{back_url}" style="display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-decoration: none; border-radius: 6px; font-weight: 500; transition: background 0.2s;">⬅ Quay lại thử lại</a>
    </div>
    """
    return content


# ==========================================
# 1. ROUTER ROUTES FOR DISPLAYING PAGES (GET)
# ==========================================

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')


# ==========================================
# 2. CAESAR CIPHER ROUTES (POST)
# ==========================================

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form.get('inputPlainText', '').strip()
    key_raw = request.form.get('inputKeyPlain', '').strip()
    
    if not text or not key_raw:
        return render_result_template("Caesar Encryption Error", text, key_raw, "Vui lòng điền đầy đủ Plain Text và Key!", is_error=True, back_url="/caesar")
    
    try:
        key = int(key_raw)
    except ValueError:
        return render_result_template("Caesar Encryption Error", text, key_raw, "Khóa của Caesar bắt buộc phải là số nguyên!", is_error=True, back_url="/caesar")
        
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_result_template("Caesar Encryption Result", text, key, encrypted_text, back_url="/caesar")

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form.get('inputCipherText', '').strip()
    key_raw = request.form.get('inputKeyCipher', '').strip()
    
    if not text or not key_raw:
        return render_result_template("Caesar Decryption Error", text, key_raw, "Vui lòng điền đầy đủ Cipher Text và Key!", is_error=True, back_url="/caesar")
        
    try:
        key = int(key_raw)
    except ValueError:
        return render_result_template("Caesar Decryption Error", text, key_raw, "Khóa của Caesar bắt buộc phải là số nguyên!", is_error=True, back_url="/caesar")
        
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_result_template("Caesar Decryption Result", text, key, decrypted_text, back_url="/caesar")


# ==========================================
# 3. VIGENÈRE CIPHER ROUTES (POST)
# ==========================================

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip() # GIỮ NGUYÊN KIỂU CHUỖI, KHÔNG ÉP KIỂU INT
    
    clean_key = "".join([c for c in key if c.isalpha()])
    if not clean_key:
        return render_result_template("Vigenère Encryption Error", text, key, "Khóa không hợp lệ!", is_error=True, back_url="/vigenere")
        
    cipher = VigenereCipher()
    encrypted_text = cipher.encrypt_text(text, clean_key)
    return render_result_template("Vigenère Encryption Result", text, clean_key, encrypted_text, back_url="/vigenere")

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form.get('inputCipherText', '')
    key = request.form.get('inputKeyCipher', '').strip()
    
    clean_key = "".join([c for c in key if c.isalpha()])
    if not clean_key:
        return render_result_template("Vigenère Decryption Error", text, key, "Khóa không hợp lệ! Vigenère bắt buộc khóa phải là chuỗi chữ cái (A-Z).", is_error=True, back_url="/vigenere")
        
    cipher = VigenereCipher()
    decrypted_text = cipher.decrypt_text(text, clean_key)
    return render_result_template("Vigenère Decryption Result", text, clean_key, decrypted_text, back_url="/vigenere")


# ==========================================
# 4. RAIL FENCE CIPHER ROUTES (POST)
# ==========================================

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form.get('inputPlainText', '')
    key_raw = request.form.get('inputKeyPlain', '').strip()
    
    try:
        key = int(key_raw)
        if key < 2:
            raise ValueError
    except ValueError:
        return render_result_template("Rail Fence Encryption Error", text, key_raw, "Khóa số tầng (Rails) phải là số nguyên và lớn hơn hoặc bằng 2!", is_error=True, back_url="/railfence")
        
    cipher = RailFenceCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return render_result_template("Rail Fence Encryption Result", text, key, encrypted_text, back_url="/railfence")

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form.get('inputCipherText', '')
    key_raw = request.form.get('inputKeyCipher', '').strip()
    
    try:
        key = int(key_raw)
        if key < 2:
            raise ValueError
    except ValueError:
        return render_result_template("Rail Fence Decryption Error", text, key_raw, "Khóa số tầng (Rails) phải là số nguyên và lớn hơn hoặc bằng 2!", is_error=True, back_url="/railfence")
        
    cipher = RailFenceCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return render_result_template("Rail Fence Decryption Result", text, key, decrypted_text, back_url="/railfence")


# ==========================================
# 5. PLAYFAIR CIPHER ROUTES (POST)
# ==========================================

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    
    # Ràng buộc: Khóa ma trận Playfair phải có ít nhất 1 chữ cái để tạo lập
    clean_key = "".join([c for c in key if c.isalpha()])
    if not clean_key:
        return render_result_template("Playfair Encryption Error", text, key, "Khóa không hợp lệ! Playfair bắt buộc phải sử dụng chuỗi chữ cái để tạo ma trận.", is_error=True, back_url="/playfair")
        
    cipher = PlayFairCipher()
    encrypted_text = cipher.encrypt_text(text, clean_key)
    return render_result_template("Playfair Encryption Result", text, clean_key, encrypted_text, back_url="/playfair")

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form.get('inputCipherText', '')
    key = request.form.get('inputKeyCipher', '').strip()
    
    clean_key = "".join([c for c in key if c.isalpha()])
    if not clean_key:
        return render_result_template("Playfair Decryption Error", text, key, "Khóa không hợp lệ! Playfair bắt buộc phải sử dụng chuỗi chữ cái để giải mã.", is_error=True, back_url="/playfair")
        
    cipher = PlayFairCipher()
    decrypted_text = cipher.decrypt_text(text, clean_key)
    return render_result_template("Playfair Decryption Result", text, clean_key, decrypted_text, back_url="/playfair")


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)