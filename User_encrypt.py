def text_to_unicode(text):
    if text=='':
        text='EMPTY_STRING'
    unicode_list = [f"{ord(char):05}" for char in text] 
    unicode_str = ''.join(unicode_list) 
    import sys
    str_length = len(unicode_str)
    if str_length > 4300:
        sys.set_int_max_str_digits(len(unicode_str))
    return int(unicode_str)

def encrypt(M, C_prime, D_prime):
    """加密算法：E = M * C' + D'"""
    return M * C_prime + D_prime

C_prime_padded = 'Here is Public Key C'
D_prime_padded = 'Here is Public Key D'
text = input('请输入需要加密的文本:\n\t')
M = text_to_unicode(text)
E = encrypt(M, C_prime_padded, D_prime_padded)
print(f"加密后的密文\n\t{E}")
