input_file = open('input.txt', 'r')
input_arr=[]
for n in input_file:
    input_arr.append(n.strip())

gamma_binary = ""
epsilon_binary = ""
binary_count = { '1': 0,
           '0': 0 }

for i in range(len(input_arr[0])):
    for b in range(len(input_arr)):
        binary = input_arr[b]
        bit = binary[0]
        if bit == '1':
            binary_count['1'] += 1
        else:
            binary_count['0'] += 1
        input_arr[b] = binary[1:]
    if binary_count['1'] > binary_count['0']:
        gamma_binary += '1'
        epsilon_binary += '0'
    else:
        gamma_binary += '0'
        epsilon_binary += '1'
    binary_count = { '1': 0,
           '0': 0 }
gamma = int(gamma_binary, 2)
epsilon = int(epsilon_binary, 2)            

print(gamma * epsilon)
