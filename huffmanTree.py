class HLeaf:
    def __init__(self) -> None:
        pass
class HTLeaf:
    def __init__(self, char: str, count: int):
        self.char = char
        self.count = count
class HTree:
    def __init__(self, node: HTLeaf, left = None, right = None):
        self.node = node
        self.data = (node.char, node.count)
        self.left = left
        self.right = right
    def sum(self)-> int:
        if self == None:
            return 0
        elif self.left and not self.right:
            return self.left.sum() + self.node.count
        elif self.right and not self.left:
            return self.right.sum() + self.node.count
        elif self.left and self.right:
            return self.left.sum() + self.right.sum() + self.node.count #data
        else:
            return self.data
    def tree_frq(self):
        x = self.node.count
        if self == None:
            return 0
        elif self.left and not self.right:
            return self.left.node.tree_frq() + self.node.count
        elif self.right and not self.left:
            return self.right.node.tree_frq() + self.node.count
        elif self.left and self.right:
            return self.left.tree_frq() + self.right.tree_frq() + self.node.count
        else:
            return self.node.count - x 
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
def tree_lt(first: HTree, second: HTree):
    return (first.sum() <= second.sum())
def base_tree_list(frq: list):
    BTL = HTList()
    BTL.head = HTListNode(HTLeaf(chr(0), frq(0)))
    current = BTL.head
    for i in range(frq[1:]):
        current.next = HTLeaf(chr(i), frq(i))
        current = current.next
    return BTL
def tree_list_insert(lst: HTList, new: HTree):
    current = lst.head
    currenter = current.next
    while current.next:
    # for i in range(lst.size()):
        if not current.next.next:
            if current.data.tree_frq() >= new.tree_frq():                
                current.next = HTListNode(new)
            else:
                temp = current
                current.data  = HTListNode(new)
                current.next = temp
            return lst
        if new.tree_frq() > current.next.data.tree_frq():
            temp = HTListNode(new)
            current.next = temp
            temp.next = currenter
            currenter = temp
        return lst
def initial_tree_sort(uList: HTList):
    sList = HTList()
    sList.head = uList.head
    current = uList.next
    while current:
        tree_list_insert(sList, current)
    return sList
def coalesce_once(lst: HTList):
    x = lst.head.next.next
    fr = lst.head.data
    # print(type(lst.head))
    # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", type(lst.head.next))
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
    # if lst.head.next.next:
    # x = lst.head.next.next
    #     lst.head = HTListNode(newTree)
    #     lst.head.next = x
    # else:
    lst.head = HTListNode(newTree)
    lst.head.next = x
    return lst
def coalesce_all(lst: HTList):
    while lst.size() > 1:
        coalesce_once(lst)
    return lst
def get_leaves(root: HTree):
    leaves = []
    if not root.left and not root.right:
        return [root.data]
    if not root.left:
        leaves = get_leaves(root.right)
    if not root.right:
        leaves = get_leaves(root.left)
    if root.left and root.right:
        leaves = get_leaves(root.left) + get_leaves(root.right)
    return leaves
def get_paths(root: HTree):
    paths = []
    if not root.left and not root.right:
        print("111111111111111111")
        return paths
    if not root.left:
        print("222222222222222222")
        paths = get_paths(root.right).append(1)
    if not root.right:
        print("3333333333333333333")
        paths = get_paths(root.left).append(0)
    if root.left and root.right:
        print("444444444444444444")
        paths = get_paths(root.left) + (get_paths(root.right))
    print(paths)
    return paths
def build_encoder_array(slf: HTree):
    rl = 256*[0]
    leaves = get_leaves(slf)
    paths = get_paths(slf)
    for i in range(len(leaves)):
        a = ord(leaves[i][0])
        rl[a] = paths[i]
    return rl

aa = HTree(HTLeaf('s', 1))
aa.left = HTree(HTLeaf('a', 1))
aa.right = HTree(HTLeaf('t', 1))
l = HTList()
a = HTListNode(aa)
l.head  = a
b = HTListNode(HTree(HTLeaf('f', 1)))
a.next = b
c = HTListNode(HTree(HTLeaf('g', 1)))
c.data.left = HTree(HTLeaf('x', 1))
c.data.right = HTree(HTLeaf('v', 1))
b.next = c
print(a.data.listify())
print(l.head.next.data.listify())
coalesce_all(l)
print(l.head.data.listify())
print(l.head.data.tree_frq())