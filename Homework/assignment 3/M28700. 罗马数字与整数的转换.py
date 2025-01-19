roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

int_to_roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

#罗马数字转整数
def roman_to_int(s):
    total = 0
    prev_value = 0
    for char in s:
        value = roman_to_int_map[char]
        if value > prev_value:
            total += value - 2 * prev_value  # 处理特殊情况，如IV, IX
        else:
            total += value
        prev_value = value
    return total

#整数转罗马数字
def int_to_roman(num):
    result = []
    for value, symbol in int_to_roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)

def main():
    input_data = input().strip()

    if input_data.isdigit():
        #输入整数
        num = int(input_data)
        print(int_to_roman(num))
    else:
        #输入罗马数字
        print(roman_to_int(input_data))

if __name__ == "__main__":
    main()