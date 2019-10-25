package repeated_string_match

import "strings"

func repeatedStringMatch(A string, B string) int {
	a, count := A, len(B)/len(A)
	if len(B)%len(A) > 0 {
		count++
	}
	for times := 0; times < 2; times++ {
		a = strings.Repeat(A, count)
		if strings.Index(a, B) != -1 {
			return count
		}
		count++
	}
	return -1
}
