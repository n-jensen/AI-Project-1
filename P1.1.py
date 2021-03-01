
class nodes:
    def __init__(self, n):
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
                new.append(nodes('x'))
                new[-1].row = r
                new[-1].column = c
            elif r == 2 and c == 1:
                new.append(nodes('x'))
                new[-1].row = r
                new[-1].column = c
            elif (r == 3 and c == 1) or (r == 3 and c == 2):
                new.append(nodes('x'))
                new[-1].row = r
                new[-1].column = c
            elif r == 4 and c == 1:
                new.append(nodes('x')) 
                new[-1].row = r
                new[-1].column = c
            else:
                new.append(nodes(' '))
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
            elif (maze[i][j].key == 0) and i != 3 and j != 0:
                row_string = row_string + '    '
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

def per_direction(curr, direction, stack, move_num):
    if(direction != None) and (direction.name != 'x'):
        move_num[0] = move_num[0] + 1
        direction.key = move_num[0] ##EACH step has its own iterated key
        direction.state = 'unexplored'
        stack.append(direction)

        
def DFS(maze, start_node, goal_node, stack, exp_stack, idscount, rs, cs):
    dfscount = 0
    move_num = [0]
    while (0 <= dfscount < idscount):
        exp_stack.append(stack.pop(-1))
        exp_stack[-1].state = 'explored'
        curr = exp_stack[-1]
        
        if (curr.name != 'x') and ( 0 <= curr.column-1 < cs) and (search_stack(exp_stack, maze[curr.row][curr.column-1]) == False) and (search_stack(stack, maze[curr.row][curr.column-1]) == False):
            per_direction(curr, maze[curr.row][curr.column-1], stack, move_num)##(curr, curr.west, stack, move_num)

        if (curr.name != 'x') and ( 0 <= curr.row-1 < rs) and (search_stack(exp_stack, maze[curr.row-1][curr.column]) == False) and (search_stack(stack, maze[curr.row-1][curr.column]) == False):
            per_direction(curr, maze[curr.row-1][curr.column], stack, move_num)##(curr, curr.north, stack, move_num)
        
        if (curr.name != 'x') and ( 0 <= curr.column+1 < cs) and (search_stack(exp_stack, maze[curr.row][curr.column+1]) == False) and (search_stack(stack, maze[curr.row][curr.column+1]) == False):
            per_direction(curr, maze[curr.row][curr.column+1], stack, move_num)##(curr, curr.east, stack, move_num)

        if (curr.name != 'x') and ( 0 <= curr.row+1 < rs) and (search_stack(exp_stack, maze[curr.row+1][curr.column]) == False) and (search_stack(stack, maze[curr.row+1][curr.column]) == False):
            per_direction(curr, maze[curr.row+1][curr.column], stack, move_num)##(curr, curr.south, stack, move_num)
        
        dfscount += 1
        
        if (dfscount == idscount):
            if (move_num[0]/2) < idscount:
                dfscount = 1
                while (stack[-1] != stack[0]): ##move all but index0 from stack into explored stack
                    exp_stack.append(stack.pop(-1))
            elif (move_num[0]/2) >= idscount:
                while(stack): ##move ALL from stack into explored stack
                    exp_stack.append(stack.pop(-1)) 
    print_maze_key(maze)
    
def IDS(maze, start_node, goal_node, stack, exp_stack, idscount, rs, cs):
    idscount = 1
    found_goal = False
    
    while (idscount <= 9):
        print('ids depth = ', idscount)
        stack.append(start_node)            
        exp_stack = []
        found_goal = DFS(maze, start_node, goal_node, stack, exp_stack, idscount, rs, cs)
        idscount += 1
    
nrows = 6
ncols = 5

stack = []
exp_stack = []
dfs_counter = 0 
move_num = 0

maze = make_maze() 
print_maze(maze)

maze[3][0].name = 'o'
start_node = maze[3][0]

maze[2][2].name = 'g'
goal_node = maze[2][2]

##stack.append(start_node)

IDS(maze, start_node, goal_node, stack, exp_stack, idscount, nrows, ncols)  
    
    
    