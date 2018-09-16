import sys
script , encoding , error = sys.argv

def main(language_file , encoding , errors):
    line = language_file.readline()
    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors)

def print_line(line , encoding , errors):
    #strip 去掉头尾的空格或者换行符
    next_line = line.strip()
    #对每行的文字进行utf-8编码
    raw_bytes = next_line.encode(encoding , errors = errors)
    #对编码后的字节进行解码
    cooked_string = raw_bytes.decode(encoding,errors = errors)

    print(raw_bytes,"<===>",cooked_string)

languages = open("f://common//atom//languages.txt",encoding="utf-8")

main(languages, encoding , error)
