# Variable Calculator
This is a small calculator program, which allows you to make your own variables.

All variable names must only be one letter long, otherwise an error will appear.

You can assign a variable by stating its name, an equals sign, and then its value or expression. Eg:
```python
a = 10
e= 7+ 3.5
j=4 *6
f = 9 / 3
```
All of those definitions are allowed because they all have; a one character variable name, an equals sign, and a value or expression. However,
```python
num = 8
n = &4
a = *+
```
are all illegal.
`num = 8`
Is illegal because the variable name has more than one character
```python
n = &4
```
Is illegal because the value has to be a number or operater.
```python
a = *+
```
Is illegal because you can't have an operater with numbers before and after.
