def generate_table(original_list: list[dict[str:list]]) -> dict[bool:list[str]]:
    status = True
    markdown = ""
    error_message = ""
    markdown_dict = dict()
    error_dict = dict()

    for original in original_list:
        column = 0
        row = 0
        for key, value in original.items():
            if key == "thead":
                column = len(value[0])
                for i in value[0]:
                    markdown += "|" + i
                markdown += "|"
                markdown += "\n"
                for i in range(column):
                    markdown += "|:-:"
                markdown += "|"
            elif key == "tbody":
                markdown += "\n"
                row = len(value)
                for i in range(row):
                    for j in value[i]:
                        markdown += "|" + j
                    markdown += "|"
                    markdown += "\n"
                markdown = markdown[:-1]
                # print(markdown)
                markdown_dict[status] = markdown
            else:
                status = False
                error_message = "Incorrect table format"
                error_dict[status] = error_message
                break

        if status:
            return markdown_dict
        else:
            return error_dict


if __name__ == "__main__":
    original = list()
    original.append({'thead': [['auto', 'enum', 'unsigned', 'break', 'extern']],
                     'tbody': [['return', 'void', 'case', 'float', 'short'],
                               ['volatile', 'char', 'for', 'signed', 'while'],
                               ['const', 'goto', 'sizeof', 'continue', 'if'],
                               ['static', 'default', 'struct', 'do', 'int'],
                               ['switch', 'double', 'long', 'typedef', 'else'], ['register', 'union'],
                               ['restrict', 'inline', '_Bool', '_Complex', '_Imaginary']]})
    result: dict[bool:str] = generate_table(original)
    print(result)
    print("\n")
    for status, markdown in result.items():
        print(status)
        print(markdown)
