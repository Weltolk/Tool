def generate_table(original: dict) -> dict[bool:dict[str:list]]:


if __name__ == "__main__":
    original = {'thead': [['auto', 'enum', 'unsigned', 'break', 'extern']],
                       'tbody': [['return', 'void', 'case', 'float', 'short'],
                                 ['volatile', 'char', 'for', 'signed', 'while'],
                                 ['const', 'goto', 'sizeof', 'continue', 'if'],
                                 ['static', 'default', 'struct', 'do', 'int'],
                                 ['switch', 'double', 'long', 'typedef', 'else'], ['register', 'union', '', '', ''],
                                 ['<em>restrict</em>', '<em>inline</em>', '<em>_Bool</em>', '<em>_Complex</em>',
                                  '<em>_Imaginary</em>']]}
    result: dict = generate_table(original)
    # print(result)
    for i, j in result.items():
        for k, l in j.items():
            print(k, l)
