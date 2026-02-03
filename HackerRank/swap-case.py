def swap_case(s):
    ans = ""
    for char in s:
        if char.isalpha() and char.isupper():
            char = char.lower()
        elif char.isalpha and char.islower():
            char = char.upper()
        ans+=char
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)