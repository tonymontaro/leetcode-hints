package convert_sorted_array_to_binary_search_tree

import "github.com/openset/leetcode/internal/kit"

type TreeNode = kit.TreeNode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
	var node *TreeNode
	if l := len(nums); l > 0 {
		node = &TreeNode{Val: nums[l/2]}
		node.Left = sortedArrayToBST(nums[0 : l/2])
		node.Right = sortedArrayToBST(nums[l/2+1:])
	}
	return node
}
