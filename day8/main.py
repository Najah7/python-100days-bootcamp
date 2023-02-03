# Project Caesar Cipher

# 文字数を指定の文字数分ずらす暗号
import sys

from art import LOGO

sys.path.append('../utils')
from input_helper import int_input, yes_no_input

# NOTE:文字コードを使わずにアルファベットのリストを用意して暗号化していた。
# メモリの消費量も微細なので、アルファベットのリストを使った方がいいかも...。加えて、アルファベットのリストを使うと関数を一つにできる。
# NOTE:アルファベットのリストを2周分ならべることで、zなど最後の方の数字の場合のifを省略できる。

def main():
    
    print(LOGO)
    
    is_continue = True
    
    while is_continue:
        
        user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        
     
        if user_choice == 'encode':
            
            # get user input
            plain_msg = input("Type your message: ").lower()
            num_shift = int_input("Type the Shift number: ")
            
            # HACK:初期値としてmsgとnum_shiftを渡す感じでOK？（インタフェースの設計に改善の余地あり）
            # make Caesar instancd and encrypt
            caesar = Caesar(plain_msg, num_shift)
            encoded_msg = caesar.encrypt()
            
            # print output 
            print(f"Here's the encoded result : {encoded_msg}")
            
        elif user_choice == 'decode':
            
            # # get user input
            encoded_msg = input("Type your encoded message: ")
            num_shift = int_input("Type the Shift number: ")
            
            # make Caesar instancd and decrypt
            caesar = Caesar(encoded_msg, num_shift)
            plain_msg = caesar.decrypt()
            
            # print output 
            print(f"Here's the decoded result : {plain_msg}")
        
        
        is_continue = ask_user()
       
        
class Caesar:
    
    # HACK:encryptとdecryptの関数、共通部分が多い。まとめられる可能性大。しかしインタフェース的には関数は分けておいた方がいいかも？
    
    def __init__(self, message, num_shift):
        # HACK:ASCII関係の値はプロパティでOK？
        self.__NUM_ALPHABET = 26
        self.__ASCII_CODE_OF_a = 97
        self.__ASCII_CODE_OF_z = 122
        self._message = message
        self._num_shift = num_shift
    
    def is_letter(self, letter):
        ascii_code = ord(letter)
        if self.__ASCII_CODE_OF_a <= ascii_code <= self.__ASCII_CODE_OF_z:
            return True
        return False
        

    def _encrypt_char(self, letter):
        # NOTE:ord関数はOrdinal（順序）の略
        # NOTE:小文字を受け取るようにしているので、最後のzは一応小文字にした。
        
        if not self.is_letter(letter):
            return letter
        
        ascii_code = ord(letter)
        
        
        encrypted_code = ascii_code + self._num_shift
        while self.__ASCII_CODE_OF_z < encrypted_code:
            encrypted_code -= self.__NUM_ALPHABET
        
        encrypted_letter = chr(encrypted_code)
        
        return encrypted_letter
    
    def _decrypt_char(self, letter):
        # NOTE:ord関数はOrdinal（順序）の略
        
        if not self.is_letter(letter):
            return letter
        
        ascii_code = ord(letter)

        decrypted_code = ascii_code - self._num_shift
        while decrypted_code < self.__ASCII_CODE_OF_a:
            decrypted_code += self.__NUM_ALPHABET
        
        decrypted_letter = chr(decrypted_code)
        
        return decrypted_letter

    # You can use it for string
    def encrypt(self):
        
        encrypted_message = list()
        for letter in self._message:
            encrypted_message.append(self._encrypt_char(letter))
            
        return ''.join(encrypted_message)

    # You can use it for string
    def decrypt(self):
        
        decrypted_message = list()
        for letter in self._message:
            decrypted_message.append(self._decrypt_char(letter))
            
        return ''.join(decrypted_message)


def ask_user():
    return yes_no_input("Type yes if you want to go again. Otherwise type 'no' ")
    
    
if __name__ == '__main__':
    main()