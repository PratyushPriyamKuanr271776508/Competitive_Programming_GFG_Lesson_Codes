def find_subarr(arr):
    n = len(arr)
    
    # --- PREFIX SUM GENERATION ---
    # ps[i] will store the sum of the first 'i' elements of the array.
    # Base case: The sum of 0 elements is 0.
    ps = [0]
    for i in range(n):
        # We use arr[i] because Python is 0-indexed.
        # ps[-1] always grabs the most recent running total.
        ps.append(ps[-1] + arr[i])
        
    # --- BUCKET TRACKING (PIGEONHOLES) ---
    # idx array acts as our 'pigeonholes' or buckets for remainders 0 to n-1.
    # We initialize with -1 to signify that a remainder hasn't been seen yet.
    idx = [-1] * n 
    
    # --- ITERATING THROUGH REMAINDERS ---
    # We iterate through the prefix sums from index 1 to n.
    for i in range(1, n + 1):
        # SCENARIO A: Direct Divisibility
        # If a prefix sum itself is perfectly divisible by n, 
        # the valid subarray starts from the very beginning (index 0) up to i-1.
        if ps[i] % n == 0: 
            return (0, i - 1)
            
        # SCENARIO B: Same Remainder Conflict (Pigeonhole Principle)
        x = ps[i] % n  # Calculate the remainder (our pigeonhole index)
        
        # BUG FIX: Check 'idx[x]' to see if we have visited this remainder before.
        if idx[x] == -1: 
            # If it is the first time seeing this remainder, 
            # record the current index so we can subtract it later if a match appears.
            idx[x] = i 
        else: 
            # If the remainder was seen before, a conflict is found!
            # The elements between the previous index and current index sum up to a multiple of n.
            # We return the starting index (idx[x]) and ending index (i-1) of the subarray.
            return (idx[x], i - 1)
            
    return None

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================
#
# TIME COMPLEXITY: O(n)
# --------------------
# 1. Prefix Sum Loop: Runs exactly 'n' times to build the 'ps' array. 
#    Each append and addition operation inside takes O(1) constant time. 
#    Total for this step = O(n).
#
# 2. Main Processing Loop: Runs a maximum of 'n' times. 
#    Inside the loop, calculating modulo (ps[i] % n), lookup (idx[x] == -1), 
#    and assignment (idx[x] = i) are all basic arithmetic/array operations 
#    that execute in O(1) constant time.
#
# Since these two loops execute sequentially, the total Time Complexity is 
# O(n) + O(n) = O(2n), which simplifies asymptotically to O(n).
#
#
# SPACE COMPLEXITY: O(n)
# ---------------------
# 1. Prefix Sum Array ('ps'): Stores 'n + 1' integers to keep track of 
#    cumulative sums. This scales linearly with the input size, consuming O(n) space.
#
# 2. Index Tracker Array ('idx'): Stores 'n' integers (initialized to -1) 
#    to track the remainder history. This also consumes O(n) space.
#
# Combining these two structural overheads results in O(n) + O(n) = O(2n) auxiliary 
# space, which simplifies asymptotically to a total Space Complexity of O(n).
# ==============================================================================
