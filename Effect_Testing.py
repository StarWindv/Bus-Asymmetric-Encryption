from 公私密钥 import *

def calculate_hamming_distance(bin1, bin2):
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))

def calculate_bit_change_rate(bin1, bin2):
    total_bits = len(bin1)
    changed_bits = calculate_hamming_distance(bin1, bin2)
    return changed_bits / total_bits

def test_avalanche_effect(text1, text2):
    M1 = text_to_unicode(text1)
    E1 = encrypt(M1, C_prime_padded, D_prime_padded)
    bin1 = bin(E1)[2:][-128:].zfill(128)

    M2 = text_to_unicode(text2)
    E2 = encrypt(M2, C_prime_padded, D_prime_padded)
    bin2 = bin(E2)[2:][-128:].zfill(128)

    hamming_distance = calculate_hamming_distance(bin1, bin2)
    bit_change_rate = calculate_bit_change_rate(bin1, bin2)

    return hamming_distance, bit_change_rate

def test_key_sensitivity(text, key1, key2):
    B1 = reverse_number(key1)
    C1 = calculate_c(key1, B1)
    D1 = generate_d(key1)
    X1 = get_max_prime_factor(key1)
    C_prime1 = C1 * X1
    D_prime1 = D1 * X1
    C_prime_padded1 = pad_to_128_bits(C_prime1)
    D_prime_padded1 = pad_to_128_bits(D_prime1)
    E1 = encrypt(text_to_unicode(text), C_prime_padded1, D_prime_padded1)
    bin1 = bin(E1)[2:][-128:].zfill(128)

    B2 = reverse_number(key2)
    C2 = calculate_c(key2, B2)
    D2 = generate_d(key2)
    X2 = get_max_prime_factor(key2)
    C_prime2 = C2 * X2
    D_prime2 = D2 * X2
    C_prime_padded2 = pad_to_128_bits(C_prime2)
    D_prime_padded2 = pad_to_128_bits(D_prime2)
    E2 = encrypt(text_to_unicode(text), C_prime_padded2, D_prime_padded2)
    bin2 = bin(E2)[2:][-128:].zfill(128)

    hamming_distance = calculate_hamming_distance(bin1, bin2)
    bit_change_rate = calculate_bit_change_rate(bin1, bin2)

    return hamming_distance, bit_change_rate

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def test_collision_resistance(num_tests=1000000):
    seen_hashes = set()
    for _ in range(num_tests):
        text = generate_random_text(1000)
        M = text_to_unicode(text)
        E = encrypt(M, C_prime_padded, D_prime_padded)
        if E in seen_hashes:
            print(f"发现碰撞: {text}")
            return False
        seen_hashes.add(E)
    print("抗碰撞测试: 通过")
    return True

import string
import time

def test_encryption_speed(text):
    start_time = time.time()
    M = text_to_unicode(text)
    E = encrypt(M, C_prime_padded, D_prime_padded)
    end_time = time.time()
    return end_time - start_time

def test_boundary_conditions():
    """测试边界条件"""
    test_cases = [
        "",  # 空输入
        "A",  # 单个字符
        "A" * 100000,  # 1MB 数据
        ]

    for text in test_cases:
        try:
            M = text_to_unicode(text)
            E = encrypt(M, C_prime_padded, D_prime_padded)
            M_decrypted = decrypt(E, C_prime_padded, D_prime_padded)
            decrypted_text = unicode_to_text(M_decrypted)
            assert decrypted_text == text, f"边界条件测试失败: {text}"
            print(f"边界条件测试通过: {text[:20]}...")  # 只打印前 20 个字符
        except Exception as e:
            print(f"边界条件测试失败: '{text}' - {e}")


    '''
    base_text = "Hello, World!"
    modified_text = "Hello, World?"
    # 测试雪崩效应
    hamming_distance, bit_change_rate = test_avalanche_effect(base_text, modified_text)
    print(f"汉明距离: {hamming_distance}")
    print(f"比特变化率: {bit_change_rate:.2%}")

    test_cases = [
    ("Hello, World!", "Hello, World?"),
    ("Cryptography", "Cryptographz"),
    ("Secure Algorithm", "Secure Algorithn"),
    ("Test Input", "Test Inpuz"),
]

    total_hamming_distance = 0
    total_bit_change_rate = 0
    num_tests = len(test_cases)

    for text1, text2 in test_cases:
        hamming_distance, bit_change_rate = test_avalanche_effect(text1, text2)
        total_hamming_distance += hamming_distance
        total_bit_change_rate += bit_change_rate

    avg_hamming_distance = total_hamming_distance / num_tests
    avg_bit_change_rate = total_bit_change_rate / num_tests

    print(f"平均汉明距离: {avg_hamming_distance}")
    print(f"平均比特变化率: {avg_bit_change_rate:.2%}")

    text = "Hello, World!"
    key1 = "1234567890123456789012345678901234567890123456789012345678901234"
    key2 = "1234567890123456789012345678901234567890123456789012345678901235"  # 只改变最后一位

    hamming_distance, bit_change_rate = test_key_sensitivity(text, key1, key2)
    print(f"密钥敏感性测试 - 汉明距离: {hamming_distance}")
    print(f"密钥敏感性测试 - 比特变化率: {bit_change_rate:.2%}")

    text_short = "A" * 1000  # 1KB
    text_medium = "A" * 10000  # 10KB
    text_large = "A" * 100000  # 100KB

    time_short = test_encryption_speed(text_short)
    time_medium = test_encryption_speed(text_medium)
    time_large = test_encryption_speed(text_large)

    print(f"加密 1KB 数据所需时间: {time_short:.4f} 秒")
    print(f"加密 10KB 数据所需时间: {time_medium:.4f} 秒")
    print(f"加密 100KB 数据所需时间: {time_large:.4f} 秒")
    # test_collision_resistance()
    
    test_boundary_conditions()
    '''
