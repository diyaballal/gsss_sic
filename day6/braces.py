import sys
input_str=sys.argv[1]
print(f'User given input is {input_str}')
def braces_check(s):
    count1=0
    count2=0

    for ch in s:
        if ch == '{':
            count1 +=1
        elif ch == '}':
            count2 +=1

        if count1 == count2:
            print("It is balanced")
        elif count2 > count1:
            print("It is not balanced.")

print(braces_check(input_str))