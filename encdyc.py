class PasswordEncryptDecrypt:
    '''encrypts and decrypts password'''
    def __init__(self, shift):
        self.shifter=shift
        self.s=self.shifter%26
  
    def _convert(self, text,s):
        '''encrypts/decrypts the password'''
        result=""
        for i,ch in enumerate(text):     
             if (ch.isupper()):
                  result += chr((ord(ch) + s-65) % 26 + 65)
             else:
                  result += chr((ord(ch) + s-97) % 26 + 97)
        return  result
  
    def encrypt(self, text):
        '''encrypts the password'''
        return self._convert(text,self.shifter)
        
    def decrypt(self, text):
        '''decrypts the password'''
        return self._convert(text,26-self.s) 