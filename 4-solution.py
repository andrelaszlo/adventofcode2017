with open('4-input.txt') as f:
    data = f.readlines()

indata = [line.strip().split(' ') for line in data]

def valid_passphrase(passphrase):
    s = set()
    for word in passphrase:
        if word in s:
            return False
        s.add(word)
    return True

def valid_passphrase2(passphrase):
    s = set()
    for word in passphrase:
        word = ''.join(sorted(word))
        if word in s:
            return False
        s.add(word)
    return True

solution1 = sum(1 if valid_passphrase(passphrase) else 0 for passphrase in indata)
print("Solution 1:", solution1)

solution2 = sum(1 if valid_passphrase2(passphrase) else 0 for passphrase in indata)
print("Solution 2:", solution2)
