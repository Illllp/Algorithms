'''
23. Дан список, содержащий запись неотрицательных целых чисел в двоичной системе счисления.
Заменить каждый элемент списка на его запись в шестнадцатеричной системе счисления. 
'''
# conversion from binary to hexadecimal


a = ['10000', '11001', '1111']

# An important class for specifying the beginning and end


class Node:

    def __init__(self, data):

        self.next = None
        self.data = data

    def binToHex(self, bin):

        for i in range(len(bin)):

            num = int(bin[i], 2)  # We point the program to the binary
            hex_num = format(num, 'x')  # Specify the translation format
            bin[i] = hex_num  # Output the hexadecimal system alternately


ll = Node(a)
ll.binToHex(a)


print(ll.data)
