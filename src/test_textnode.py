import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node but different", TextType.BOLD)
        self.assertNotEqual(node2, node3)

    def test_eq_false2(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node2, node3)

    def test_eq_url(self):
        link_node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        link_node2 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(link_node, link_node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))



if __name__ == "__main__":
    unittest.main()
