class Heap:
  
  
  def __init__(self):
    self.heap_array = []
  
  
  def insert(self, value):
    """
    Inserts a value into a heap.
    
    Args:
      value: The value to be inserted
    
    Returns:

    """
    self.heap_array.append(value)
    self.percolate_up()
  
  
  def percolate_up(self):
    """
    Swaps elements in the heap from the last element inserted 
    until the min-heap property is satisfied.
    
    Args:
    
    Returns:

    """
    last = len(self.heap_array)-1
    # As long as the min-heap property is violated this swapping
    # code will run
    while self.heap_array[last] < self.heap_array[(last-1)//2] and \
          last > 0:
      parent = (last-1)//2
      temp = self.heap_array[parent]
      self.heap_array[parent] = self.heap_array[last]
      self.heap_array[last] = temp
      last = parent


  def extract_min(self):
    """
    Retrieves the first element of a heap for the user
    
    Args:
    
    Returns:
      value: The first element of the heap
    """
    # Returns None if no elements are left in the heap
    if len(self.heap_array) == 0:
      return
    value = self.heap_array[0]
    self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
    del self.heap_array[len(self.heap_array)-1]
    self.percolate_down()
    return value
  
  
  def percolate_down(self):
    """
    Swaps elements in the heap from the first element
    until the min-heap property is satisfied.
    
    Args:
    
    Returns:

    """
    last = 0
    while last < len(self.heap_array):
      # Creates a dictionary where the key is a child node's value
      # and the value is a child node's index in the heap_array
      child_dict = dict()
      if ((2 * last) + 1) < len(self.heap_array):
        child_dict[self.heap_array[(2 * last) + 1]] = (2 * last) + 1
      if ((2 * last) + 2) < len(self.heap_array):
        child_dict[self.heap_array[(2 * last) + 2]] = (2 * last) + 2
      temp = self.heap_array[last]
      swap = -1
      for key, value in child_dict.items():
        if key < self.heap_array[last]:
          self.heap_array[last] = key
          swap = value
      # If no children exist for the given last index or if the heap
      # satisfies the min-heap property this code executes
      if swap == -1:
        break
      self.heap_array[swap] = temp
      last = swap


  def is_empty(self):
    """
    Checks if the heap is empty.
    
    Args:
    
    Returns:
      The size of the heap as a boolean.

    """
    return len(self.heap_array)==0

