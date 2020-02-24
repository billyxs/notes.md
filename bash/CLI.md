# CLI

## Commands & shorcuts

```bash
" Handling processes
ctrl-c " kill a process
ctrl-z " suspend the current process and run it in the background
fg     " reattach to the background process created from ctrl-z
ctrl-d " close the bash shell
ctrl-l " clear the screen. similar to clear
ctrl-s " stop all output to the screen. does not stop the process
ctrl-q " resume output to the screen after a ctrl-s command
```

```bash
" Movement 
ctrl-a " go to the beginning of line
ctrl-e " go to the end of line
ctrl-b " go left one character 
alt-b  " go left one word 
ctrl-f " go right one character 
alt-f  " go right one word 
ctrl-xx" moves between the beginning of a line and the current position of the cursor

" Editing
ctrl-d " delete the character under the cursor
alt-d  " delete all the characters after the cursor on the line
ctrl-h " delete the character before the cursor

ctrl-t  " swap current word with previous word
alt-t   " swap the last two characters before the cursor with each other. 
ctrl-_  " undo your last key press. can be executed multiple times

ctrl-w  " cut the word before the cursor, adding it to the clipboard
ctrl-k  " cut all text after the cursor to end of line, adding it to the clipboard
ctrl-u  " cut all text before the cursor to the beginning of line, adding it to the clipboard
ctrl-y  " pasting the contents of the last cut

alt-u   " capitalize every character from the cursor to the end of the current word
alt-l   " uncapitalize every character from the cursor to the end of the current word
alt-c   " capitalize the word under the cursor 

ctrl-x-e " Enter default editor($EDITOR) to write out script
alt-.    " Paste last argument

" Fun stuff
!!   " Rerun the last command. Can also be used with a command, eg: sudo !!
reset " unbork your terminal
```

## Tools

### less
```bash
less +F <filename>
" ctrl-c to detach from the end to scroll contents
" shift-f to reatach to the end

```
