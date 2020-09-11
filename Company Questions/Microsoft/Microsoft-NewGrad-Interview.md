Microsoft interview
Table of Contents
General process
On the day of the interview, you will accept 4 to 5 rounds of interviews (the internship is 3 rounds, the first two rounds are parallel, just after one round), the interviewers are usually from two teams of different managers, the company will arrange the interview in the meeting room .
The general process of each round of interview is:

Self-introduction in English -> Algorithmic 2+ Road -> Experience, Character -> English answer "Why do you want to join Microsoft for an internship"
"Why do you want to join Microsoft?" To
ask this question, Microsoft wants to know whether you are passionate about technology. A better answer is: "I have been using Microsoft software since I came into contact with computers. Your company's products are amazing. For example, I have been VS Codelearning to program and its plug-ins are so easy to use."

Algorithm question
It's not difficult, communication is very important, interaction (inplace or not, is there a negative number in the tree)! ! ! Pay attention to code quality (programming style, naming conventions, outlier handling) . Various follow up and require you to design as many test cases as possible .

mathematics
Frequent questions
✔️Rotate image ++++
inplace? Phalanx?
Idea: reverse up and down and then reverse diagonally.
✔️Coloring problem +++
Given an adjacency matrix, 0 means not adjacent, 1 means adjacent, and given k colors, find out how each item should be painted.
Ideas:
Complexity o(n^3)
Write a function to judge whether a certain point and the connected point have the same color, that is, judge matrix[x][y] == 1 and color[x] == color[y], traverse y, find the difference, and return 1.
Write a main function to traverse each time to assign a color to a point, and keep changing if it is different.
✔️Find the array and be the target+++
Find the index of the two numbers in an array and the target ++
Store the value of target-current number in the dictionary, where value is the current index.
When the following value is in the dictionary, the sum of this number and a previous number is the target, and the previous index is taken out
follow up: find out a triplet whose sum is target in an array
follow up: find a combination of targets in an array
Find the absolute minimum value of the sum of any two numbers in an array
Can be sorted? can
Use pointers, pay attention to pointer movement conditions
✔️Longest continuous subsequence
For a sequence that only contains 0 and 1, find the longest continuous sub-column that guarantees the same number of 0 and 1. http://www.voidcn.com/article/p-pshuooqw-mn.html
Change 0 to -1, the problem is equivalent to the longest continuous subsequence that sums to 0, dynamic programming, pay attention to find the last even number of 0
What if the substring does not start from scratch? For example, 1101100, the dynamic programming method needs to be adjusted at this time.
Map each sub-column sum to find the difference between the largest index of the same value.
Such as 1101100

Blind date
amicable number, in two positive integers, the sum of all positive divisors of each other is equal to the other
The divisor is also called the factor, b is the divisor of a, then a%b==0, there is no remainder when dividing evenly
All factors of 220 (factors other than themselves): 1+2+4+5+10+11+20+22+44+55+110 = 284
All factors of 284: 1+2+4+71+142 = 220
Full array
Find the index of this permutation in the full array. https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
One line is an array of length N, each element is 0 or 1 or 2, find the number of (i, j, k) satisfying a[i]<a[j]<a[k]
Simple question:
Find prime numbers from 1 to 1000000
Add two large numbers
Multiply large integers, see Sword Finger offer for details
Find the maximum number of all numbers in the array
To determine whether three numbers can form a triangle, it is required to implement isTriangle(int a, int b, int c)
Can only judge whether the subtraction is less than, not the sum of the two sides is greater than the third side, it will overflow
Explain . Explanation two
Given a function rand100(), it can randomly return an integer from 1 to 100, and this function is required to implement rand10000()
follow up: use rand100() to implement rand500()
follow up 2: Use rand100() to implement rand150()
Conclusion: If x and y can be generated within a certain time using rand100, then given a number, ask if rand100 can be used to generate within a certain time
The k-th largest number in the array
String processing
Letter and number mapping problem: Given a letter and number mapping relationship, such as 1-26 corresponding to az, and then input a numeric string such as "123", please output all possible letter string, "abc" And "aw" and "lc".
atoi function , string to integer
To remove the space, strip()
Whether the string is empty, if empty, return 0
Exceed 2^31-1 or -2^31, all are truncated into 2^31-1 or -2^31
The first character is positive or negative, get and save the symbol
Get the number substring, until a non-digit character is found, exit the loop
https://leetcode.com/problems/word-break/description/
https://leetcode.com/problems/integer-to-english-words/
There is a text containing only letters and spaces, and all the words in it are output. STL cannot be used.
Give a string, which is a normal English sentence. It is required to reverse the order of appearance of all the words in it, but the words themselves are not in reverse order, such as "This is a test" -> "test a is This"
Note that there are consecutive spaces at the beginning and end and in the middle
Given a string with uppercase and lowercase letters, move all uppercase letters to the back of lowercase letters and keep the order unchanged.
A string of characters can be turned into a palindrome by deleting at least a few characters.
Given two strings S1 and S2, if f(S1.substring)=S2.substring, and f: change one character in the string. Please find out all S1.substring edit distance?
Longest palindrome substring
Enter a char[] str, and it is required to replace all "ab" in str with "c" and all single "b" with "ef". Require in-place, and ensure that the number of "ab" in str> the number of "b" (that is, the length of str is sufficient to put the result of replacement)
Binary search
+++The sword refers to the ordered array of n*m (each row/column) of the original question of the offer.
Given an array, the elements in it decrease first and then increase, and it is required to find the subscript of the smallest element
++ https://leetcode.com/problems/search-in-rotated-sorted-array/
partition algorithm! !
Given a disorderly linked list, given a number, put the nodes larger than this number in the back and nodes smaller than this number in the front, requiring stability, that is, maintaining the relative position between the original numbers.
Find the median in the array
+++ top k (I said heap row, the interviewer was going to ask me about the implementation of heap, I said that it would not do it...too bad, the interviewer did not ask me)
Find the median of the merged two ordered arrays under the requirement of time complexity O(log(m+n));
Linked list:
merge sorted array (easy)
Fill from the end of the longer array, and fill the larger of the two arrays to the end to avoid moving array elements.
And collect
+++ https://leetcode.com/problems/friend-circles/

https://leetcode.com/problems/accounts-merge/

https://leetcode.com/problems/number-of-islands/ ++

There are many tags in the system, and there is a parent-child relationship between tags. For example, the two tags "iOS" and "Android" are children of the "programming" tag. An article will contain multiple tags. Given a tag, output a list of articles containing this tag and its subtags.

Enter tag_record, each of which is a two-tuple of (parent tag, child tag)

Enter tag_article, each of which is a two-tuple of (article tag, article id)

Enter tag, which is the tag to find

Output a list of matching article names

Solution: Use a dictionary and a tree. Use a dictionary to find nodes in the tree based on tags. A node in the book corresponds to a tag. The node stores the tag value and the attribute of children. Children stores the ids of all direct child tags. After traversing tag_record, the tree structure with parent-child relationship is maintained, and then the input tag and its child tags can be easily found, and then compared with the record in tag_article to find it.

Find bloggers with more than N followers (direct or indirect follow).

maxStack
min Stack
Implement a stack with getmax() function
Take the largest value for each pop traversal
Space for time, stack two elements (x, curMax) at the same time, compare with the top of the stack and update curMax when pushing, pay attention to check stack length for other operations
tree
++++ dictionary prefix tree
Balanced binary tree
balanced binary tree +++
1. Implement a depth to get the depth of the current node recursively. The isBalanced function, recursively checks whether it is balanced. Complexity o(nlogn)
2. Implement a depth to obtain the depth of the current node recursively, and check whether it is balanced, and use the global variable self.isBalanced to mark it. Avoid isBalanced repeating recursion o(logn)
++ Ordered array constructs balanced binary tree
Binary search tree is converted into an ordered doubly linked list
+++ Verify binary search tree
In the binary search tree, find the node closest to the target value and return . If multiple nodes meet the requirements, just return one of them
In-order traversal tree++
Binary search tree implements search node, insert node, delete node Each function asks what kind of test case to use to test, I feel that some interviewers will value this.
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
The maximum path of the tree and +++
++ The longest path of the tree
Print the longest path of the tree
Determine whether an array is a binary search tree
Can subsequent traversals be written non-recursively?
Given an array but not a tree, determine if this array may be the result of a post-order traversal of a binary search tree
LCA, only two target nodes, no root
dfs
Largest sub-matrix : the largest square. Find the largest square with all 1s in a two-dimensional 01 matrix.
https://leetcode.com/problems/maximal-rectangle/
Dynamic programming
+++Sell stock https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

follow up: Maximum number of transactions++
+++On an n * m chessboard, the starting point is in the upper left corner, and the end point is in the lower right corner. Each position has a different amount. You can only move to the left and the bottom, and you need to find the largest amount and path. minimum-path-sum

https://leetcode.com/problems/path-sum/

https://leetcode.com/problems/path-sum-ii/

https://leetcode.com/problems/path-sum-iii/

greedy
The first question is to know the start and end times of n programs, and ask how many programs can be watched at most. Of course I know this is O(n) greedy
Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
√two pointers
Determine whether the linked list has a ring

Linked List Cycle( https://leetcode.com/problems/linked-list-cycle/ )
Judging whether two linked lists intersect is a variant of finding whether there are rings in the linked list, for example, given two linked lists A and B
A traverses itself until it reaches the end and then starts from B. The same is true for B, after traversing itself, traverse A again.
If there are the same nodes in the middle, then they intersect, otherwise they do not intersect.
Because if they intersect, they will stop at len(A)+len(B)-len(A∩B)
Determine whether the linked list has a ring, and find the entry node

Linked List Cycle( https://leetcode.com/problems/linked-list-cycle-ii/ )
Give a linked list head, return whether it is a singly linked list or a ring linked list, and then add another one to return the length of a linked list head.

How to judge that a linked list has a ring

Big Data:
Median data stream https://leetcode.com/problems/find-median-from-data-stream/
Billions sort summary
Topology
Logic problem
√ Probability questions (use less for more and evenly)
Give a string of numbers containing only 0-9, each number has the same probability (for example, 32978417506), and now tell you (1,3,5,7) these four numbers are not available, that is, only (0, 2,4,6,8,9) How do these 6 numbers represent the original string of numbers?
00 means 0, 02 means 1, 04 means 3, 06 means 5, 08 means 7
15 bits represent the previous 10 bits, so the storage is 0.5 times more
√ Convex hull problem
Find the convex polygon that wraps all points
Exhaustive method O(n³)
Idea: Two points determine a straight line. If the remaining points are on one side of the straight line, then these two points are points on the convex hull, otherwise they are not.
Steps: 1. Pair all points in the point set in pairs to form n(n-1)/2 straight lines. 2. For each straight line, check whether the remaining n-2 points are on the same side of the straight line.
If the result is positive, ($$x_3, y_3$$) is on the left side of the line, and negative on the right side
Three-point distance formula

Divide and conquer O(nlogn)
Idea: Find the convex hull point, divide the point set, and continue to find the convex hull point on the sub-point set
step:
Find P1 and P2 with the largest abscissa must be convex hull points, divided into upper and lower envelopes
For the upper package, find the point farthest from the straight line (the formula is as above) , that is, Pmax in the figure
Pack the left side of P1Pmax and the right side of PnPmax
Repeat the second and third steps, the same for the next package


Step method O(nH)
H is the number of closure points.

Ideas:

First find the point with the smallest ordinate and add it to the closure
Starting from P0, find the point that minimizes the alpha angle (the angle between the x-axis) on the point set counterclockwise, that is, P1
Starting from P1, find the point that minimizes the alpha angle (the angle between P0P1 and P1P?) on the point set counterclockwise, namely P2
Repeat until back to P0. Note that the collinear time points are all added to the closure, but the farthest point is selected as the starting point for the next time.


Graham scanning method O(nlogn)


Soft skills (behavioral interview)
The interviewer wants to know which of your abilities has improved the most in this project.
