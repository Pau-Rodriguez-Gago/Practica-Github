a = int(input())
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
if a <= 9  and a > 0:
    print(nums[a - 1])
else:
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
    