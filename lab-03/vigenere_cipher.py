import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow  
import requests

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 👤 Cá nhân hóa tiêu đề cửa sổ giao diện
        self.setWindowTitle("VIGENERE CIPHER - Nguyen Chi Tam (MSSV: 2380601979)")
        
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip().replace(" ", "")
        
        if not plain_text or not key:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ Plain Text và Key!")
            return
            
        if not key.isalpha():
            QMessageBox.warning(self, "Cảnh báo", "Key của Vigenere chỉ được phép chứa các chữ cái!")
            return

        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {"plain_text": plain_text, "key": key}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_text"])
                QMessageBox.information(self, "Thành công", "Vigenere Encrypted successfully")
            else:
                print(f"Error while calling API: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            
    def call_api_decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip().replace(" ", "")
        
        if not cipher_text or not key:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đầy đủ Cipher Text và Key!")
            return
            
        if not key.isalpha():
            QMessageBox.warning(self, "Cảnh báo", "Key của Vigenere chỉ được phép chứa các chữ cái!")
            return

        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {"cipher_text": cipher_text, "key": key}
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_text"])
                QMessageBox.information(self, "Thành công", "Vigenere Decrypted successfully")
            else:
                print(f"Error while calling API: Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())