# Rectangle packing solver

This is a effective solver for 2D-rectangle-packing problem, which can find potential usage in various fields.

### Problem description
It is formalized as a typical optimization problem within such framework:

- **Input**
    + A set of rectangles
- **Output**
    + A complete arrangement of these rectangles in 2D space
- **Constraints**
    + Each rectangle is aligned to X and Y axis.
    + No overlapping is allowed.
- **Objective**
    + Minimize the area of the axis-aligning bounding box covering all rectangles.

### Analogy ###
It is like given a large piece of cloth and required is a set of small pieces for some assembling work. The objective is to cut off these required pieces with least consumption of the large cloth.

### Short explanation ###
In this implementation the greedy method is applied for its satisfying effect. Further optimization schemes can be explored by making use of the adapt this model to interface with some optimizer's settings.


## Sample output

As a simple example, an arrangement for 30 random generated rectangles is generated by this solver, plotted by `pyplot.figure`:

<p align="center">
    <img src="./sample1.png"
    width="70%"
    height="70%" />
</p>


## Highlight of this approach
- No utilities from computational graphics or computational geometry are used, since the underlying data structure resembles a Threaded-Tree, which is more abstract.
- With this structure, spatial restrictions can be detected by simple arithmetics, rather than applying geometric algorithms.
- This approach sacrifices completeness of by considering stacking direction merely upwardsrightwards. However, the results seem satisfying.
- Much more performant implementation can be derived from this Python implementation with no dependencies required.


## Restrictions and TODOs

- When many rectangles are of the same size, which is the degeneracy case, the model suffers from the disability of arranging them like a "grid".

- In this unbounded space, it seems there exists a tendency to arrange rectangles along the X or Y axis for some input with rectangles of near sizes. Though the quantitative result looks good, but setting constraints about boundaries should be made available to make the resulted bounding area more like a square.