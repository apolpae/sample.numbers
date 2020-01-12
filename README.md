# sample.numbers
Sample program which determines all equations with a given result that can be formed from a given range of numbers
## Usage
```sh
sample_numbers [range-start=9] [range-end=0] [result=200]
```

For example:

```sh
~$ sample_numbers 9 0 999
Equations with result of 999 and a dictionary from 9 to 0:
987-6+5+4-3+2+10
9+8+765+4+3+210
987+6-5-4+3+2+10
9+8+7+654+321+0
987+6+5-4-3-2+10

~$ sample_numbers 0 9
Equations with result of 200 and a dictionary from 0 to 9:
123-4+5-6-7+89
0+123+4+5+67-8+9
234-44-7+8+9
0+1+234-5-6-7-8-9
1+234-5-6-7-8-9
0+123-4+5-6-7+89
2-3+45+67+89
123+4+5+67-8+9
```
