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
G  "
gg "
```

## Jumps

```bash
^o
^i
`<   " Go to start of previous visual selection
`>   " Go to end of previous visual selection
```
## Editing



## Format Text

```bash
={motion}  " format file with proper indenting
G=gg       " format entire file from bottom to top
```

**Change case**
```bash
~     " toggle character from upper to lowercase, or lower to uppercase
guu   " change line to lowercase
gUU   " change line to uppercase
guiw  " change word to lowercase
gUiw  " change word to uppercase
guiw~ " capitalize word
```

## Visual Selection

```bash
gv   " select previous visual selection
o    " toggle cursor to start and end of visual selection
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
:g/^import/y A        " Copy all lines that start with import into register A. This appends to the register.
```

## Jumps

```bash
:jumps   " list of jumps
g;       " move cursor to previous edit in history
g,       " move cursor to next edit in history
gi       " move cursor to last and change to insert mode

```

## Buffers

```bash
:ls  " list buffers
:b#  " go to last buffer
:b1  " go to buffer 1 in buffer list
:bp  " go to previous buffer
:bn  " go to next buffer
:bd  " delete buffer
```

## Windows

```bash
<Ctrl-w>h   " move focus to left window
<Ctrl-w>j   " move focus to bottom window
<Ctrl-w>k   " move focus to top window
<Ctrl-w>l   " move focus to right window
<Ctrl-w>=   " resize all windows to equal size

:tabe filename  " Edit file in a new tab

```

## Netrw - Directory Management

```bash
:E       " open directory explorer
:split   " open directory with horizontal split
:vsplit  " open directory with vertical split
```

## Other

```
:%TOhtml  "

:r! ls    " pull ls contents into the vim session
:r! date  " pull date contents into the vim session

<Ctrl-z>  " suspend vim session
fg        " go back to to suspended vim session
```
