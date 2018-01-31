# Random Number Generators

How can a deterministic computer generate random numbers.

Computers need access to random numbers. Random numbers are used to
+ Encrypt information
+ Deal cards and in solitaire
+ Simulate unknown variables like weather prediction

## Terms

**Deterministic** actions are determined by a prescribed set of instructions.
**Inverse Transform Sampling**
**Probablility Distribution Function**
**Cumululative Distribution Function**




Donald Knuth - In a sense, there is no such thing as a random number. For example, is 2 a random number? Rather, we speak of a sequence of independent random numbers with a specified distribution.

## True Random Number Generators

Computers require external input to generate random numbers. They inherit the randomness of the world, using hardware such as a geiger counter.

External hardware is is not very fast, and not reproducible.


## Pseudorandom Number Generators

+ Easily replicable
+ Don't require extra hardware or devices
+ Efficient


All sequences of pseudorandom numbers eventually repeat. The number of terms in the sequence before it repeats is called the period.


If you have a range of numbers from 0,9999, it is impossible to go through more than 10,000 terms without repeating. Each number in the sequence is determined by the one before it.


## Middle square algorithm
**by Von Neuman?**

+ Start with a number
+ Square the number and extract the middle 4 digits
+ Repeat the process for n


## Linear Congruential Generator

This requires four variables to derive it's numbers.
+ modulus: m = 7829
+ multiplier: a = 378
+ increment: c = 2310
+ seed = 4321

(seed * a + c)mod m = (4321 * 378 + 2310)mod 7829 = 7216

```
Xn+1 = (a*Xn+c)mod m
```
The numbers will be between 0 and 7828 - zero to m-1.

With proper numbers for the modulus, multiplier, and increment, the linear congrunetial generator will run for much longer before repeating than the middle-square algorithm.


## Mersenne Twister



## Uniform Distribution

The distribution of points between 0,1


## Other

What does it mean for a sequence to be random? There's no one way to determine a sequence is random, but there are some statistics that can help us understand the sequence.

+ compute the running average, or mean
+ plot a historgram

##


## Resources

https://www.youtube.com/watch?v=C82JyCmtKWg
