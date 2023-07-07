# bridge_problem

## Problem description

This is a short python simulation to solve a math problem.

Assume we have a river and 8 nodes accorss the river and they are connected via bridges, nodes and bridges look like this:

```txt
   2-3  
  /| |\  
 1-4-5-6  
  \| |/  
   7-8  
```
  
There are 13 bridges connecting those 8 nodes. To successfully cross the bridge you have to reach node 6 from node 1.

If we have a storm coming, and each bridge have 50% chance to be destroyed, then what's the probability that the we can still cross the river at the end of the storm.

## Solution

I made a Python simulation to solve this problem, see `./src/main.py`.



