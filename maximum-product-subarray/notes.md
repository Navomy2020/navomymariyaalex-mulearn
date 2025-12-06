# Notes — Maximum Product Subarray (Day 4)

## Problem Summary
Given an integer array `nums`, return the maximum product of any contiguous subarray.

Examples:
- Input: [2, 3, -2, 4] → Output: 6
- Input: [-2, 0, -1] → Output: 0

The product must be formed from a continuous subarray.

---

## Why This Problem Is Hard
In the Maximum Sum Subarray problem, we reset the running sum when it becomes negative. This works because a negative prefix always makes future sums worse.

However, in the Maximum Product Subarray:

- A negative product is not always bad.
- Multiplying another negative number later can turn it into a large positive product.
- Therefore, we cannot simply drop negative products.

Example:
`[-2, 3, -4]`

The subarray `[-2, 3]` gives product `-6`, which is negative.
But multiplying with the next negative number `-4` gives `24`, which is the maximum.

To capture this behavior, we must track both the maximum and minimum products at every index.

---

## Key Idea: Track max_prod and min_prod

At each index, three possibilities exist:
1. Start a new subarray with the current number.
2. Extend the previous max product.
3. Extend the previous min product (important when the current number is negative).

Thus, for each number `x`:
