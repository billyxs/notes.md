# TMUX

## Articles
- https://www.sitepoint.com/10-killer-tmux-tips/
- https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/
- https://zanshin.net/2014/12/27/changing-my-tmux-command-prefix-to-tic/
- https://coderwall.com/p/sojscq/a-case-against-c-a-in-tmux
- https://www.linode.com/docs/networking/ssh/persistent-terminal-sessions-with-tmux/


## Fixing Vim colorscheme
- https://stackoverflow.com/questions/10158508/lose-vim-colorscheme-in-tmux-mode 

Set `.tmux.conf
```bash
set -g default-terminal "xterm"
```


## Plugins
- https://github.com/tmuxinator/tmuxinator


## Cheat sheets
- https://gist.github.com/MohamedAlaa/2961058


## Confs
- https://gist.github.com/spicycode/1229612


## Cheat Sheet

**Prefix** default is Control+b, but many in the community like to bind the prefix to Control+a. I've taken a liking to Control-o. 

### Commands
```
tmux new -s base       - create a new session called "base"
tmux attach -t base    - attach to session named "base" 
tmux attach            - attach to previous session
```

### Sessions 
```bash
Prefix + s     - display list of sessions
Prefix + (     - switch to previous session 
Prefix + )     - switch to next session 
Prefix + d     - detach from session 
```

### Windows
```bash
Prefix + w     - see window list 
Prefix + c     - create a new window
Prefix + ,     - rename window
Prefix + p     - switch to previous window 
Prefix + n     - switch to next window 
Prefix + 0-9   - switch to window using index number
Prefix + o     - switch to next pane 
```

### Panes
```bash
Prefix + %     - split the active pane vertically 
Prefix + "     - split the active pane horizontally 
Prefix + ,     - rename window
Prefix + z     - toggle zoom on an active pane 
```

### Navigation
```
Prefix + [     - enable Vim key bindings to move the cursor through the terminal output 
```

### Exit and kill processes 
```bash
Prefix + x     - force kill unresponsive task 
Prefix + &     - force kill-all processes in an unresponsive window
exit           - close window
```
