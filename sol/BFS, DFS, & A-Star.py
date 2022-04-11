from game.Node import Node
import datetime

class State:
    def __init__(self, v):
        self.value = v
        self.g_cost = 0
        self.h_cost = 0
        self.parent = 0


# Takes string input, converts to list, swaps chars, returns as string
def swap(input, index1, index2):
    lst = list(input)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return ''.join(lst)

# Takes input as string, returns list of children strings
def getChildren(input):
    list = []
    initPos = input.index('8')

    # [0] swap with [1] or [3]
    if initPos == 0:
        input1 = input
        input1 = swap(input1, initPos, 1)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 3)
        list.append(input2)
    # [1] swap with [0] or [2] or [4]
    elif initPos == 1:
        input1 = input
        input1 = swap(input1, initPos, 0)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 2)
        list.append(input2)

        input3 = input
        input3 = swap(input3, initPos, 4)
        list.append(input3)
    # [2] swap with [1] or [5]
    elif initPos == 2:
        input1 = input
        input1 = swap(input1, initPos, 1)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 5)
        list.append(input2)
    # [3] swap with [0] or [4] or [6]
    elif initPos == 3:
        input1 = input
        input1 = swap(input1, initPos, 0)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 4)
        list.append(input2)

        input3 = input
        input3 = swap(input3, initPos, 6)
        list.append(input3)
    # [4] swap with [1] or [3] or [5] or [7]
    elif initPos == 4:
        input1 = input
        input1 = swap(input1, initPos, 1)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 3)
        list.append(input2)

        input3 = input
        input3 = swap(input3, initPos, 5)
        list.append(input3)

        input4 = input
        input4 = swap(input4, initPos, 7)
        list.append(input4)
    # [5] swap with [2] or [4] or [8]
    elif initPos == 5:
        input1 = input
        input1 = swap(input1, initPos, 2)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 4)
        list.append(input2)

        input3 = input
        input3 = swap(input3, initPos, 8)
        list.append(input3)
    # [6] swap with [3] or [7]
    elif initPos == 6:
        input1 = input
        input1 = swap(input1, initPos, 3)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 7)
        list.append(input2)
    # [7] swap with [6] or [4] or [8]
    elif initPos == 7:
        input1 = input
        input1 = swap(input1, initPos, 6)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 4)
        list.append(input2)

        input3 = input
        input3 = swap(input3, initPos, 8)
        list.append(input3)
    # [8] swap with [7] or [5]
    else:
        input1 = input
        input1 = swap(input1, initPos, 7)
        list.append(input1)

        input2 = input
        input2 = swap(input2, initPos, 5)
        list.append(input2)

    return list

"""
# when you generate a child:
#	1. check child for goal state
#	2. check if child is in list of pre-existing nodes for repeat
#		1. if its a repeat: ignore.
#		2. if not a repeat: add to the queue/stack & list
"""

"""
Queue:
queue = []
queue.append('a')
print(queue.pop(0))
"""
def bfs(puzzle):
    startTime = datetime.datetime.now()
    #  time.sleep(1)
    puzzle = "".join([str(number) for number in puzzle])  # Converts array/list to string
    parentNode = Node(0, puzzle, 0)  # Setting the initial puzzle as a parent node
    goalState = "012345678"
    goalStateFound = False
    list = []  # Solution path list to be returned
    queue = []  # Visited nodes queue
    queue.append(parentNode)  # Adding initial parent node to the queue
    queue.pop(0)  # Popping the initial parent node from the queue
    expandedList = []  # Expanded nodes list
    expandedList.append(parentNode.puzzle)  # Adding the initial parent node to the expanded list

    while not goalStateFound:  # loop as long as the goal state has not been found
        children = getChildren(parentNode.puzzle)  # children = the children of the parent node
        parentNode.children = children
        # Begin loop of row of CHILDREN
        for child in children:
            if not goalStateFound:
                if child == goalState:  # Condition if child is the goal state
                    childNode = Node(parentNode, child, 1)  # Creating node for child
                    list.append(childNode.puzzle.index('8'))  # add 8 index to 'list'
                    while parentNode.puzzle != puzzle:  # loop through parents except for last parent (initial puzzle)
                        list.append(parentNode.puzzle.index('8'))  # add parent node's 8 index to 'list'
                        parentNode = parentNode.parent  # re-assign parent node to its own parent
                    goalStateFound = True  # Once all indexes have been placed in list, goal state = true
                    break
                elif child not in expandedList:  # if child node is not a repeat
                    childNode = Node(parentNode, child, 1)  # Create child node
                    queue.append(childNode)  # Add child node to queue
        # End loop of row of CHILDREN
        if not goalStateFound:  # Once all above children have been added to queue, pop node off queue of children
            parentNode = queue.pop(0)
            expandedList.append(parentNode.puzzle)
    list.reverse()  # once the list has been filled, its initially backwards so it is reversed
    endTime = datetime.datetime.now()
    executionTime = endTime - startTime
    print('BFS() Execution Time: ', int(executionTime.total_seconds() * 1000), 'ms')
    return list  # Solution path list is returned


"""
Stack:
stack = []
stack.append('a')
print(stack.pop())
"""
#   Here you need to implement the Depth First Search Method
def dfs(puzzle):
    puzzle = "".join([str(number) for number in puzzle])  # Converts array/list to string
    parentNode = Node(0, puzzle, 0)  # Setting the initial puzzle as a parent node
    goalState = "012345678"
    goalStateFound = False
    list = []  # Solution path list to be returned
    stack = []  # Visited nodes stack
    stack.append(parentNode)    # Adding initial parent node to the stack
    stack.pop()     # Popping the initial parent node from the stack
    expandedList = []   # Expanded nodes list
    expandedList.append(parentNode.puzzle)  # Adding the initial parent node to the expanded list

    while not goalStateFound:  # loop as long as the goal state has not been found
        children = getChildren(parentNode.puzzle)  # children = the children of the parent node
        parentNode.children = children
        # Begin loop of row of CHILDREN
        for child in children:
            if not goalStateFound:
                if child == goalState:  # Condition if child is the goal state
                    childNode = Node(parentNode, child, 1)  # Creating node for child
                    list.append(childNode.puzzle.index('8'))  # add 8 index to 'list'
                    while parentNode.puzzle != puzzle:  # loop through parents as long as the string != initial puzzle
                        list.append(parentNode.puzzle.index('8'))  # add parent node's 8 index to 'list'
                        parentNode = parentNode.parent  # re-assign parent node to its own parent
                    goalStateFound = True  # Once all indexes have been placed in list, goal state = true
                    break
                elif child not in expandedList:  # if child node is not a repeat
                    childNode = Node(parentNode, child, 1)  # Create child node
                    stack.append(childNode)  # Add child node to stack
        # End loop of row of CHILDREN
        if not goalStateFound:  # Once all above children have been added to stack, pop node off stack of children
            parentNode = stack.pop()
            expandedList.append(parentNode.puzzle)
    list.reverse()  # once the list has been filled, it's initially backwards so it is reversed
    return list  # Solution path list is returned

#   Takes string value as input and returns heuristic computation based on 0, 5, and 8
def h(input):
    zeroCoord = []
    fiveCoord = []
    eightCoord = []
    matrix = [[], [], []]
    num = 0  # num is used for each char in 'input'
    #   for loop assigns input to 2d array matrix, records coordinates of '0', '5', '8'
    for x in range(3):  # x is used for recording y coord, and for each row in the 2d matrix
        for y in range(3):  # y is used for recording x coord, and for each column in the 2d matrix
            matrix[x].append(input[num])  # Add character of string to 2d array
            if input[num] == '0':
                zeroCoord.append(y + 1)
                zeroCoord.append(x + 1)
            elif input[num] == '5':
                fiveCoord.append(y + 1)
                fiveCoord.append(x + 1)
            elif input[num] == '8':
                eightCoord.append(y + 1)
                eightCoord.append(x + 1)
            num = num + 1  # Increment the char of the string
    zeroDist = abs(zeroCoord[0] - 1) + abs(zeroCoord[1] - 1)
    fiveDist = abs(fiveCoord[0] - 3) + abs(fiveCoord[1] - 2)
    eightDist = abs(eightCoord[0] - 3) + abs(eightCoord[1] - 3)
    totalDistance = zeroDist + fiveDist + eightDist
    return totalDistance

#   Takes list of states as input and returns the minimum state
def findMinState(stateList):
    states = stateList
    minDistance = states[0].h_cost + states[0].g_cost  # Sets minimum distance to the first distance
    minGValue = states[0].g_cost  # Sets minimum g value to the first g_cost
    minIndex = 0  # Final index of the minimum state, 0 for now

    # for loop runs through the states, returning the index of the minimum state
    # checks for repeated minimum values and compares their g values for accurate choice
    for state in states:
        # if checks for a repeated minimum distance
        if (state.h_cost + state.g_cost) == minDistance:
            # if checks if the repeated minimum distance has a smaller g value
            if state.g_cost < minGValue:
                minGValue = state.g_cost
                minIndex = states.index(state)  # set minIndex to the new index of the smallest G Value
        # elif checks if state's distance is < the current minimum distance
        elif (state.h_cost + state.g_cost) < minDistance:
            minDistance = state.h_cost + state.g_cost
            minGValue = state.g_cost
            minIndex = states.index(state)
    return states[minIndex]

def astar(puzzle):
    startTime = datetime.datetime.now()

    puzzle = "".join([str(number) for number in puzzle])  # Converts array/list to string
    mem_list = []   # list of states that are reached but not expanded yet
    expanded_list = []  # list of all expanded states to avoid repeats
    expanded_listStrings = []  # list of all expanded state value strings to avoid repeats
    goalState = "012345678"
    expanded_goal_state = 0

    # Initializing initial_state and adding to mem_list
    initial_state = State(puzzle)
    initial_state.h_cost = h(initial_state.value)
    mem_list.append(initial_state)

    while mem_list is not []:
        minimum_state = findMinState(mem_list)  # Find minimum_state out of mem_list
        mem_list.remove(minimum_state)  # Remove minimum state from mem_list
        # Goal State Condition
        if minimum_state.value == goalState:
            expanded_goal_state = minimum_state
            break
        expanded_list.append(minimum_state)  # Add minimum state to expanded_list
        expanded_listStrings.append(minimum_state.value)

        # For-Loop removes repeated states from mem-list once one has been expanded
        for state in mem_list:
            if state.value == minimum_state.value:
                mem_list.remove(state)

        # Returns children of minimum_state as a list of strings
        childrenStrings = getChildren(minimum_state.value)

        # For-Loop runs through each child string and checks that it is not in expanded_list before initialization
        for string in childrenStrings:
            if string not in expanded_listStrings:
                child = State(string)
                child.parent = minimum_state
                child.g_cost = minimum_state.g_cost + 1
                child.h_cost = h(child.value)
                mem_list.append(child)

    # Initializing path[] by tracing back parents
    parent = expanded_goal_state.parent
    path = []
    path.append(expanded_goal_state.value.index('8'))
    while parent is not initial_state:
        path.append(parent.value.index('8'))
        parent = parent.parent
    path.reverse()

    endTime = datetime.datetime.now()
    executionTime = endTime - startTime
    print('AStar() Execution Time: ', int(executionTime.total_seconds() * 1000), 'ms')

    return path
