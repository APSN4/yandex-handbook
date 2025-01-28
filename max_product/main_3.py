count = int(input())
data = list(map(int, input().split()))

class FixedSizeStructure:
    def __init__(self, limit=3):
        self.limit = limit
        self.elements = []

    def add(self, num):
        self.elements.append(num)

        if len(self.elements) > self.limit:
            min_val = min(self.elements)
            self.elements.remove(min_val)

struct = FixedSizeStructure(3)

for i in range(count):
    if len(struct.elements) < 3:
        struct.elements.append(data[i])
        continue
    struct.add(data[i])

print(struct.elements[0] * struct.elements[1] * struct.elements[2])