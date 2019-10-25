package max_consecutive_ones_iii

func longestOnes(A []int, K int) int {
	left, right := 0, 0
	for right = range A {
		K -= 1 ^ A[right] // 每次遇到 0 就会消耗一次 K
		if K < 0 {        // K 不够用的时候，就从左边回血
			K += 1 ^ A[left]
			left++
		}
	}
	// A[left:right+1] 并不是真的 max-length-sliding-windows
	// 把 right-left+1 当作是 A[:right+1] 中出现过的最长子数组的长度，更合适
	return right - left + 1
}
