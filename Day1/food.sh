awk 'BEGIN{ max=0; total =0; } /^$/ { if (total > max) { max = total;}; total = 0 } /[0-9]*/ { total += ; } END{ print max };' food.txt 
