"""
Following the tutorial here: http://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
"""
import torch

'''
both torch.Tensor, and torch.rand return randomly intialized tensors
'''

x = torch.Tensor(5,3)
print("X:" , x)

y = torch.rand(5,3)
print("Y:", y)

''' adding two tensors, all the outputs below should be the same '''
print(x+y)
print(torch.add(x,y))
result = torch.Tensor(5,3)
torch.add(x,y, out = result)
print(result)
y.add_(x) # operations that modify tensors in-place are postfixed with an _
print(y)

'''
returns 1's along the diagonal, zeros everywhere else.
caveat: if m>n, it will returns ones along the diagonal assuming m = n, and adds 0's everywhere else
'''
print(torch.eye(5,10))

'''returns a 1-D tensor with equal steps between start and end''' 
print(torch.linspace(start = -100, end = 200, steps = 5))