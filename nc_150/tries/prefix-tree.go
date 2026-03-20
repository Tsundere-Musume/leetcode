package tries

import "fmt"

type Node struct {
	neighbors [26]*Node
	word bool
}

type PrefixTree struct {
	head *Node 
}

func Constructor() PrefixTree {
	return PrefixTree{head: &Node{}}
}

func (this *PrefixTree) Insert(word string) {
	curr := this.head
	for idx := range len(word) {
		offset := word[idx] - 'a'
		fmt.Println(offset)

		if curr.neighbors[offset] == nil {
			curr.neighbors[offset] = &Node{}
		}

		curr = curr.neighbors[offset]
	}
	curr.word = true
}

func (this *PrefixTree) Search(word string) bool {
	curr := this.head
	for idx := range len(word) {
		offset := word[idx] - 'a'
		if curr.neighbors[offset] == nil {
			return false
		}
		curr = curr.neighbors[offset]
	}

	return curr.word 
}


func (this *PrefixTree) StartsWith(prefix string) bool {
	curr := this.head
	for idx := range len(prefix) {
		offset := prefix[idx] - 'a'
		if curr.neighbors[offset] == nil {
			return false
		}
		curr = curr.neighbors[offset]
	}

	return true
}

