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
