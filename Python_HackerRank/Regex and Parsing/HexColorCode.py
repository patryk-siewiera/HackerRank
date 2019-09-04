import re


def regex_checker(check_this):
    patern_all = re.compile(r'\#\w{3,6}')

    # search all paterns
    search_all = re.findall(patern_all, check_this)
    print(search_all)

    # search css selectors
    patern_delete = re.compile(r'\#\w{3,6}\n')
    search_delete = re.findall(patern_delete, check_this)
    for i in range(len(search_delete)):
        temp = search_delete[i]
        temp = temp[:-1]
        search_delete[i] = temp
    print(search_delete)

    # delete duplicats
    final_score = []

    # tutaj !!!!!!!!!!

    for p in search_all:
        for o in range(len(search_delete)):
            if (search_delete[o] == p):
                # #### tu
                search_all.remove(p)
                continue

    print(final_score)


def input_data():
    amount = int(input())
    my_list = []
    for i in range(amount):
        my_list.append(input())
    score = ('\n'.join(my_list))
    return score


def sample_input():
    my_str = """11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
    """
    return my_str


output_str = input_data()

regex_checker(output_str)
