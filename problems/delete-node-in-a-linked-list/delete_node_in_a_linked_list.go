package delete_node_in_a_linked_list

import . "github.com/openset/leetcode/internal/kit"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteNode(node *ListNode) {
	if node != nil && node.Next != nil {
		node.Val = node.Next.Val
		node.Next = node.Next.Next
	}
}
