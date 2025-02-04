#Read the birthdate year of a young man and according to your age          Your program need to show how much time last or passed to enlist
#If he is still going to enlist in the military service     If it's time to enlist      If the time to enlist passed
year = int(input('Digit your birthdate year: '))
yearold = 2025 - year
if yearold < 18:
    tpm = 18 - yearold
    print('\033[33mYou will still enlist in the military service')
    print('Time left until enlist: {} years'.format(tpm))
elif yearold == 18:
    print('\033[32mIts time to enlist in the military service!!!!')
else:
    tpm = yearold - 18
    print('\033[35mThe time to enlist has passed.')
    print('Time passed to enlist: {} years'.format(tpm))