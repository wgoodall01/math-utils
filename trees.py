#Trees

class Node:
    def __init__(self, name=''):
        self.name = name
        self.children = []

    def __str__(self, level=0):
        output = ('\t' * level) + self.name + '\n'
        for child in self.children:
            output += child.__str__(level + 1)
        return output

    def add_child(self, child):
        self.children.append(child);

    def count_children(self):
        nodes = 0
        if len(self.children) != 0:
            for child in self.children:
                nodes += child.countchildren()
        else:
            nodes += 1
        return nodes

    def __repr__(self): return self.name