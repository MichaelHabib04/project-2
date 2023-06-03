# import untitTest
import unittest
from huffmanTree import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_frq("ddddddddddddddddccccccccbbbbaaff")
        rlist = [0, 2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[96:104], rlist)
    def test_coalesce(self):
        l = HTList()
        l.head  = HTListNode(HTree(HTLeaf('d', 1)))
        l.head.next = HTListNode(HTree(HTLeaf('c', 2)))
        l = coalesce_once(l)
        self.assertEqual(l.head.data.listify(), [[('d', 3)], [('d', 1)], [('c', 2)]])
    def test_base_tree_list(self):
        return
    def test_tree_lt(self):
        a = HTListNode(HTree(HTLeaf("a", 777777)))
        b = HTListNode(HTree(HTLeaf("b", 1)))
        self.assertTrue(a>b)
    def test_initial_tree_sort(self):
        l = HTList()
        l.head  = HTListNode(HTree(HTLeaf('c', 2)))
        l.head.next = HTListNode(HTree(HTLeaf('d', 1)))
        l.head.next.next = HTListNode(HTree(HTLeaf('a', 4)))
        l.head.next.next.next = HTListNode(HTree(HTLeaf('b', 3)))
        l.head.next.next.next.next = HTListNode(HTree(HTLeaf(' ', 3)))
        l = initial_tree_sort(l)
        s = HTList()
        s.head  = HTListNode(HTree(HTLeaf('d', 1)))
        s.head.next = HTListNode(HTree(HTLeaf('c', 2)))
        s.head.next.next = HTListNode(HTree(HTLeaf(' ', 3)))
        s.head.next.next.next = HTListNode(HTree(HTLeaf('b', 3)))
        s.head.next.next.next.next = HTListNode(HTree(HTLeaf('a', 4)))
        self.assertEqual(output(s), output(l))
    def test_coalesce_once(self):
        l = HTList()
        l.head  = HTListNode(HTree(HTLeaf('d', 1)))
        l.head.next = HTListNode(HTree(HTLeaf('c', 2)))
        l.head.next.next = HTListNode(HTree(HTLeaf(' ', 3)))
        l.head.next.next.next = HTListNode(HTree(HTLeaf('b', 3)))
        l.head.next.next.next.next = HTListNode(HTree(HTLeaf('a', 4)))
        s = coalesce_once(l)
        self.assertEqual(output(s), [[[('d', 3)], [('d', 1)], [('c', 2)]], [(' ', 3)], [('b', 3)], [('a', 4)]])
    def test_coalesce_all(self):
        l = HTList()
        l.head  = HTListNode(HTree(HTLeaf('d', 1)))
        l.head.next = HTListNode(HTree(HTLeaf('c', 2)))
        l.head.next.next = HTListNode(HTree(HTLeaf(' ', 3)))
        l.head.next.next.next = HTListNode(HTree(HTLeaf('b', 3)))
        l.head.next.next.next.next = HTListNode(HTree(HTLeaf('a', 4)))
        self.assertEqual(output(coalesce_all(l)), [[[(' ', 13)], [[(' ', 6)], [(' ', 3)], [('b', 3)]], [[('d', 7)], [[('d', 3)], [('d', 1)], [('c', 2)]], [('a', 4)]]]])
    def test_build_encoder_array(self):
        l = HTList()
        l.head  = HTListNode(HTree(HTLeaf('d', 1)))
        l.head.next = HTListNode(HTree(HTLeaf('c', 2)))
        l.head.next.next = HTListNode(HTree(HTLeaf(' ', 3)))
        l.head.next.next.next = HTListNode(HTree(HTLeaf('b', 3)))
        l.head.next.next.next.next = HTListNode(HTree(HTLeaf('a', 4)))
        l = coalesce_all(l)
        rcodes = ['00','11', '01', '101', '100']
        build_encoder_array(l.head.data)
        self.assertEqual(rcodes, get_encoder_array())
    def test_encode_string_one(self):
        self.assertEqual(encode_string_one("abcd abc ab a", array = []*256), "11011011000011011010011010011")
    def test_bits_to_chars(self):
        self.assertEqual(bits_to_chars(encode_string_one("abcd abc ab a", array = []*256)), "21913166152")
if __name__ == '__main__':
    unittest.main()
