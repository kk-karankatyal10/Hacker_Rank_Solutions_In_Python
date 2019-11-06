def minimumBribes(q):
    bribes = 0
    for final_pos, start_pos in enumerate(q):
        # Abort if anyone is more than two bribes ahead of where they started
        if  final_pos + 1 < start_pos - 2:
            print('Too chaotic')
            return
        # Count the number of people who started behind me, who are ahead of my
        # final position. Conduct the search between two spots forward of where
        # I started, thru to the person in front of me in the end; as these are
        # the only people to have potentially bribed me.
        potential_bribers = range(max(start_pos - 2, 0), final_pos)
        bribes += [q[briber] > start_pos for briber in potential_bribers].count(True)
    print(bribes)
