#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0
    while (a < n * n * n):
      a = a + n * n


The runtime complexity of this is O(n). If n = 1, a is compared to 1 and will update a to 1, if n = 2, it will iterate between 1 and 2, thus will produce two values and so on...


b) sum = 0
   for i in range(n):
     j = 1
     while j < n:
       j *= 2
       sum += 1

The runtime complexity is O(n^2). The first for loop is O(n), the nested while loop is O(n), but because it is nested, the number of operations is n * n. The multiplication and addition operations are both O(n). Since n^2 is more significant than n, then the final complexity is O(n^2)

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)


The return statements is composed of two parts. The value 2 will always stay as value 3 for any number of bunnies not equal to 0, thus this is O(1).  The second component is bunnyEars(bunnies - 1) which has a worst case complexity of O(n-1). Thus as a whole the final runtime complexity is O(n)

## Exercise II

A. Naive way - 
Since I have a lot of eggs, I could try a naive way of solving this by trying first floor, drop and check if it breaks. If not move on to 2nd floor, drop and check if it breaks, and so on. Thus the worst case scenario would be O(n).


B. Binary Search - 
A more efficient way would be to do a binary seach. Start at n/2. If the egg breaks there, then that's your f. If it doesn't, then most likely, it will not break being dropped from lower floor either. The second attempt will be at 3n/4, with is halfway between the n/2 and top floor. If it breaks there, then thats your f. If it doesnt break there, then it is als not likely to break on any floor below that. Next one will be at 7n/8, which is halway between the last drop point and top floor.. and repeat the process until f is located. In this case the run time complexity is O(logn).

'''
let f = the floor where the egg breaks
    n = array of floor numbers e.g [0,1,2,...n-1]
'''
def egg_drop_at(n, f):
  # define the lowest and highest possible floor number
  lowest = 0
  highest = len(n) - 1
  mid = 0

  # As long as the lowest floor and highest floors are assigned accordingly
  while lowest <= highest:
    # the middle floor is the average of the lowest and highest, locate that floor
    mid = (lowest + highest)//2

    # check if egg does not break at mid floor, then ignore lower half.
    if n[mid] < f:
      #assign a new lowest floor
      lowest = mid + 1

    # if the egg breaks at this floor, it is possible to break at any of the lower half floors
    elif n[mid] > f:
      # the reassign a new highest floor
      highest = mid - 1

    else: 
      return mid

  # if the egg does not break at all even at the highest floor    
  return -1