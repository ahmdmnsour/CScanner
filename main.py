from scanner import Scanner

if __name__ == '__main__':
    file_path = input("Please enter the file path\n")

    sc = Scanner(file_path)
    tok = sc.get_token()

    while tok.get_symbol() != -1:
        print(tok)
        tok = sc.get_token()
