# <center>Lecture 5</center>
---
### Mathematical Models for running time

__In principle__, accurate mathematical models are available.

__However__

__In practice__,
- Formulas can be complicated.
- Advanced mathematics might be required.
- Exact models best left for experts.

__Bottom line__, we use approximations for this course.

---
#### Order of growth

It is the tilde approximation without the constant.

Definition: If `f(N) ~ c g(N)` for some constant `c > 0`, then the oder of growth of `f(N)` is `g(N)`. Therefore this approximation,

- Ignores leading coefficients.
- Ignores lower-order terms.

### Common order-of-growth classifications.

The functions

1, log N, N, N log N, N<sup>2</sup>, N<sup>3</sup>, 2<sup>N</sup>

![plt][sl1]
---
##### Classification Table

![tbl][sl2]

---
## Binary Search

- First binary search publish in 1946.
- First bug-free one in 1962.
- Bug in Java's `Arrays.binarySearch()` discovered in 2006.

##### Iterative Implementation

```java
public static int binarySearch(int[] a, int key)
{
	int lo = 0, hi = a.length-1;
	while (lo <= hi)
	{
		int mid = lo + (hi - lo) / 2;
		if
		(key < a[mid]) hi = mid - 1;
		else if (key > a[mid]) lo = mid + 1;
		else return mid;
	}
	return -1;
}

```
Q. What is the runtime of this algorithm given my array is of size `N`?

- 


[sl1]: /a/raw/b/plot.png "Order of Growth - Runtimes"
[sl2]: /a/raw/b/algos.png "Order of Growth - Runtimes"
