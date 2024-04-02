# 對話紀錄處理-格式改寫
# 改寫input.txt檔案的格式，變成像output.txt的檔案格式

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    person = None   # 用來避免輸入檔案中第一行不是人名，而導致程式當掉的情況
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:                  # 如果person有值, 才做這行
            new.append(person + ': ' + line)
    return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()