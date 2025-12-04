# Product of Array Except Self – Notes

## Problem Summary

Given an array `nums`, return an array `result` where `result[i]` is the product of all elements in `nums` except `nums[i]`.

Constraints:
- Do not use division.
- Prefer an O(n) time solution.

---

## Brute Force Approach (My First Working Logic)

Idea:
For each index `i`:
1. Make a copy of the list.
2. Remove the element at index `i`.
3. Multiply all remaining elements.
4. Store the product in the answer list.

Example for `nums = [1, 2, 3, 4]`:

- Excluding index 0 (value 1): `2 * 3 * 4 = 24`
- Excluding index 1 (value 2): `1 * 3 * 4 = 12`
- Excluding index 2 (value 3): `1 * 2 * 4 = 8`
- Excluding index 3 (value 4): `1 * 2 * 3 = 6`

Final output:
`[24, 12, 8, 6]`

Time complexity: O(n²)  
Space complexity: O(n)

What I learned from this approach:
- You cannot safely remove elements from a list while iterating over it.
- Use `list_copy = nums[:]` to copy a list.
- To build a list dynamically, use `append()` instead of assigning by index.

---

## Optimized Approach (Two-Pass Method – O(n))

Key idea:
For each position `i`, the answer can be written as:

`product of all elements to the left of i`  
multiplied by  
`product of all elements to the right of i`.

We do this in two passes:

### 1. Left Pass

We store, for each index `i`, the product of all elements to the left of `i`.

Algorithm:
- Initialize `result` with 1s: `result = [1] * n`
- Maintain `left = 1`
- For `i` from 0 to n-1:
  - Set `result[i] = left`
  - Update `left = left * nums[i]`

After this pass, `result[i]` contains the product of all elements to the left of index `i`.

For `nums = [1, 2, 3, 4]`, after the left pass:

- result = `[1, 1, 2, 6]`

Explanation:
- Index 0: nothing on the left → 1
- Index 1: left is `[1]` → 1
- Index 2: left is `[1, 2]` → 1 * 2 = 2
- Index 3: left is `[1, 2, 3]` → 1 * 2 * 3 = 6

### 2. Right Pass

Now we multiply in the contribution from the right side.

Algorithm:
- Initialize `right = 1`
- For `i` from n-1 down to 0:
  - Multiply: `result[i] = result[i] * right`
  - Update: `right = right * nums[i]`

Here, `right` keeps the product of all elements to the right of `i`.

For `nums = [1, 2, 3, 4]` and `result = [1, 1, 2, 6]` from the left pass:

- Start: `right = 1`
- i = 3: result[3] = 6 * 1 = 6;   right = 1 * 4 = 4
- i = 2: result[2] = 2 * 4 = 8;   right = 4 * 3 = 12
- i = 1: result[1] = 1 * 12 = 12; right = 12 * 2 = 24
- i = 0: result[0] = 1 * 24 = 24; right = 24 * 1 = 24

Final result:
`[24, 12, 8, 6]`

Time complexity: O(n)  
Extra space (excluding output): O(1)

---

