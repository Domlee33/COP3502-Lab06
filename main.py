# Lab 6
# Started by Dominick Lee

def encode(nums):
    enco = ''
    for i in nums:
        i = int(i)
        if i < 7:
            enco += str(i + 3)
        else:
            enco += str(i - 7)
    return enco

def decode(password):  # decode function coded by Joseph Mackle
    decoded = ""
    for i in range(len(password)):
        j = int(password[i]) - 3
        if j < 0: j += 10  # account for numbers going negative
        decoded += str(j)
    return decoded

if __name__ == '__main__':
    ans = ""  # initialize variable here so it can be accessed in later loops
    while True:
        print('Menu\n-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        choice = int(input('Please enter an option: '))

        if choice == 1:
            code = input('Please enter your password to encode: ')
            ans = encode(code)
            print('Your password has been encoded and stored!')
        if choice == 2:
            print(f'The encoded password is {ans}, and the original password is {decode(ans)}.')
        if choice == 3:
            break

        print()


