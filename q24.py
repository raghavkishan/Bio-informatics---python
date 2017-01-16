class edge:
    def __init__(self, parent, child, seq):
        self.parent = parent
        self.child = child
        self.seq = seq

nodes = {}
longestseq = ""


def countleaves(node):
    if node not in nodes:
        return 1
    n = 0
    for each in nodes[node]:
        n = n + countleaves(each.child)
        print n
    return n

def parse(node, seq):
    global longestseq
    if node not in nodes: return
    for each in nodes[node]:
        parse(each.child, seq + each.seq)
    numrep = countleaves(node)
    print numrep
    if numrep > k and len(seq) > len(longestseq):
        longestseq = seq
        # debug statement

with open("test1.txt", 'r') as f:
    seq = f.readline().strip()
    k = int(f.readline().strip())
    for line in f:
        p = line.strip().split(" ")
        p[2] = int(p[2])
        p[3] = int(p[3])
        subseq = seq[p[2] - 1: p[2] - 1 + p[3]]
        ed = edge(p[0], p[1], subseq)
        nodes[p[0]] = [ed]

parse("node1", "")
print longestseq
print nodes
