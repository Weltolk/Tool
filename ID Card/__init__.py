def check(id_str: str) -> bool:
    id_list = list(id_str)
    ten = ['X', 'x', 'Ⅹ']
    ID = ["10" if x in ten else x for x in id_list]  # 将罗马数字Ⅹ和字母X替换为10
    W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    sum = 0
    for i in range(17):
        sum = sum + int(ID[i]) * W[i]
    if Checkcode[sum % 11] == int(ID[17]):
        return True
    else:
        return False


if __name__ == "__main__":
    pass
