def generate_password(n):
    string = ''
    list_ = []
    for i in range(1,21):
        for j in range(i + 1,21):
            sum_ =  i + j
            if n % sum_ == 0:
                str_ = f'{i}{j}'
                if str_ not in list_ :
                    list_.append(str_)
                    string += str_
    return string

for first_num in range(3,21):
    password = generate_password(first_num)
    print(f'{first_num} - {password}')



