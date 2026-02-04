package main

type WordDictionary struct{}

func Constructor() WordDictionary {
	return WordDictionary{}
}

func (wd *WordDictionary) AddWord(word string) {
}

func (wd *WordDictionary) Search(word string) bool {
	return false
}
type TrieNode struct{}
