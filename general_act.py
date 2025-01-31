def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_max_prime_factor(n):
    max_prime = 1
    n = int(n)
    for i in range(2, 101): 
        if n % i == 0 and is_prime(i):
            max_prime = i
    return max_prime

def reverse_number(n):
    return int(str(n)[::-1])

def calculate_c(a, b):
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]
    c = sum([a_d * b_d for a_d, b_d in zip(a_digits, b_digits)])
    return c

def generate_d(a):
    digits = sorted([int(d) for d in str(a)])
    d = int(''.join(map(str, digits)))
    return d

def pad_to_128_bits(number):
    num_str = str(number)
    padded_str = num_str
    while len(padded_str) < 128:
        padded_str += num_str[len(padded_str) % len(num_str)]
    return int(padded_str[:128])

def encrypt(M, C_prime, D_prime):
    return M * C_prime + D_prime

def decrypt(E, C_prime, D_prime):
    return (E - D_prime) // C_prime

    
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

def unicode_to_text(number):
    unicode_str = str(number)
    length = len(unicode_str)
    if length>=5:
        r = length % 5
        if r != 0:
            for _ in range(r+1):

                unicode_str = "0" + unicode_str
    else:
        r = 5-length
        for _ in range(r):
            unicode_str = '0' + unicode_str
            
    # print(f"补0后的unocode码{unicode_str}\n")        
    text = ''
    for i in range(0, len(unicode_str), 5): 
        code_point = int(unicode_str[i:i+5]) 
        text += chr(code_point)
        if text=="EMPTY_STRING":
            text=''
    return text


if  __name__ == '__main__':
    import os
    import random

    # here is encrypt.py

    # random.seed(uer_id) ## 有这个想法来着, 每个用户的id都是不一样的，所以他们对应的随机数也不一样
    # 于是私钥公钥也不一样
    # 所以不能用自己的公钥来解开别人的锁
    
    folder_path = 'private_key'
    key = os.path.join(folder_path, "private_key.txt")
    if not os.path.exists(key):
        try:
            os.makedirs(folder_path)
        except:
            pass
        A = ''.join([str(random.randint(0, 9)) for _ in range(256)])
        with open(key, 'w', encoding='utf-8') as f:
            f.write(A)
    else:
        with open(key, 'r', encoding='utf-8') as f:
            A  = f.read()
            if A == '':
                A = ''.join([str(random.randint(0, 9)) for _ in range(256)])
            else:
                A == int(A)
     
    B = reverse_number(A)
    C = calculate_c(A, B)
    D = generate_d(A)
    X = get_max_prime_factor(A)
    C_prime = C * X
    D_prime = D * X
    C_prime_padded = pad_to_128_bits(C_prime)
    D_prime_padded = pad_to_128_bits(D_prime)

    print(f"公钥C={C_prime_padded}")
    print(f"公钥D={D_prime_padded}")

    # 解密
    E = int(input("请输入密文\n\t"))
    M_decrypted = decrypt(E, C_prime_padded, D_prime_padded)
    # print(f"解密后的 Unicode 整数: {M_decrypted}\n")

    # 3. Unicode 整数转文本
    decrypted_text = unicode_to_text(M_decrypted)
    print(f"解密后的文本: {decrypted_text}\n")




