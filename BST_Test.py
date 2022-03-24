import unittest
from Binary_Search_Tree import Binary_Search_Tree

class DSQTester(unittest.TestCase):

    def setUp(self):
        self.__tree= Binary_Search_Tree()
#when the tree is empty
    def test_empty_height(self):
        self.assertEqual(0, self.__tree.get_height())
    def test_empty_inorder(self):
        self.assertEqual('[ ]', str(self.__tree))
    def test_empty_preorder(self):
        self.assertEqual('[ ]', self.__tree.pre_order())
    def test_empty_preorder(self):
        self.assertEqual('[ ]', self.__tree.post_order())
#when the tree only has a root node
    def test_one_node_height(self):
        self.__tree.insert_element(1)
        self.assertEqual(1, self.__tree.get_height())
    def test_one_inorder(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__tree))
    def test_one_preorder(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', self.__tree.pre_order())
    def test_one_postorder(self):
        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', self.__tree.post_order())
#inserting root node, then removing root node
    def test_one_node_removal_inorder(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual('[ ]', self.__tree.in_order())
    def test_one_node_removal_height(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual(0, self.__tree.get_height())
#tree has two nodes
    def test_two_nodes_height(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual(2, self.__tree.get_height())
    def test_two_nodes_inorder(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.__tree.in_order())
    def test_two_nodes_pre_order(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.__tree.pre_order())
    def test_two_nodes_postorder(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 2, 1 ]', self.__tree.post_order())
    def test_two_remove_one_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.assertEqual(1, self.__tree.get_height())
    def test_two_remove_two_height(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual(0, self.__tree.get_height())
    def test_two_remove_two_string(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.remove_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ ]', self.__tree.in_order())
#three nodes in the tree, balanced
    def test_three_inorder(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.assertEqual('[ 2, 5, 7 ]', self.__tree.in_order())
    def test_three_preorder(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 2, 7 ]', self.__tree.pre_order())
    def test_three_postorder(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.assertEqual('[ 2, 7, 5 ]', self.__tree.post_order())
    def test_three_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.assertEqual(2, self.__tree.get_height())
    def test_three_remove_root_inorder(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.__tree.remove_element(5)
        self.assertEqual('[ 2, 7 ]', self.__tree.in_order())
    def test_three_remove_root_preorder(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 2 ]', self.__tree.pre_order())
    def test_three_remove_root_height(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(7)
        self.__tree.remove_element(5)
        self.assertEqual(2, self.__tree.get_height())
    def test_left_left_case(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(6)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 4, 6, 10, 12 ]', self.__tree.in_order())
    def test_right_right_case(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(6)
        self.__tree.insert_element(13)
        self.__tree.insert_element(15)
        self.assertEqual('[ 6, 10, 12, 13, 15 ]', self.__tree.in_order())
    def test_right_left_case(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(25)
        self.__tree.insert_element(31)
        self.__tree.insert_element(50)
        self.__tree.insert_element(45)
        self.assertEqual('[ 25, 30, 31, 45, 50 ]', self.__tree.in_order())
    def test_left_right_case(self):
        self.__tree.insert_element(45)
        self.__tree.insert_element(30)
        self.__tree.insert_element(55)
        self.__tree.insert_element(25)
        self.__tree.insert_element(31)
        self.__tree.insert_element(35)
        self.assertEqual('[ 25, 30, 31, 35, 45, 55 ]', self.__tree.in_order())
    def test_left_right_case_removal(self):
        self.__tree.insert_element(45)
        self.__tree.insert_element(30)
        self.__tree.insert_element(50)
        self.__tree.insert_element(55)
        self.__tree.insert_element(25)
        self.__tree.insert_element(31)
        self.__tree.insert_element(35)
        self.__tree.remove_element(50)
        self.assertEqual('[ 25, 30, 31, 35, 45, 55 ]', self.__tree.in_order())
    def test_left_left_removal(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(50)
        self.__tree.insert_element(12)
        self.__tree.insert_element(60)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.__tree.remove_element(60)
        self.assertEqual([10, 12, 20, 25, 30, 50], self.__tree.to_list())
    def test_right_right_removal(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(26)
        self.__tree.insert_element(2)
        self.__tree.insert_element(17)
        self.__tree.insert_element(28)
        self.__tree.insert_element(1)
        self.__tree.remove_element(20)
        self.assertEqual([1, 2, 15, 17, 26, 28], self.__tree.to_list())
    def test_right_left_removal(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(26)
        self.__tree.insert_element(15)
        self.__tree.insert_element(22)
        self.__tree.remove_element(15)
        self.assertEqual([20, 22, 26], self.__tree.to_list())
    def test_tolist(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(50)
        self.__tree.insert_element(12)
        self.__tree.insert_element(60)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        self.assertEqual([10,12,20,25,30,50,60], self.__tree.to_list())


if __name__ == '__main__':
  unittest.main()
