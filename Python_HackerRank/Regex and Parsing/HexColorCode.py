import re

def user_input():
    amount = int(input())
    my_list = []
    for i in range(amount):
        my_list.append(input())
    score = ('\n'.join(my_list))
    return score

def sample_input():
    my_str = """5
.shadow {
-moz-box-shadow: inset 0 0 10px #000000;
-webkit-box-shadow: inset 0 0 10px #000000;
box-shadow: inset 0 0 10px #0z00G0;
}
    """
    return my_str

def parse_between_brackets(str_to_parse):
    patern = re.compile(r'{(?:[^{}]*{[^{]*})*[^{}]*}')
    search = re.findall(patern, str_to_parse)
    search = "\n".join(search)
    return search

def parse_hex_code(str_to_parse):
    patern_all = re.compile(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b')
    search_all = re.findall(patern_all, str_to_parse)
    for i in search_all:
        print(i)

# my_input = user_input()
my_input = sample_input()
output_text_brackets = parse_between_brackets(my_input)
parse_hex_code(output_text_brackets)
