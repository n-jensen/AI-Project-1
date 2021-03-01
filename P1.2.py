
class nodeA:
    def __init__(self, n):
        self.actual_cost = 0
        self.est_cost = 0
        self.weight = 0
        
        self.name = n
        self.key = 0
        self.state = None
        
        self.west = None
        self.north = None
        self.east = None
        self.south = None
        
        self.row = None
        self.column = None
        
def make_maze():
    windy_maze = []
    new = []
    rows = 6
    cols = 5
    index = 0
    for r in range(rows):
        for c in range(cols):
            if (r == 1 and c == 1) or (r == 1 and c == 2):
                new.append(nodeA('x'))
                new[-1].row = r
                new[-1].column = c
            elif r == 2 and c == 1:
                new.append(nodeA('x'))
                new[-1].row = r
                new[-1].column = c
            elif (r == 3 and c == 1) or (r == 3 and c == 2):
                new.append(nodeA('x'))
                new[-1].row = r
                new[-1].column = c
            elif r == 4 and c == 1:
                new.append(nodeA('x')) 
                new[-1].row = r
                new[-1].column = c
            else:
                new.append(nodeA(' '))
                index += 1 
                new[-1].row = r
                new[-1].column = c
                
        windy_maze.append(new)
        new = []
    return windy_maze

def print_maze(maze):
    row_string = ""
    for i in range(len(maze)): ##6
        for j in range(len(maze[0])): ##5
            row_string = row_string + str(maze[i][j].name) + "   "
        print(row_string)
        row_string = ""
   
def print_maze_key(maze):
    row_string = ""
    for i in range(len(maze)): ##6
        for j in range(len(maze[0])): ##5
            if (maze[i][j].name == 'x'):
                row_string = row_string + 'x' + '   '
            elif len(str(maze[i][j].key)) == 2:
                row_string = row_string + str(maze[i][j].key) + "  "
            else:
                row_string = row_string + str(maze[i][j].key) + "   "
        print(row_string)
        row_string = ""
        

def search_stack(stack, node_val):
    found = False
    for s in stack:
        if(s == node_val):
            return True 
    return found
        

def min_in_frontier(stack):
    node = stack[0]
    
    for f in stack:
        if(node.key > f.key) and (node.weight == f.weight):
            node = f
        elif (node.weight > f.weight):
            node = f
    return node
    
def get_est_weight(curr_node, goal_node):    
    rdist = goal_node.row - curr_node.row
    if (rdist < 0): ##if dist is - , going south
        rdist  = abs(rdist * 3)
    elif (rdist > 0): ##if dist is + , going north
        rdist = abs(rdist * 1)
        
    cdist = goal_node.column - curr_node.column
    if (cdist < 0): ##if dist is - , going east
        cdist  = abs(cdist * 2)
    elif (cdist > 0): ##if dist is + , going west
        cdist = abs(cdist * 2)
        
    dist = rdist + cdist
    return dist

def pop_current(k, stack, exp_stack):
    for s in stack:
        if s.key == k:
            exp_stack.append(s)
            stack.remove(s)

def per_direction(curr_node, goal_node, a_count, stack, act_cost):
    curr_node.key = a_count
    curr_node.actual_cost = act_cost
    curr_node.est_cost = get_est_weight(curr_node, goal_node)
    curr_node.weight = curr_node.actual_cost + curr_node.est_cost
    stack.append(curr_node)
    
def print_stack(stack):
    stack_out = []
    for s in stack:
        stack_out.append(str(s.name) + '   ')
    print (stack_out)

def A_star(maze, stack, exp_stack, rs, cs):
    a_count = 0
    while(stack):
        curr = min_in_frontier(stack) ##exp_stack[-1]
        pop_current(curr.key, stack, exp_stack)
        
        if (0 <= maze[curr.row][curr.column].column-1 < cs) and (maze[curr.row][curr.column-1].name != 'x') and (search_stack(exp_stack, maze[curr.row][curr.column-1]) == False) and (search_stack(stack, maze[curr.row][curr.column-1]) == False):
            a_count += 1
            per_direction(maze[curr.row][curr.column-1], goal_node, a_count, stack, 2 + curr.actual_cost)
            
        if (0 <= maze[curr.row][curr.column].row-1 < rs) and (maze[curr.row-1][curr.column].name != 'x') and (search_stack(exp_stack, maze[curr.row-1][curr.column]) == False) and (search_stack(stack, maze[curr.row-1][curr.column]) == False):
            a_count += 1
            per_direction(maze[curr.row-1][curr.column], goal_node, a_count, stack, 3 + curr.actual_cost)
            
        if (0 <= maze[curr.row][curr.column].column+1 < cs) and (maze[curr.row][curr.column+1].name != 'x') and (search_stack(exp_stack, maze[curr.row][curr.column+1]) == False) and (search_stack(stack, maze[curr.row][curr.column+1]) == False):
            a_count += 1
            per_direction(maze[curr.row][curr.column+1], goal_node, a_count, stack, 2 + curr.actual_cost)
            
        if (0 <= maze[curr.row][curr.column].row+1 < rs) and (maze[curr.row+1][curr.column].name != 'x') and (search_stack(exp_stack, maze[curr.row+1][curr.column]) == False) and (search_stack(stack, maze[curr.row+1][curr.column]) == False):
            a_count += 1
            per_direction(maze[curr.row+1][curr.column], goal_node, a_count, stack, 1 + curr.actual_cost)

maze = make_maze() 
print_maze(maze)          
rs = 6
cs = 5

stack = []
exp_stack = []

maze[3][0].label = 'o'
start_node = maze[3][0]
maze[2][3].label = 'g'
goal_node = maze[2][2]

stack.append(start_node)

A_star(maze, stack, exp_stack, rs, cs)
print_maze_key(maze)
