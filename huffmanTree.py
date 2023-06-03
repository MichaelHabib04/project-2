codes = [None] * 256
def get_encoder_array():
    res = [i for i in codes if i is not None]
    return res
class HTLeaf:
    def __init__(self, char: str, count: int):
        self.char = char
        self.count = count
        self.odata = (char, count)
    def __lt__(self, other):
        if other == None:
            return True
        check = True
        if self.count < other.count:
            check = True
        elif self.count > other.count:
            check = False
        else:
            if ord(self.char) < ord(other.char):
                check = True
            else:
                check = False
        return check
class HTree:
    def __init__(self, node: HTLeaf, left = None, right = None, code = ""):
        self.node = node
        self.data = (node.char, node.count)
        self.left = left
        self.right = right
        self.code = code
    def sum(self)-> int:
        if self == None:
            return 0
        elif self.left and not self.right:
            return self.left.sum() + self.node.count
        elif self.right and not self.left:
            return self.right.sum() + self.node.count
        elif self.left and self.right:
            return self.left.sum() + self.right.sum() + self.node.count
        else:
            return self.data
    def tree_frq(self):
        x = self.node.count
        if self == None:
            return 0
        elif self.left and not self.right:
            return self.left.tree_frq() + self.node.count
        elif self.right and not self.left:
            return self.right.tree_frq() + self.node.count
        elif self.left and self.right:
            return self.left.tree_frq() + self.right.tree_frq() + self.node.count
        else:
            return self.node.count
    def listify(self)-> list:
        rlist = []
        if self == None:
            pass
        elif self.left and not self.right:
            rlist.append([self.data])
            rlist.append((self.left).listify())
            return rlist
        elif self.right and not self.left:
            rlist.append([self.data])
            rlist.append((self.right).listify())
            return rlist
        elif self.left and self.right:
            rlist.append([self.data])
            rlist.append((self.left).listify())
            rlist.append((self.right).listify())
            return rlist
        else:
            return [self.data]
class HTListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __lt__(self, other):
        if other == None:
            return True
        check = True
        if self.data.node.count < other.data.node.count:
            check = True
        elif self.data.node.count > other.data.node.count:
            check = False
        else:
            if ord(self.data.node.char) < ord(other.data.node.char):
                check = True
            else:
                check = False
        return check
class HTList():
    def __init__(self):
        self.head = HTListNode(None)
    def size(self) -> int:
        len = 0
        current = self.head
        while current != None:
            len = len + 1
            current = current.next
        return len
def cnt_frq(string: str):
    frq = 256*[0]
    for i in range(len(string)):
        idx = ord(string[i])
        frq[idx]+=1
    return frq
def coalesce_once(lst: HTList):
    x = lst.head.next.next
    fr = lst.head.data
    ls = lst.head.next.data
    newLeaf = HTLeaf(None, int(fr.node.count + ls.node.count))
    if fr.node.count > ls.node.count:
        newLeaf.char = ls.node.char
        newTree = HTree(newLeaf, ls, fr)
    elif fr.node.count < ls.node.count:
        newLeaf.char = fr.node.char
        newTree = HTree(newLeaf, fr, ls)
    else:
        if ord(fr.node.char) < ord(ls.node.char):
            newLeaf.char = fr.node.char
            newTree = HTree(newLeaf, fr, ls)
        else:
            newLeaf.char = ls.node.char
            newTree = HTree(newLeaf, ls, fr)
    newLeaf.count = ls.node.count + fr.node.count
    y = HTListNode(newTree)
    y.next = x
    lst.head = y
    return lst
def coalesce_all(lst: HTList):
    while lst.size() > 1:
        lst = initial_tree_sort(lst)
        lst = coalesce_once(lst) 
    return lst
def build_encoder_array(tree: HTree):
    if tree.left == None and tree.right == None:
        codes[ord(tree.node.char)] = tree.code
    if tree.left:
        tree.left.code = tree.code + "0"
        build_encoder_array(tree.left)
    if tree.right:
        tree.right.code = tree.code + "1"
        build_encoder_array(tree.right)
def output(l: HTList):
    current = l.head
    o = []
    while current.next:
        o.append(current.data.listify())
        current = current.next
    o.append(current.data.listify())
    return o
def initial_tree_sort(lst: HTList):
    l1 = []
    l2 = []
    rl = HTList()
    rlcur = rl.head
    current = lst.head
    for i in range(lst.size()):
        l1.append(current.data)
        l2.append(current.data.node)
        current = current.next
    for i in range(len(l2)):
        minI = i
        for x in range(i,len(l2)):
            if l2[x] < l2[minI]:
                minI = x
        t = l2[minI]
        l2[minI] = l2[i]
        l2[i] = t
        t = l1[minI]
        l1[minI] = l1[i]
        l1[i] = t
    rl.head = HTListNode(l1[0])
    rlcur = rl.head
    for i in range(1, len(l2)):
        rlcur.next = HTListNode(l1[i])
        rlcur = rlcur.next
    return rl
def encode_string_one(string: str, array = []*256):
    rl = []
    ol = HTList()
    array = cnt_frq(string)
    for i in range(256):
        if array[i]:
            rl.append(HTree(HTLeaf(chr(i), array[i])))
    ol.head = HTListNode(rl[0])
    current = ol.head
    for i in range(1,len(rl)):
        current.next = HTListNode(rl[i])
        current = current.next
    ol = coalesce_all(ol)
    build_encoder_array(ol.head.data)
    ar = codes
    clear = ""
    for i in range(len(ar)):
        if ar[i] != None:
            clear += ar[i]
    op = ""
    for i in string:
        op  = op + codes[ord(i)]
    return op
def bits_to_chars(string: str):
    bits = string
    chars = ""
    for i in range((8-(len(string)%8))):
        bits += "0"
    itr = int(len(bits)/8)
    for i in range(itr):
        b2 = str(bits[i*8: i*8 + 8])
        chars += str(int(b2, 2))
    return chars
def huffman_code_file(file_in: str, file_out: str):
    try:
        input_file = open(file_in, "r")
    except:
        raise FileNotFoundError
    input_text = input_file.readlines()
    output_file = open(file_out, "w")
    for str in input_text:
        output_file.write(encode_string_one(str))
        output_file.write(bits_to_chars(encode_string_one(str)))
    input_file.close()
    output_file.close()
