# L-systems
A final project for Foundations of Computer Science (Fall 2023) at Olin College of Engineering 

Daniel Sudzilouski and Sparsh Gupta

Implementing the L-system rewrite: https://en.wikipedia.org/wiki/L-system.


## L-systems vs Grammars

### Context-free case
At each iteration, an L-system will apply each rule as many times as possible. A traditional grammar, on the other hand, will apply one rule at a time at each iteration. This can make a difference in practice for example: 

<table>
    <td colspan="2">Traditional Grammar Example</td>
  <tr>
    <td>Start</td>
    <td>$$S$$</td>
  </tr>
   <tr>
    <td>Terminals</td>
    <td>$$\{S\}$$</td>
  </tr>
  <tr>
    <td>Non-Terminals</td>
    <td>$$\{\}$$ </td>
  </tr>
  <tr>
    <td>Rules</td>
    <td> $$\{S \rightarrow SS\}$$ </td>
  </tr>
     <tr>
    <td>Language</td>
    <td>$$\{S, SS, SSS, SSS...\}$$</td>
  </tr>
</table>


<table>
    <td colspan="2">L-system Grammar Example</td>
  <tr>
    <td>Start</td>
    <td>$$S$$</td>
  </tr>
   <tr>
    <td>Terminals</td>
    <td>$$\{S\}$$</td>
  </tr>
  <tr>
    <td>Non-Terminals</td>
    <td>$$\{\}$$ </td>
  </tr>
  <tr>
    <td>Rules</td>
    <td> $$\{S \rightarrow SS\}$$ </td>
  </tr>
     <tr>
    <td>Language</td>
    <td>$$\{S, SS, SSSS, SSSSSSSS\}$$</td>
  </tr>
</table>


### Stochastic Grammar L-systems

Stochastic Grammar involves introducing randomness into the production rules of L-systems.
Deterministic L-systems have specific rules associated to it to have a unique replacement for every symbol, and stochastic L-systems
add probabilities to these rules of replacement causing variability and randomness in the generation of grammar.

## Examples of L-systems

### Fractal Plant

The Fractal Plant is a mathematical model of plant growth that produces intricate and self-replicating patterns. It simulates the branching structures seen in nature by iteratively applying rules to symbols, resulting in the creation of complex and visually appealing plant-like forms.

**<u>Instruction set</u>** [[wiki]](https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant)

variables : X F <br>
constants : + − [ ] <br>
start  : X <br>
rules  : (X → F+[[X]-X]-F[-FX]+X), (F → FF) <br>
angle  : 25° <br>

We initialize an empty stack first. Here, F means "draw forward", − means "turn right 25°", and + means "turn left 25°". X does not correspond to any drawing action and is used to control the evolution of the curve. The square bracket "[" corresponds to saving the current values for position and angle, and we push it to the top of the stack, and when the "]" token is encountered, we pop the stack and reset the position and angle. Every "[" comes before every "]" token.

### Stochastic Fractal Plant

A stochastic fractal plant is a generated using stochastic (random) processes and fractal geometry. It incorporates randomness to simulate the natural variability found in plants, creating realistic and diverse virtual plant structures.

**<u>Instruction set</u>** [[ref - Page 28 (Section 1.7)]](http://algorithmicbotany.org/papers/abop/abop.pdf)

variables : F <br>
constants : + − [ ] <br>
start  :  F <br>
rules  : <br>
F --P(0.33)--> F[+F]F[-F]F, <br>
F --P(0.33)--> F[+F]F, <br>
F --P(0.34)--> F[-F]F <br>
angle  : 25° <br>

Here, F means "draw forward", − means "turn right 25°", and + means "turn left 25°". The square bracket "[" corresponds to saving the current values for position and angle, and we push it to the top of the stack, and when the "]" token is encountered, we pop the stack and reset the position and angle. Every "[" comes before every "]" token.

### Koch Curve

The Koch Curve is a mathematical fractal curve that exhibits self-similarity, meaning it retains a similar pattern at different scales. It is constructed by repeatedly replacing each straight line segment with a smaller equilateral triangle, creating a progressively more detailed and complex geometric shape. [[wiki]](https://en.wikipedia.org/wiki/Koch_snowflake)

**<u>Instruction set</u>** [[wiki]](https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve)

variables : F <br>
constants : + − <br>
start  : F <br>
rules  : (F → F+F−F−F+F) <br>

Here, F means "draw forward", + means "turn left 90°", and − means "turn right 90°"

### Sierpinski Triangle

The Sierpinski Triangle is a geometric fractal that results from recursively removing triangles from an equilateral triangle. Starting with an initial triangle, smaller triangles are successively removed from its center, creating a self-replicating pattern of triangles within triangles. [[wiki]](https://en.wikipedia.org/wiki/Sierpiński_triangle)

**<u>Instruction set</u>** [[wiki]](https://en.wikipedia.org/wiki/L-system#Example_5:_Sierpinski_triangle)

variables : F G <br>
constants : + − <br>
start  : F−F−F <br>
rules  : (F → F−G+F+G−F), (G → GG) <br>
angle  : 120° <br>

Here, F means "draw forward", G means "move forward", + means "turn left by angle", and − means "turn right by angle".

### Dragon Curve

The Dragon Curve is a self-replicating geometric pattern generated by iteratively folding a strip of paper. It is a space-filling curve that exhibits fractal-like properties, forming a complex, dragon-like shape through a sequence of simple folding steps. [[wiki]](https://en.wikipedia.org/wiki/Dragon_curve)

**<u>Instruction set</u>** [[wiki]](https://en.wikipedia.org/wiki/L-system#Example_6:_dragon_curve)

variables : F G <br>
constants : + − <br>
start  : F <br>
rules  : (F → F+G), (G → F-G) <br>
angle  : 90° <br>

Here, F and G both mean "draw forward", + means "turn left by angle", and − means "turn right by angle".

