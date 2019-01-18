<center>Lecture 2 (contd.)</center>
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

<center>Final verdict on linked-lists vs arrays</center>
---

|Linked Lists|Arrays|
|---|---|
|It is a dynamic data structures where the size of a linked list can be modified| Is is a static data structure which means you are limited by the size of the array |
|Used for variable capacity stacks| Used for fixed-capacity stacks|
|Every operation takes constant time in the __worst case__|Every operation takes constant __amortized__ time|
|Uses extra time and space to deal with the links|Less wasted space| 


<center>__end of lecture 2 content__</center>

---
<center>Lecture 3</center>
---
### Queues

<center>![qu][sl1]</center>
<center>__Queue Visual__</center>

API Spec
|Method|Description|
|---|---|
|`QueOfStrings()`|creates an empty queue|
|`void enqueue(String item)`| insert a new string into the queue|
|`String dequeque()`| remove and return the string|
|`boolean isEmpty()`| is the queue empty?|
|~~`int size()`~~| ~~number of strings on the queue~~|


#### Linked-List Implementation

- __How to implement a queue with a linked-list?__
---
![q1][sl2]

`<answer here>`

##### Implementation steps
---
- Maintain one pointer `first` to first node in a singly-linked-list
- Maintain another pointer `last` to the last node
- Dequeue from `first`
- Enqueue after `last`.

![fig2][sl3]

##### Implementation Code

```java
public class LinkedQueueOfStrings {
	private Node first, last;
	private class Node { /* same as in LinkedStackOfStrings */ }
	public boolean isEmpty() {
		return first == null;
	}
	public void enqueue(String item) {
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;
		if (isEmpty()) first = last;
		else
			oldlast.next = last;
	}
	public String dequeue() {
		String item	= first.item;
		first		= first.next;
		if (isEmpty()) last = null;
		return item;
	}
}
```
#### Array-based Implementation
- __How to implement a fixed-capacity queue with an array?__
---
![q2][sl4]

`<answer here>`

##### Implementation steps
---

- Use array `q[]` to store items in queue.
- `enqueue()`: add new item at `q[tail]`.
- `dequeue()`: remove item from `q[head]`.
- Update `head` and `tail` modulo the `capacity`.
- Add resizing array.


![fig2][sl5]

##### Implementation Code

```java
//WIP

```
---
## <center> 1.4 Analysis of Algorithms </center>

Defining the metrics and the ways we can differentiate between different problems and find the best tools for it.

- We compare two algorithms using the same inputs. ie. the same size of data.

Q. What do you mean by the `size` of the input?

A. The `size` of the input is the size of the array, when your input is an `array`. Say if the input was two integers, the `size` of the input would be the size of the integers in terms of their bits. Given you want to find the shortest path between two nodes in a graph, you are given an input of all of the nodes and edges. The size you the inputs is the `#nodes` + `#edges`. 

>The rule of thumb is the size of my input is the number of inputs of the unitary object that my algorithm will need to manipulate to get a result.

<center>__Ask yourself, what is my algorithm gonna go through? And everything your algorithm is touching counts towards the input size__ </center>

- Q. How do we compare algorithms?
- A. Using runtime based on the same inputs for any algorithm will differ from each algorithms use case. So one metric we can choose is use the worst case scenario for each input. This makes sense as a very pessimistic metric which means that your algorithm will not take any more than that time. Therefore, we use worst case analysis for comparing algorithm.

We are doing asymptotic analysis which means that the analysis holds only past a certain `N`.
Even for small `N`s the algorithmic runtime difference will be negligibly small.

[sl1]: /a/raw/b/que1.png "Queue"
[sl2]: /a/raw/b/que_q1.png "Queue Question"
[sl3]: /a/raw/b/fig2.png "Linked-list Implementation"
[sl4]: /a/raw/b/que_q2.png "Queue Question 2"
[sl5]: /a/raw/b/fig3.png "Array-based Queue"

