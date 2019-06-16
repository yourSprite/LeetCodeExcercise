class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}  # 前缀树使用字典表示，字典的值仍是字典
        self.end_of_word = '#'  # 结束标志符

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # 1.如果当前节点没有后续节点则生成一个空字典并返回，有的话直接返回
            # 2.当前节点后续节点传递给node
            node = node.setdefault(char, {})
            # print(self.root)
        node[self.end_of_word] = self.end_of_word  # 最后写入结束标志

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            # 没有当前节点直接返回False
            if char not in node:
                return False
            # 当前节点后续节点传递给node
            node = node[char]
        # 判断是否有结束标志
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('word')
param_3 = obj.startsWith('prefix')

print(param_2)
print(param_3)
