import hashlib


def generator(file):
    with open(file) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in generator('C:\\Users\\Anastasia\\PycharmProjects\\HW_2.4.2\\file.txt'):
    print(item)