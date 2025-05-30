# filename: codebase/leader_pairs.py
import sys


def read_input():
    """
    Reads input from stdin if available, otherwise uses the provided sample input.
    Returns:
        N (int): Number of cows
        breeds (str): String of breeds
        E (list of int): List of E_i values
    """
    import sys
    lines = []
    for line in sys.stdin:
        if line.strip() == "":
            continue
        lines.append(line.strip())
    if len(lines) >= 3:
        N = int(lines[0])
        breeds = lines[1]
        E = list(map(int, lines[2].split()))
    else:
        # Fallback to provided sample input
        N = 3
        breeds = "GGH"
        E = [2, 3, 3]
    return N, breeds, E


def main():
    N, breeds, E = read_input()
    
    # Precompute breed indices
    G_indices = []
    H_indices = []
    for i in range(N):
        if breeds[i] == 'G':
            G_indices.append(i)
        else:
            H_indices.append(i)
    
    # Get min/max for each breed
    min_G = G_indices[0]
    max_G = G_indices[-1]
    min_H = H_indices[0]
    max_H = H_indices[-1]
    
    # Find all possible leader candidates for each breed
    G_leaders = G_indices
    H_leaders = H_indices
    
    # For each possible pair (g_leader, h_leader), check if both satisfy the leader condition
    count = 0
    for g in G_leaders:
        for h in H_leaders:
            # For G leader g:
            g_list_start = g
            g_list_end = E[g] - 1  # 0-based
            g_ok = False
            if g_list_start <= min_G and g_list_end >= max_G:
                g_ok = True
            elif g_list_start <= h and g_list_end >= h:
                g_ok = True
            # For H leader h:
            h_list_start = h
            h_list_end = E[h] - 1
            h_ok = False
            if h_list_start <= min_H and h_list_end >= max_H:
                h_ok = True
            elif h_list_start <= g and h_list_end >= g:
                h_ok = True
            if g_ok and h_ok:
                count += 1
    print(count)


if __name__ == "__main__":
    main()