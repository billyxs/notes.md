# Vim Cheat Sheet

**Legend**
`^` Control key


## Motions

```bash
" Normal mode

h  " move left
j  " move down
k  " move up
l  " move right

w  " move to next word
W  " move to next word, ignore special characters
e  "
E  "
f  "
F  "
t  "
T  "
^e "
^d "
^u "
H  "
L  "
M  "
```

## Format

```bash
={motion}  " format file with proper indenting
G=gg       " format entire file from bottom to top
```


## Autocomplete

```bash
^p    " autocomplete word in session
^x^l  " autocomplete file path if found in your session
```

## Ex commands

```bash
m     " move
t     " copy
j     " join
```

```bash
:g    " global match
:v    " not matching
:!g   " not matching, like :v
:%s   " search and replace
```

```bash
:%s/hello/goodbye/gc  " Replace in file all 'hello' with 'goodbye' and require confirm
:g/hello/m $          " Get all lines that have hello and move them to the bottom of the file
:v/^import/normal dd  " Delete all lines that don't start with import
:g/^import/j          " Join all lines that start with import
:g/^import/t 0        " Copy all lines that start with import to line 0, or top of file
```
