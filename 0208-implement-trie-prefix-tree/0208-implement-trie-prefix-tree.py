class TrieNode:
    def __init__(self) -> None:
        # Dictionary mapping characters to child TrieNode instances
        self.children: dict[str, "TrieNode"] = {}
        # Flag indicating whether this node marks the end of a word
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        """
        Initialize the trie data structure.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def _search_prefix(self, prefix: str) -> TrieNode | None:
        """
        Helper method to traverse the trie according to the given prefix.
        Returns the node corresponding to the end of the prefix, or None
        if the prefix does not exist in the trie.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        node = self._search_prefix(word)
        return node.is_end if node is not None else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        return self._search_prefix(prefix) is not None
