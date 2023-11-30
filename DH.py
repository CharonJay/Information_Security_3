import random
import pandas as pd


def one_way_f(p, g, x):
    y = (g ** x) % p
    return y


def generate_private_int(seed):
    random.seed(seed)
    key = random.randint(0, 2023)
    return key


def DH(p, g):
    print(f"---------------p = {p}, g = {g}---------------")

    # 分别生成私密整数
    private_int1 = generate_private_int(p + 1)
    private_int2 = generate_private_int(p + 2)
    print(f"用户1的秘密数字: {private_int1} || 用户2的秘密数字: {private_int2}")

    # 分别根据秘密数字生成公钥
    public_key1 = one_way_f(p, g, private_int1)
    public_key2 = one_way_f(p, g, private_int2)
    print(f"用户1生成的公钥: {public_key1} || 用户2生成的公钥: {public_key2}")

    # 交换公钥后求解密钥
    private_key1 = one_way_f(p, public_key2, private_int1)
    private_key2 = one_way_f(p, public_key1, private_int2)
    print(f"用户1求解的密钥: {private_key1} || 用户2求解的密钥: {private_key2}")

    result = [private_int1, private_int2, public_key1, public_key2, private_key1, private_key2]
    return result


if __name__ == "__main__":
    P_G = [
        [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
         223, 227, 229, 233, 239, 241, 251],
        [2, 5, 2, 6, 3, 3, 2, 3, 2, 2, 2, 2, 6, 5, 2, 2, 2, 19, 5, 2, 3, 2, 3, 2, 6, 3, 7, 7, 6]]
    DH(107, 227)

    result_table = pd.DataFrame({
        'p': [],
        'g': [],
        '用户1的秘密数字': [],
        '用户2的秘密数字': [],
        '用户1生成的公钥': [],
        '用户2生成的公钥': [],
        '用户1求解的密钥': [],
        '用户2求解的密钥': []
    })

    for i in range(len(P_G[0])):
        P = P_G[0][i]
        G = P_G[1][i]
        result = DH(P, G)
        result.insert(0, G)
        result.insert(0, P)
        result_table.loc[result_table.shape[0]] = result

    result_table.to_csv("D-H实验结果.csv", encoding="utf_8_sig")