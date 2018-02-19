# Linear Algebra

+ [Graphical Linear Algebra](https://graphicallinearalgebra.net/)


## YouTube - Essence of Linear Algebra

https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab



### Chapter 1: Vectors, what even are they?
https://www.youtube.com/watch?v=fNk_zzaMoSs

"The introduction of numbers as coordinates is an act ov violence" - Hermann Weyl

The fundamental root of it all, building block, is the vector.

+ Vectors are arrows pointing in space. It is defined by it's length and the direction it is pointing


**Perspectives**
Computer Science - vectors are ordered lists of numbers
Mathematician - anything where there is a sensible notion of adding two vectors and multipliying the vector by a number

* Coordinates of a vector is a pair of numbers that give instructions on how to get from the tail of a vector to it's tip.
* Every pair of numbers gives you one and only one vector.
* Every vector is linked to only one pair of numbers.

**Adding vectors**
(1,2) + (3,4) = (4,6)
1 + 3 = 4
2 + 4 = 6

**Multiplying vectors by a number, or scalar
The scaler will stretch or shrink the vector.
(2,4)*3 = (6, 12)




## Chapter 2: Linear combinations, span, and basis vectors
https://www.youtube.com/watch?v=k7RM-ot2NWY

"Mathematics requires a small dose, not of genius, but of an imaginative freedom which, in a larger dose, would be insanity" - Angus K. Rodgers

* Each coordinate in the vector is a scalar
* î - "i hat", unit of vector in the X direction
* ĵ - "j hat", unit of vector in the Y direction
* î and ĵ are the basis of the coordinate system. They are the basis vectors
* Anytime you describe vectors numerically, it depends on an implicit choice of what basis vectors we're using. So anytime you that you are scaling two vectors and adding them, it's called a linear combination of those two vectors.
* If you lock one vector and let the other change it's value freely, it draws a straight line.
* Scaling both vectors allows one to reach any point in the coordinate system


**Span**
The set of all possible vectors you can reach with a linear combination of a given pair of vectors, is called the span.

What are all the possible vectors you can reach using only vector addtion and multiplication?

*If two vectors are pointing in the same direction, there span is a straight line. When this happens, we say the two vectors are linear dependent.
*If a vector adds another dimension to the span, they are linear independent


**Basis**
The basis of a vector space is a set of linearly independent vectors that span the full space.



## Chapter 3: Linear Transformations and Matrices

https://www.youtube.com/watch?v=kYB8IZa5AuE

**Linear transformation**
*transformation is the same as a function
*A transformation is linear if it has two properties.  All lines must remain lines without getting curved, and the origin must remain in place.
*Linear transformations keep grid lines parallel and evenly space

| 1| + |3| = -1î + 2ĵ = -1| 1| + 2|3| = |5|
|-2|   |0|                |-2|    |0|   |2|

**"2x2 Matrix"**
|x| -> x| 1| + y|3| = [  1x + 3y ]
|y|     |-2|    |0|   [ -2x + 0y ]

### Shear

