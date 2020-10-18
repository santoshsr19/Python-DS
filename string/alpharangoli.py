import string

alpha = string.ascii_lowercase


def nrange(N):
    return list(range(N)) + list(range(N - 2, -1, -1))


def print_rangoli(size):
    for i in nrange(size):
        print('-'.join([alpha[size - j - 1] for j in nrange(i + 1)]).center(4 * (size - 1) + 1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)