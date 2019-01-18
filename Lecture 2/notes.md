### <center>Datastructures and Algorithms have nothing to do with theory.</center>
---
* What is an `algorithm`?

			      Algorithm
		**input** -----------> **output**

	Example: Search

	* Input: Sequence of **n** numbers {a<sub>0</sub>,a<sub>1</sub>...,a<sub>n</sub>}

	* Output:Index **i** if x = a<sub>i</sub>

* When someone asks you what's the best searching algorithm?
	
	It depends!

* Engineering is the efficient management of resources. eg `Input Data, Available Memory, etc`

* In this course we will be covering `Runtime Resources` and `Memory Analysis`.

---

* Q. How (ie. at what level of detail) do we describe an algorithm?

	* **High:** In English!
	* ***Medium:*** Pseudocode
		```python
		function binary_search_leftmost(A, n, T):
		    L := 0
		    R := n
		    while L < R:
			m := floor((L + R) / 2)
			if A[m] < T:
			    L := m + 1
			else:
			    R := m
		    return L
		```
	* **Low**: In actual Java, C, C++, Python .. code
---

* Q. What is a `data structure`?
	* An organization of data (data + book-keeping info)
	* Operations on data supported by the organization

---

### <center>Lecture 2: </center>
* Q. What is a `data structure`?
	* An organization of data (data + book-keeping info)
	* Operations on data supported by the organization

* Example: **Linked list**
	```c
	typedef struct{
		Item_type item;
		List_element *next;
		}List_element;

	typedef struct{
		List_element *start;
		}List L;
	```
	Linked lists have book keeping data, namely the *next pointer. This is data that you make. 

---
>**Client**: program using operations defined in interface.

>**Implementation**: actual code implementing operations.

>**Interface**: description of data type, basic operations.
---

#### Stacks, Bags and Queues

* Stack:
	* A stack looks like an array.
	* Value : collection of objects.
	* Operations : `insert`, `remove`,`iterate`, test if empty
	* Intent is clear when we insert

![slide][sl1]

**Stack**: Examines the item most recently added.	<- `LIFO="last in first out"`

**Queue**: Examines the item least recently added.	<- `FIFO="first in first out"`

You always insert and read at the begining of the stack.

---
##### <center>Linked-Lists vs Arrays for implementing stacks</center>
#### Stack: linked-list implementation
![slide2][sl2]
In a linked list, you would want to think about the operations that are to be performed on the list, namely `push` and `pop`. Now considering option **`B`**, we can see that if the top of the stack is at the end of the linked list, the cost of operations like `push` and `pop` will be huge, since you would have to traverse through the entire list to perform any of the functions. Therefore, option **`C`** shows the optimal position for the top of the stack that is on the head node of the linked list.

##### Implementation
```java
public class LinkedStackOfStrings
{
	private Node first = null;
	private class Node
	{
		String item;
		Node next;
	}
	public boolean isEmpty()
	{
		return first == null;
	}
	 
	public void push(String item)
	{
		 Node oldfirst = first;
		 first = new Node();
		 first.item = item;
		 first.next = oldfirst;
	}
	public String pop()
	{
		 String item = first.item;
		 first = first.next;
		 return item;
	}
 }

```
##### Performance

In java,

**Computation**: Every operation takes constant time in the worst case.

**Memory**: A stack with `N` items uses approximately ~ `40 * N` bytes 
![stack][sl3]

#### Stack: Array implementation
![arr][sl4]

Again, whenever talking about a better implemenation for an interface, we use operations to figure out the best one. Take option **`C`** for instance, if we want to perform a push, we must copy each of the elements over to its next index, and then add our new element to the top of the stack, which is the first index. That would be a bad choice due to its computational complexity. Therefore, **`B`** is the correct idea for implementing a fixed stack using an array.
##### Implementation

```java
public class FixedCapacityStackOfStrings
{
	private String[] s;
	private int N = 0;
	public FixedCapacityStackOfStrings(int capacity)
	{
		s = new String[capacity];
	}
	public boolean isEmpty()
	{ return N == 0; }
	public void push(String item)
	{
		s[N++] = item;
	}
	public String pop()
	{ return s[--N]; }
}

```
##### Overflow and Underflow
* **Underflow**: throw exception if pop from an empty stack.
* **Overflow**: use resizing array for array implementation. 

- __Loitering__ : Holding a reference to an object when it is no longer needed.

![loit][sl5]

---
##### Dynamic Arrays / Resizing Arrays
#### The problem
![resiz][sl6]

If we were to resize the array one by one, we would be accessing the array of size N, N<sup>2</sup> times. This information can be extrapolated from the fact that we are accessing every element in the array once, and we are writing that element into another array with size N + 1. So, that makes the number of accesses to follow the formula `N + (2 + 4 + .. 2(N-1))` which can be further expanded into `N + (2(N-1) + 2)/2 * (2(N-1))` using Newton's Summation Identity. This explains why there is an ~ N<sup>2</sup>.

- Q. How to grow array?
- A. If array is full,  create a new array of __twice__ the size, and copy items.

```java
public ResizingArrayStackOfStrings()
{ s = new String[1]; }
public void push(String item)
{
	if (N == s.length) resize(2 * s.length);
	s[N++] = item;
}
private void resize(int capacity)
{
	String[] copy = new String[capacity];
	for (int i = 0; i < N; i++)
	copy[i] = s[i];
	s = copy;
}

```

__Array accesses to insert first N = 2<sup>i</sup> items. `N + (2 + 4 + 8 .. + N) ~ 3N`.__

<center>__Array growing ☑__</center>

---
- Q. How to shrink array?

__Efficient Solution__
- `push()`: double size of array `s[]` when array is full.
- `pop()`: halve size of array `s[]` when array is __one-quarter full__.

```java
public String pop()
{
	String item = s[--N];
	s[N] = null;
	if (N > 0 && N == s.length/4) resize(s.length/2);
	return item;
}

```

__Invariant__: Array is between 25% and 100% full.

---
<center>__end of lecture__</center>

[sl1]: /a/raw/b/Screenshot_20190109_144626.png "Stack vs Queue"
[sl2]: /a/raw/b/linked-list-stack.png "Linked-List Stack Question"
[sl3]: /a/raw/b/mem_perf.png "Memory Performance"
[sl4]: /a/raw/b/stack_array.png "Array Stack Question"
[sl5]: /a/raw/b/loitering.png "Loitering"
[sl6]: /a/raw/b/resizing1.png "Resizing Problem"
