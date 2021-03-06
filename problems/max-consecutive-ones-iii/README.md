<!--|This file generated by command(leetcode description); DO NOT EDIT.    |-->
<!--+----------------------------------------------------------------------+-->
<!--|@author    openset <openset.wang@gmail.com>                           |-->
<!--|@link      https://github.com/openset                                 |-->
<!--|@home      https://github.com/tonymontaro/leetcode-hints                        |-->
<!--+----------------------------------------------------------------------+-->

[< Previous](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/check-if-word-is-valid-after-substitutions "Check If Word Is Valid After Substitutions")
　　　　　　　　　　　　　　　　
[Next >](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/maximize-sum-of-array-after-k-negations "Maximize Sum Of Array After K Negations")

## [1004. Max Consecutive Ones III (Medium)](https://leetcode.com/problems/max-consecutive-ones-iii "最大连续1的个数 III")

<p>Given an array <code>A</code>&nbsp;of 0s and 1s, we may change up to <code>K</code>&nbsp;values from 0 to 1.</p>

<p>Return the length of the longest (contiguous) subarray that contains only 1s.&nbsp;</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,1,1,0,0,0,1,1,1,1,0]</span>, K = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation: </strong>
[1,1,1,0,0,<u><strong>1</strong>,1,1,1,1,<strong>1</strong></u>]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]</span>, K = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">10</span>
<strong>Explanation: </strong>
[0,0,<u>1,1,<b>1</b>,<strong>1</strong>,1,1,1,<strong>1</strong>,1,1</u>,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>0 &lt;= K &lt;= A.length</code></li>
	<li><code>A[i]</code> is <code>0</code> or <code>1</code>&nbsp;</li>
</ol>
</div>
</div>

### Related Topics
  [[Two Pointers](https://github.com/tonymontaro/leetcode-hints/tree/master/tag/two-pointers/README.md)]
  [[Sliding Window](https://github.com/tonymontaro/leetcode-hints/tree/master/tag/sliding-window/README.md)]

### Similar Questions
  1. [Longest Substring with At Most K Distinct Characters](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/longest-substring-with-at-most-k-distinct-characters) (Hard)
  1. [Longest Repeating Character Replacement](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/longest-repeating-character-replacement) (Medium)
  1. [Max Consecutive Ones](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/max-consecutive-ones) (Easy)
  1. [Max Consecutive Ones II](https://github.com/tonymontaro/leetcode-hints/tree/master/problems/max-consecutive-ones-ii) (Medium)
