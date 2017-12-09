with open('2-input.txt') as f:
    data = f.read().strip()

rows = [[int(c.strip()) for c in row.split('\t')] for row in data.splitlines()]
checksum = sum(max(row) - min(row) for row in rows)
print("Checksum:", checksum)

def find_divisors(row):
    for a in row:
        for b in row:
            if a%b == 0 and a != b:
                return a//b

checksum2 = sum(find_divisors(row) for row in rows)
print("Checksum 2:", checksum2)
