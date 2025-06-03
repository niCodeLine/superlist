# Lista

Have been feeling that ```list``` in python are missing functionalities?  

Do not longer worry, here you have a lightweight wrapper around Python lists with chainable, functional-style methods.


## Features

- Add items at any position
- Remove by item OR position
- Find all indexes of an item
- Replace items by value
- Slice, iterate, and combine like native lists

## Installation

Just copy the `Lista` class to your project — no external dependencies.

## Usage

To create a Lista:
```python
from your_module import Lista

my_list: list = [1, 2, 3, '4']
l = Lista(my_list)
# [1, 2, 3, 4]
```
*Note: for the followings examples we're gonna be using the previous list.*

### .add(item, position=-1)
Add an item at a given position. Default adds to the end.
```python
l = l.add(5)
# [1, 2, 3, '4', 5]

l = l.add('middle', 2)
# [1, 2, 'middle', 3, '4', 5]

l = l.add('almost end', -2)
# [1, 2, 'middle', 3, '4', 'almost end', 5]

```

### .pops(item=None, position=None)
Remove an item by value or by index.

```python
l.pops(item=2)   
# [1, 3, '4']

l.pops(position=1)
# [1, 3, '4']

l.pops(position=-1)
# [1, 2, 3]
```

### .index(item)
Get all indexes where item appears.

```python
Lista([1, 2, 2, 3]).index(2)
# (1, 2)
```

### List-style features


```python
print(l[0])         # 1
print(l[1:])        # [2, 3, '4']
print(len(l))       # 4
print(2 in l)       # True
print(l + [4, 5])   # [1, 2, 3, '4', 4, 5]
print((l + 6))      # [1, 2, 3, '4', 6]

l[1] = 'changed'
print(l)            # [1, 'changed', 3, '4']

for item in l:
    print(item)     
# 1
# 2
# 3
# '4'
```

## Features

- **Add to whatever position you like**
- **Better way of deleting items**
- **Find items easier**
- **Still get the list common features**


## Contributions

Contributions are welcome! If you have improvements or fixes, please send a pull request or open an issue in the GitHub repository.

## License

This project is licensed under the MIT License.  
Do whatever you want.

## Contact

Nico Spok - nicospok@proton.me
GitHub: niCodeLine
