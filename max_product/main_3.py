count = int(input())
data = list(map(int, input().split()))

class FixedSizeStructure:
    def __init__(self, limit=3):
        self.limit = limit
        self.elements = []
        self.negative_elements = []

    def add(self, num):
        self.elements.append(num)

        if len(self.elements) > self.limit:
            min_val = min(self.elements)
            self.elements.remove(min_val)
        if num < 0:
            self.add_negative_number(num)

    def add_negative_number(self, num):
        self.negative_elements.append(num)

        if len(self.negative_elements) > self.limit:
            max_val = max(self.negative_elements)
            self.negative_elements.remove(max_val)

    def get_result(self):
        max_val = max(self.elements)
        min_val_negative = 0
        for i in self.negative_elements:
            if 0 < i < min_val_negative:
                min_val_negative = i
        if min_val_negative == 0:
            min_val_negative = max(self.negative_elements)

        self.negative_elements.remove(min_val_negative)
        self.negative_elements.append(max_val)

        return max(self.elements[0] * self.elements[1] * self.elements[2], self.negative_elements[0] * self.negative_elements[1] * self.negative_elements[2])

struct = FixedSizeStructure(3)

for i in range(count):
    if len(struct.elements) < 3:
        struct.elements.append(data[i])
        struct.negative_elements.append(data[i])
        continue
    struct.add(data[i])

print(struct.get_result())