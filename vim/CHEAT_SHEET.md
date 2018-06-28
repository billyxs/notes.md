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

w  " move to start of next word
W  " move to start of next word, ignore special characters
e  " move to end of next word
E  " move to end of next word, ignore special characters

(  " move to previous sentence
)  " move to next sentence
{  " move to previous paragraph
}  " move to next paragraph

%  " move to opposite brace or bracket the cursor is under
]] " move to next sections { in the first column
][ " move to next sections } in the first column
[[ " move to previous section { in the first column
[] " move to previous sections } in the first column

[{ " move to beginning of code block or previous unmatched {
]} " move to end of code block or next unmatchd }
[( " move to beginning of code block or previous unmatched (
]) " move to end of code block or next unmatchd )

]m " move to next start of method for java structured languages
[M " move to next end of method for java structured languages
[m " move to previous start of method for java structured languages
]M " move to previous end of method for java structured languages

fx " move forward the to next occurence of 'x'
Fx " move backward the to previous occurence of 'x'
tx " move forward just before the next occurence of 'x'
Tx " move backward just before the previous occurence of 'x'

0  " move to the beginning of the line
$  " move to the end of the line
^  " move to the first non-whitespace character on the line
_  " move to the first non-whitespace character on the line

^e " scroll screen up one line. cursor line doesn't change
^d " move down half the page and scroll
^u " move up half the page and scroll

H  " move to the top of the window, no scroll
L  " move to the bottom of the window, no scroll
M  " move to the middle of the window, no scroll
zz " scroll the file to so the current cursor postion is the middle of the window

G  " move to the bottom of the file
gg " move to the top of the file
gi " change to insert mode and move to location you left insert mode
```

## Writing

### ASCII, Digraphs, and Special Characters

```bash
ga             " print ascii value of char under cursor as decimal, hexidecimal, and octal 
:as or :ascii  " print ascii value of char under cursor as decimal, hexidecimal, and octal 

" Digraphs
:dig or :digraphs  " list of defined digraphs

" Insert mode
^v   " prefix before inserting ascii keycode. ctrl-v cH renders ♡

^k   " prefix before inserting a digraph keycode. ctrl-k cH renders ♡
     " any two numbers will produce a fraction. ctrl-k 12 renders ½
```

## Editing

```bash
r " replace current character
R " replace mode
s " substitute char - remove character and change to insert mode
S " substitute line - remove line and change to insert mode
o " add new line below and change to insert mode
O " add new line above and change to insert mode
```

## Copy and Paste

```bash
y    " copy
yiw  " copy inside word
yiW  " copy inside word including special characters
yi(  " copy paragraph
yit  " copy inside of tags - ie <span>word</span>
yy   " copy line
Y    " copy line

p  " paste text after cusor
P  " paste text before cusor
gp " paste after cursor and put cursor at end of new text
gP " paste after cursor and put cursor at end of new text
```

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
`<   " move cursor to previous selection's start position
`>   " move cursor to previous selection's end position
```


## Autocomplete

**Insert mode**
```bash
^p    " autocomplete word in session
^n    " autocomplete word in session
^x^n  " autocomplete many words. repeat commands as needed.
^x^l  " autocomplete line or file path if found in your session

```

## Macros

```bash
qa   " record a macro to register "a". hit "q" to quit recording
@a   " run macro from register a.
@@   " repeat the last macro.
qaq  " clear macro "a".

:reg    " see register list of macros
:reg ah " see registers "a" and "h" 
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

" Casing
\c    " ignore case with search
\C    " match case with search

" Magic mode
\v    " enable all special characters for regex
\V    " disable special characters and search them literal

:bd *.js then hit <C-a> " autocomplete *.js to match any buffers in the session

```

```bash
:%s/hello/goodbye/gc  " Replace in file all 'hello' with 'goodbye' and require confirm
:g/hello/m $          " Get all lines that have hello and move them to the bottom of the file
:v/^import/normal dd  " Delete all lines that don't start with import
:g/^import/j          " Join all lines that start with import
:g/^import/t 0        " Copy all lines that start with import to line 0, or top of file
:g/^import/y A        " Copy all lines that start with import into register A. This appends to the register.
```

## Jumps and History

```bash
:jumps   " list of jumps
:changes " list of jumps where the file was changed

^o       " Go to the previous cursor position in history
^i       " Go to the next cursor position in history
`<       " Go to start of previous visual selection
`>       " Go to end of previous visual selection

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
:%bd  " delete all buffers
```

## Windows

```bash
<Ctrl-w>h   " move focus to left window
<Ctrl-w>j   " move focus to bottom window
<Ctrl-w>k   " move focus to top window
<Ctrl-w>l   " move focus to right window
<Ctrl-w>=   " resize all windows to equal size

<Ctrl-w>H   " move current window right
<Ctrl-w>J   " move current window below
<Ctrl-w>K   " move current window up
<Ctrl-w>L   " move current window left

:tabe filename  " Edit file in a new tab

```

## Netrw - Directory Management

```bash
:E       " open directory explorer
:Vex     " open directory in vertical split
:Sex     " open directory in horizontal split
:Tex     " open directory in tab
:Rex     " return to and from directory 
:split   " horizontally split window
:vsplit  " vertically split window

r  " refresh and reverse sort directory list 
R  " move file
D  " delete file

" Copy file, run these commands in order
mt " mark target folder for copying to
mf " mark file to copy
mc " execute copy of file to target
```

## Other

```
:%TOhtml   " create the current file contents as HTML document

" read
:r! ls     " pull ls output into the vim session
:r! date   " pull date into the vim session

" suspend vim and use terminal
<Ctrl-z>   " suspend vim session
fg         " go back to to suspended vim session

g <Ctrl-g> " show file info based on the cursor position
ga         " print ascii value of char under cursor in decimal, hexidecimal, octal, and digraph if applicable
gx         " open url under the cursor in a browser

:%!python -m json.tool " format JSON

```
