def mutate_string(string, position, character):
    string = ""
    string = list(s)
    string[position] = c
    return "".join(string)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
