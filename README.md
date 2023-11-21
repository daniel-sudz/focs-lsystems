# L-system
A final project for Foundations of Computer Science at Olin College of Engineering implementing the L-system rewrite https://en.wikipedia.org/wiki/L-system.


## L-systems vs Grammers

#### Context-free case
At each iteration an L-system will apply each rule as many times as possible. A traditional grammer, on the other hand, will apply one rule at a time at each iteration. This can make a difference in practice for example: 

<table>
    <td colspan="2">Traditional Grammer Example</td>
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
    <td colspan="2">L-system Grammer Example</td>
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
