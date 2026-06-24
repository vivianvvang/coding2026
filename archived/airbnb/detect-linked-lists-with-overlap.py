def do_lists_overlap(next_map: dict, headA: int, headB: int) -> bool:
    # Edge case: If either list is empty, they cannot share nodes.
    if headA is None or headB is None:
        return False

    def get_tail_and_cycle(head):
        """
        Uses Tortoise and Hare to detect a cycle.
        Returns: (tail_node, cycle_node)
        - If acyclic: returns (actual_tail, None)
        - If cyclic: returns (None, some_node_in_cycle)
        """
        slow = head
        fast = head

        # Advance fast by 2, slow by 1
        while fast is not None and next_map.get(fast) is not None:
            slow = next_map[slow]
            fast = next_map[next_map[fast]]

            # If they meet, a cycle exists
            if slow == fast:
                return None, slow

        # If we break out of the loop, the list is acyclic.
        # Let's traverse normally to find the exact tail node.
        curr = head
        while next_map.get(curr) is not None:
            curr = next_map[curr]
            
        return curr, None

    # Step 1: Analyze both lists for tails and cycles
    tailA, cycleA = get_tail_and_cycle(headA)
    tailB, cycleB = get_tail_and_cycle(headB)

    # Step 2: Handle the three structural cases

    # Case 1: Both lists are acyclic. They overlap if they share the same tail.
    if cycleA is None and cycleB is None:
        return tailA == tailB

    # Case 2: Both lists are cyclic. Check if they share the same cycle.
    if cycleA is not None and cycleB is not None:
        # Traverse List A's cycle starting from cycleA
        curr = next_map[cycleA]
        
        while curr != cycleA:
            if curr == cycleB:
                return True
            curr = next_map[curr]
            
        # Don't forget to check the starting node itself!
        return cycleA == cycleB

    # Case 3: One is cyclic, the other is acyclic. They cannot overlap.
    return False