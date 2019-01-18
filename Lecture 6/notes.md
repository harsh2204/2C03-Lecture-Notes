# <center>Lecture 6</center>
---
# Union-Find
### Dynamic connectivity problem

__Definition__: In computing and graph theory, a dynamic connectivity structure is a data structure that dynamically maintains information about the connected components of a graph.

In simple terms, you could think of a dynamic set of numbers that are constantly being 
updated. This means, there are numbers being added and removed at the same time, and the problem is how do we maintain information about connections within the set.

#### Given a set of `N` objects, support two operations:
- Connect two objects.
- Is there a path connecting two objects.
![connectivity_problem][sl1]

---
#### Modelling the object and its operations

This object can be modelled by a simple array where the integers of the objects are the indices of the array.

The `connected-to` relationship on the other hand can be modelled by an equivalence relation:
- **Reflexive**: `p` is connected to `p`.
- **Symmetric**: if `p` is connected to `q`, then `q` is connected to `p`.
- **Transitive**: if `p` is connected to `q` and `q` is connected to `r`, then `p` is connected to `r`.

__Connected component (dfn.)__: Maximal `set` of objects that are mutually connected.
<insert picture of connected components>

---
### Implementing the Operations

- __Find__: In which component is object `p`?
- __Connected__: Are objects `p` and `q` in the same component?
- __Union__: Replace components containing objects `p` and `q` with their union.

#### Union-Find API

(Initial stuff. Can be skipped.)
**Goal**. Design efficient data structure for union-find.
- Number of objects N can be huge.
- Number of operations M can be huge.
- Union and find operations may be intermixed.
#### Quick Find [eager approach]
**Data Structure**.
- Integer array `id[]` of length `N`.
- Interpretation: `id[p]` is the id of the component containing the value `p`.

Here, the id of a component refers to the first integer in the component. For example:

	Component: {8} has an id of 8. {8, 2, 1, 3} would also have an id of 8 if 2, 1, 3 were added after 8.
We only do this to simplify things computationally. You could easily use a symbol table (Chapter 3) and use any kind of value other than integers (which you already do here).

What does this mean for the find operation?

The find operation can be easily implemented by an array access with constant time. Similarly our connected operation takes constant time due to only two array accesses. So constant time means all good right?

Right! except we forgot about the union function.

How would you implement the union function?

_Naive Approach_: You could just pick one of the two connected components to be merged into the other. Lets say we have two connected components `p` and `q` who have the `id` values of `4` and `1` respectively.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`p:{4, 0, 2}` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `q:{1, 3}`

&nbsp;&nbsp;&nbsp;&nbsp;`id[] = [0, 1, 2, 3, 4]`
&nbsp;&nbsp;&nbsp;&nbsp;`values: 4, 1, 4, 1, 4`

[sl1]: /a/raw/b/algos.png "Order of Growth - Runtimes"
