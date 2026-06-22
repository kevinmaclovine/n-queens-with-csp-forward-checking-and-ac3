# n-queens-with-csp-forward-checking-and-ac3

this a classic problem in algorithms which i coded it in python with csp
algorithm and with some heuristic function which i applied to it.
this program need an input file which inside it contains number of queens
and for output it makes a file (output.txt) which o means cells with 
queens and * means empty cells.heuristic function which is use in this 
problem is mrv and lvs that they are really efficient and helpful for 
finding sloution but i also add degree heuristic to it which it was a 
improvment for it and made it faster.(degree heuristic already exists for
csp problems but in n-queens we can't have different degrees but in opponion
we have three kind of queen column:1-whith two non-assigned neighbors.
2-with one non-assigned neighbor and one assigned neighbor. and 
3-with two assigned neighbors.which my priority is from 1 to 3.)
after adding ac3 as an extension it slowed down the programm but i made
few change into it and made it faster but it is still slower than times we
don't use ac3.
