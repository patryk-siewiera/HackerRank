# 6 kyu
#
# A strem of data is received and needs to be reversed.
#
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
#
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:
#
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.
#
# The data is given in an array as such:
#
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.
#

def data_reverse(data):
    list_data = []
    for i in range(len(data) // 8):
        temp = data[(i * 8):((i + 1) * 8)]
        temp = "".join(str(temp))
        list_data.append(str(temp))
    reverse_list = list_data[::-1]
    join_list = "".join(reverse_list)
    return join_list


data3 = [0, 0, 1, 1, 0, 1, 1, 0,
         0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1,
         0, 0, 1, 1, 0, 1, 1, 0]

print("return data3: \n\t\t", data_reverse(data3), "\n")
# print(data_reverse(data3) == data4)
