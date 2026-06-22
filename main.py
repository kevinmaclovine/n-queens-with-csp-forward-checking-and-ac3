from copy import deepcopy
import sys

class queen:
    def __init__( self, n):
        self.value = 0
        self.have_value = False
        self.domain = []
        self.domain_size = n
        self.degree = 2
        for i in range(n):
            self.domain.append(i)

def print_output(queens , n ):
    with open('output.txt', 'w') as file:
        for i in range(n):
            for j in range(n):
                if queens[j].value == i:
                    file.write("o ")
                else:
                    file.write("* ")
            file.write("\n")

def print_queens(queens , n):
    for i in range(n):
        if queens[i].have_value:
            print("#",i , "value:" , queens[i].value , "domian:" , queens[i].domain , "domain_size:" , queens[i].domain_size)   
        else:
            print("#" , i ,"value:none " , "domain:" , queens[i].domain, "domain_size:" , queens[i].domain_size )
        

def is_safe(selected_queen1 , selected_queen2 , value1 , value2):
    if value1 == value2 :
        return False
    value_diff = value1 - value2
    queen_pos_diff = selected_queen1 - selected_queen2
    if abs(queen_pos_diff) == abs(value_diff):
        return False
    return True

def update_domain(queens ,selected_queen , bv , n ):
    for i in range(n):
        if queens[i].have_value == False:
            j=0
            while j < queens[i].domain_size:    
                if not is_safe(selected_queen , i  , bv , queens[i].domain[j]):
                    queens[i].domain.pop(j)
                    queens[i].domain_size -= 1
                else:
                    j+=1
    return queens
    

def lcv(selected_queen , queens , n):
    tmp = []
    for i in range(n) :
        if queens[i].have_value == False and i != selected_queen:
            tmp.append(i)
    
    tmpkv = {}
    for i in queens[selected_queen].domain:
        tmpkv[i] = 0
        for j in tmp :
            for z in queens[j].domain :        
                if not is_safe(selected_queen , j , i , z):
                    tmpkv[i] += 1
                    
    sorted_dict = dict(sorted(tmpkv.items(), key=lambda item: item[1]))
    casted = {int(k): v for k, v in sorted_dict.items()}
    return list(casted.keys()) 
        
def health( queens, n):
    for i in range(n):
        if queens[i].have_value == False:
            if not queens[i].domain:
                return False
    return True

def find_max_degree(queens , n):
    min = -1
    for i in range(n):
        if queens[i].degree > min and queens[i].have_value == False:
            min = queens[i].degree
    return min           
def select_func(queens , n):
    max_degree = find_max_degree(queens , n)
    max = n+1; 
    for i in range(n):
        if queens[i].degree == max_degree and max > queens[i].domain_size and queens[i].have_value == False:
            max = queens[i].domain_size
            tmp = i
    try:
        queens[tmp+1].degree -= 1
        queens[tmp-1].degree -= 1
    except:
        pass
         
    return tmp

def complete(a , n):
    for i in range(n):
        if a[i].have_value == False:
            return False
    return True

def revise( i , j , queens):
    revised = False

    x = 0
    while x < queens[i].domain_size:
        supported = False

        for y in queens[j].domain:
            if is_safe(i, j, queens[i].domain[x] , y):
                supported = True
                break

        if not supported:
            queens[i].domain.pop(x)
            queens[i].domain_size -= 1
            revised = True
            
        else:
            x += 1

    return revised
             
def arc3(queens , n):
    queens_copy = deepcopy(queens)
    queue = []
    for i in range(n):
        for j in range(n):
            if i!=j and queens[i].have_value == False and queens[j].have_value == False:  
                queue.append((i,j))

                
    while queue:
        i, j = queue[0]
        queue.pop(0)
        if revise(i, j, queens):
            if queens[i].domain_size == 0:
                queens = queens_copy
                return False

            for k in range(n):
                if k != i and k != j and queens[k].have_value == False:
                    queue.append((k, i))

    #queens = deepcopy(queens_copy)
    #print_queens(queens , n)
    return True
        

def n_queen_csp(queens ,  n):
    if complete(queens , n):
        print_output(queens , n)
        return True
    
    selected_queen = select_func( queens , n)
    best_values = lcv(selected_queen , queens , n )
    for bv in best_values:
        previous_state = deepcopy(queens)
        queens[selected_queen].have_value = True
        queens[selected_queen].value = bv
        queens = update_domain(queens ,selected_queen , bv , n)
        #print_queens(queens , n)
        if health(queens , n) and arc3(queens,n):
            #print_queens(queens , n)    
            resault = n_queen_csp(queens , n)
            if resault == True:
                return True
                              
            queens = previous_state
        else:
            queens = previous_state

    print("no slioution found!")
    return False  
        

def initializing(n):
    queens = []
    for i in range(n):
        queens.append(queen(n))
    queens[0].degree = 1
    queens[n-1].degree = 1
    n_queen_csp(queens , n)
    
def input(inputfile):
    with open(inputfile) as f:
        n = int(f.readline())
        initializing(n)

if  len(sys.argv) != 2:
    print("invalid arguments")
    exit(-1)
input(sys.argv[1])
