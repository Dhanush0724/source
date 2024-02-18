class Multiset(object):
    def __init__(self):
        self.elements = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.elements.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.elements:
            self.elements.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elements

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.elements)

# Example usage:
if __name__ == "__main__":
    multiset = Multiset()
    q = int(input())
    for _ in range(q):
        operation = input().split()
        if operation[0] == 'add':
            multiset.add(int(operation[1]))
        elif operation[0] == 'remove':
            multiset.remove(int(operation[1]))
        elif operation[0] == 'contains':
            print(int(operation[1]) in multiset)
        elif operation[0] == 'len':
            print(len(multiset))