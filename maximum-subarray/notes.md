## Optimized Approach — Kadane’s Algorithm (O(n))
Kadane’s algorithm uses the idea of a **running sum** that resets whenever it becomes negative.

### Key Intuition
- A **negative running sum** cannot help future subarrays → reset to `0`.
- A **positive running sum** can contribute to a larger sum.
- Track the maximum sum seen so far.

### Steps
1. Maintain two variables:
   - `current_sum`: sum of the current subarray
   - `max_sum`: best sum found so far
2. Traverse through `nums`:
   - Add current number to `current_sum`
   - Update `max_sum` with the maximum of `max_sum` and `current_sum`
   - If `current_sum` becomes negative, reset it to `0`

### Why resetting works
A negative prefix reduces the sum of any future subarray.  
So, restarting gives a better chance of forming a higher sum.

---