'''
Program: TowersOfHanoiParsons.py
Author: Bobby Parsons

Description: Uses recursion to figure out how many moves are needed to solve 
the Towers of Hanoi problem.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or 
unmodified. I have not given other fellow student(s) access to
my program.   
'''

'''
Recursion in programming is when a function calls itself in order to solve a
problem. It will repeat until it meets an exit condition, at which point it
will return the value it was calculating or the solution to the problem it
wanted to solve. It's most useful for when the solution to a problem involves
the solution to a smaller version of the same problem, making recursion perfect
for problems like the Towers of Hanoi.

In this program. recursion is used to calculate the number of moves that are
needed to solve a Towers of Hanoi problem. To do this, I first tried the puzzle
out myself and found that each solution builds on one another. With that in
mind, I figured that since each solution contains the solutions of all smaller
versions of the problem, all each iteration of the program had to do is find
the number of "new moves" and then find the "new moves" for every iteration
of the problem below it. 
'''


def solve_towers(disks, steps=0):
    '''Calculates the number of moves needed to solve the Towers of Hanoi.

    :param disks: Number of disks in the tower
    :param steps: Number of moves it has made so far (DO NOT MANUALLY SET)
    '''
    _steps = steps
    if disks > 0:
        # Calculate the number of new moves (see bottom)
        _steps = _steps + 2 ** (disks - 1)

        # Decrement disks by 1
        _steps = solve_towers(disks - 1, _steps)
    return _steps


if __name__ == "__main__":
    disks = int(input('Please enter the number of disks: '))

    moves = solve_towers(disks)

    print(str(disks) + ' disks requires ' + str(moves) + ' moves.')

    input('Press any key')

'''
1: 1
Move 1 to C
1 new move

2: 3
Move 1 to B
----
Move 2 to C
Move 1 to C
2 new moves

3: 7
Move 1 to C
Move 2 to B
Move 1 to B
----
Move 3 to C
Move 1 to A
Move 2 to C
Move 1 to C
4 new moves

4: 15
Move 1 to B
Move 2 to C
Move 1 to C
Move 3 to B
Move 1 to A
Move 2 to B
Move 1 to B
----
Move 4 to C
Move 1 to C
Move 2 to A
Move 1 to A
Move 3 to C
Move 1 to B
Move 2 to C
Move 1 to C
8 new moves

5: 31
16 new moves

B and C switch in the old moves of each solution

New moves = 2^(n-1)
moves + 2^(n-1) each iteration
'''
