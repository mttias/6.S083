# purpose: recreate the set type with our own class

class Int_set(object):
    def __init__(self):
        # creates an empty list on intialisation
        # the '_' implies this is a private variable (used only in this class!)
        self._vals = []
    # 'self' refers to the object being operated upon.
    # 'self' is used by convention
    def insert(self, e):
        if e not in self._vals:
            self._vals.append(e)
    def member (self, e):
        return e in self._vals
    def remove(self, e):
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def get_members(self):
        return self._vals[:]
    def union(self, other):
        """
            other is an Int_set
            mutates self so it contains exactly the elements 
            in self and in other.
        """
        for x in other.get_members():
            self.insert(x)

    def __str__(self):
        if self._vals == []:
            return '{}'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'

s = Int_set()
u = Int_set()

for x in range(1, 25, 2):
    s.insert(x)

for x in range(2, 25, 2):
    u.insert(x)

# s is the instance
# insert(), get_members() and so on is the method
print(str(s))
print(str(u))

s.union(u)
print(s)