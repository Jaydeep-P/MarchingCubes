# MarchingCubes

Naive implementation of the marching cubes algorithm in Python, this is extremely unoptimised code both in terms of memory and time complexity( not to mention that the code is written in Python)

The code simply makes .STL files by putting the vertices in a file that can later be animated ( in my case using blender) the points being used for the input are generated using a basic "meatball" algorithm.

Ways the code can be optimised:
- Linear interpolation to calculate the vertices of triangles would result in smoother shapes at very little cost
- The memory usage can be reduced quite significantly by not using a 3D array
- Just use C++ or any other lower level language, this is simple to do as the whole code doesn't really depend on any python specific features.
- Writing the output simultaneously to reduce memory usage
- Making the functions multi-threaded, this is the largest improvement and should be handled first.
