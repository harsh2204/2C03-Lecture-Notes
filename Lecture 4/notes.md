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

---
### Mathematical Modeling for running time.

__Total running time__ : sum of cost × frequency for all operations.
- Need to analyze program to determine set of operations.
- Cost depends on machine, compiler.
- Frequency depends on algorithm, input data.

__Challenge__. How to estimate constants.
![ops][sl1]

So my running time depends on the number of operations and the sequence of them.

## <center>T(n) = A . c<sub>1</sub> + B . c<sub>2</sub> + ... + X . c <sub>n</sub></center>

![ops2][sl2]

Here, the increment has a frequency of N to 2N because there are two variables being incremented namely, `count` and `i`. An array of 0's will give you 2N where as an array of numbers without 0's  will be only N.

---
### 2-Sum Problem.

Frequencies

![ops3][sl3]

Now imagine what would happen here for a 3-Sum algorithm...

This is a bit tedious. And too much math. So we will engineer the heck out of this.

---

- What if, of all the operations, I am doing an approximation and all the running times are the same for all of them. So lets make this constant run time 1.

- Why am I doing that?

- Looking at the frequencies on the chart. The last 4 frequencies are a function of N<sup>2</sup> and the rest are of only N. Recall the fact that we are doing __asymptotic worst case analysis__ and that in the long run, those `N` functions will not contribute to our approximationvery much. Now onto the `N`<sup>`2`</sup>, we look at the biggest term in the function expansion. For example, for the `array access` field, the function can be expanded into `N`<sup>`2`</sup>`- N`, we can just use the `N`<sup>`2`</sup> to approximate and compensate for other operations that are also happening in the algorithm. So we can say that we have `N`<sup>`2`</sup> array accesses as well as `N`<sup>`2`</sup> increments and so on..

#### <center>In essence, we pick the most frequent operation in the algorithm</center>

__Cost Model__: It is the choice of operation with the most frequent occurence in an algorithm. Here, our cost model was `array access`.

---
### Tilde Notation

- Estimatee running time as a function of input size `N`.

Ex.  `1/6 N`<sup>`3`</sup>` + 20N + 16	~ 1/6 N` <sup>`3`</sup>

Technical Defination (asymptotic): `f(N) ~ g(N)` means: 
<center>![til][sl4]</center>

So simplifying the frequency table with tilde approximation, we get the following.

![op4][sl5]

Here, we can pick either of `array access` or `increment` because we're looking for the worst case, which means the bigger number.

[sl1]: /a/raw/b/table1.png "Operation Runtimes"
[sl2]: /a/raw/b/table2.png "Operation Runtimes"
[sl3]: /a/raw/b/table3.png "Operation Runtimes"
[sl4]: /a/raw/b/tildle.png "Operation Runtimes"
[sl5]: /a/raw/b/table4.png "Operation Runtimes"
