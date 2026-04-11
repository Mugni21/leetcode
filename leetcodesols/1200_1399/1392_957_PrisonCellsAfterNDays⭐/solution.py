class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        m = len(cells)
        #We are going to create a dictionary to save key value pairs {state: day in which we reach such state}
        states = {}
        day = 0
        #Simulate
        while day < n:
            #We create tuples since dictionaries can't save lists
            state = tuple(cells)
            #First we check if we have been on the current state before
            if state in states:
                #The current state (on the first time we saw it before current state) 
                # is where we know the cycle starts
                cycle_start = states[state]
                #Then the cycle lenght is just where we are minus the first time we saw the current state
                cycle_length = day - cycle_start
                #Then, this gives us what we would have left to simulate
                remaining = (n - cycle_start) % cycle_length
                #As the dictionary keys preserve the natural order in which we observed the states, 
                #just taking its keys gives us the sequence with all the info we need
                ordered_states = list(states.keys())
                #Return the state where we sould be at day n !!!
                return list(ordered_states[cycle_start + remaining])


            #If this a new state for us just keep simulating! 
            states[state] = day

            new_cells = [0] * m
            for i in range(1, m - 1):
                if cells[i - 1] == cells[i + 1]:
                    new_cells[i] = 1
                else:
                    new_cells[i] = 0

            cells = new_cells
            day += 1

        return cells
    
#So first tried to bruteforce it, but got timeout error. So the idea is simple. There are only finitely many possible
#states. If n is greater than that amount, by pigeonhole principle we must repeat states. So we need to track the first 
#day that we repeat a state. Then, as the mechanism to switch states is deterministis, we must have a cycle of states.
#Then, now that the cycle repeats forever, we can simplu "jump ahead in time" and extract directly the state where we would be at
#at day n !!!!