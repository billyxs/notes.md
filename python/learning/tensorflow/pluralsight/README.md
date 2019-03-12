# Tensorflow: Getting started
Jerry Kurata

- A Tensor is an n-dimension of arrays
- Computation graph of (a * b) + c
  - Commonly called graph

>
             c -> \
a -> \             \
       multiply -> add -> (a*b)+c 
b -> /

- Tensorflow: Tensors flowing between operations
- Defined by properties Rank, Shape, and Type
  - Rank is the dimensionality of a tensor
    - Rank 0 = Scalar  eg: s = 145
    - Rank 1 = Vector  eg: v = [1, 3, 2, 5, 7]
    - Rank 2 = Matrix  eg: v = [[1,5,6], [5,3,4]]
    - Rank 3 = 3-Tensor(cube)  eg: v = [[[1,5,6], [5,3,4]], [[9,3,5], [3,4,9]], [[4,3,2], [5,8,7]]]
  - Shape is related to Rank

| Rank | Example | Shape |
-------------------------
| 0    | 145     | [0]   |
| 1    | [1, 3, 2, 5, 7] | [1] |
| 2    | [[1,5,6], [5,3,4]] | [2, 3] |
| 3    | [[[1,5,6], [5,3,4]], [[9,3,5], [3,4,9]], [[4,3,2], [5,8,7]]] | [3, 2, 3] |

- Quantitized values
  - Scaled to reduce size for faster processing
  - TPUs - TensorFlow Processing Units utilize TPUs

- Methods
  - get_shape() - returns shape
  - reshape() - changes shape
  - rank - returns data rank
  - dtype - return data type
  - cast - change data type

## Training a model with Tensorflow

- prepare data
  - generated house size and price data
- inference
  - price = (sizeFactor * size) + priceOffset
- loss measurement
  - mean square error
- optimizer to minimize loss
  - gradient descent optimizer

## Tensor types
- Constant - constant value
- Variable - values adjusted in graph
- PlaceHolder - used to pass data into graph


## Gradient descent
"Finding the steepest way down a hill"
- We take small steps and adjust as we find our way
- The learning rate should be low so our steps don't cause us to bounce around too much across the gradient
- The calculations of the direction of each step is calculated by finding the derivitives of the model with respect to its features

