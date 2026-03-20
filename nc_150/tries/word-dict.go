package tries

type Node struct {
	neighbors [26]*Node
	word      bool
}

type WordDictionary struct {
	head *Node
}

func Constructor() WordDictionary {
	return WordDictionary{head: &Node{}}
}

func (this *WordDictionary) AddWord(word string) {
	curr := this.head
	for idx := range len(word) {
		offset := word[idx] - 'a'

		if curr.neighbors[offset] == nil {
			curr.neighbors[offset] = &Node{}
		}

		curr = curr.neighbors[offset]
	}
	curr.word = true
}

func (this *WordDictionary) Search(word string) bool {
	var check func(node *Node, word string) bool
	check = func(node *Node, word string) bool {
		curr := node
		for idx := range len(word) {
			ch := word[idx]
			if ch == '.' {
				for _, neighbor := range curr.neighbors {
					if neighbor == nil {
						continue
					}
					if check(neighbor, word[idx+1:]) {
						return true
					}
				}
				return false
			}
			offset := ch - 'a'
			if curr.neighbors[offset] == nil {
				return false
			}
			curr = curr.neighbors[offset]
		}
		return curr.word
	}

	return check(this.head, word)
}
