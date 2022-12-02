#!/bin/bash

# Part 1
awk 'BEGIN{ max=0; total =0; } /^$/ { if (total > max) { max = total;}; total = 0 } /[0-9]*/ { total += ; } END{ print max };' food.txt 

# Part 2
echo $(($(awk 'BEGIN{ max=0; total =0; } /^$/ { print total; total = 0 } /[0-9]*/ { total += $1; };' food.txt | sort -n | tail -3 | tr "\n" "+")"0"))
