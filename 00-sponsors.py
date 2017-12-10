import base64

# The sponsors page has some puzzles. I try to solve them here.

# SmartyStreets
indata = b"U2VuZGluZyBDaH Jpc3RtYXMgY2Fy ZHMgdG8gYmFkIG FkZHJlc3Nlcz8K"
print("SmartyStreets puzzle:", base64.decodebytes(indata).decode('ascii'), end="")

# Cheppers linkedin challenge
# https://www.linkedin.com/pulse/advent-code-challenge-ala-cheppers-you-ready-gergely-brautigam/


def xor(text, key):
    result = []
    for i, c in enumerate(text):
        key_byte = key[i % len(key)]
        result.append(c ^ key_byte)
    return bytes(result)


def rot13(s):
    # Stolen from /usr/lib/python3.6/this.py
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    return "".join([d.get(c, c) for c in s])


data = b"4oqVKEhnZ0pBZ3RUUkVBZUZCOEtDQjBMQjBNWkNSVkJNd3dSSXg4Y0VBb0hIUXdkQXgwSENnPT0sIOKGkeKGkeKGk+KGk+KGkOKGkuKGkOKGkkJBKQ=="
decoded = base64.decodebytes(data).decode('utf-8')
# ⊕(HggJAgtTREAeFB8KCB0LB0MZCRVBMwwRIx8cEAoHHQwdAx0HCg==, ↑↑↓↓←→←→BA)
key='konami'.encode('utf-8')
data2 = b"HggJAgtTREAeFB8KCB0LB0MZCRVBMwwRIx8cEAoHHQwdAx0HCg=="
txt = base64.decodebytes(data2)
print("result", rot13(xor(txt, key).decode('utf-8')))

# Cheppers
# xor(Pz0pQUI7Ch cmER8YDAEYAh4L GwEP, ↑↑↓↓←→←→BA)

key = b"konami"
data = b"Pz0pQUI7Ch cmER8YDAEYAh4L GwEP"
decoded = base64.decodebytes(data)

print("Cheppers:", rot13(xor(decoded, key).decode('utf-8')))
