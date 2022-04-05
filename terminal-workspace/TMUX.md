# TMUX

## Articles
- [10 killer TMUX tips](https://www.sitepoint.com/10-killer-tmux-tips/)
- [A guide to customizing your TMUX confg](https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/)
- [Changing my TMUX command prefix to tic](https://zanshin.net/2014/12/27/changing-my-tmux-command-prefix-to-tic/)
- [A case against C-a in TMUX](https://coderwall.com/p/sojscq/a-case-against-c-a-in-tmux)
- [Persistant terminal sessions with TMUX](https://www.linode.com/docs/networking/ssh/persistent-terminal-sessions-with-tmux/)
- [Getting started with TMUX](https://news.ycombinator.com/item?id=9505647)
- [Learn X in Y - TMUX](https://learnxinyminutes.com/docs/tmux/)


## Setup help
- [Fixing Vim color in TMUX](https://stackoverflow.com/questions/10158508/lose-vim-colorscheme-in-tmux-mode)
Set `.tmux.conf`

```bash
set -g default-terminal "xterm"
```


- [Fixing meta command in iTerm](https://superuser.com/questions/649960/option-key-does-not-work-as-meta-in-tmux)
- [Fix/enable prefix binding: tmux set prefix C-b](https://www.kubuntuforums.net/forum/general/kde-neon/71017-tmux-prefix-ctrl-b-stopped-working)


## Plugins
- https://github.com/tmuxinator/tmuxinator
- https://github.com/benmills/vimux


## Cheat sheets
- https://tmuxcheatsheet.com/
- https://gist.github.com/MohamedAlaa/2961058
- https://gist.github.com/andreyvit/2921703


## .tmux.conf
- https://gist.github.com/spicycode/1229612
- https://github.com/jbnicolai/tmux/blob/master/.tmux.conf

Load tmux conf in bash. Add to .bashrc/.zshrc
```
tmux source-file ~/.tmux.conf
```

# Cheat Sheet

## Setup

- **Meta Key** For OXS and iTerm, go to Preferences -> Profile -> Keys and select Esx+ to use the alt/option key for meta commands
- **Prefix** Default is Control+b, but many in the community like to bind the prefix to Control+a. I've taken a liking to Control-o.

## Commands
```
tmux new -s base       - create a new session called "base"
tmux attach -t base    - attach to session named "base"
tmux attach            - attach to previous session
tmux clear-history     - clear history
tmux info              - list out all sessions, windows, panes and their pids, etc
tmux list-commands     - list all tmux commands and their arguments
tmux list-keys         - list all bound keys and the tmux command it runs
```

## Sessions
```bash
Prefix + s     - display list of sessions
Prefix + (     - switch to previous session
Prefix + )     - switch to next session
Prefix + d     - detach from session
```

## Windows
```bash
Prefix + w     - see window list
Prefix + c     - create a new window
Prefix + ,     - rename window
Prefix + p     - switch to previous window
Prefix + n     - switch to next window
Prefix + l     - switch to last active window
Prefix + 0-9   - switch to window using index number
Prefix + o     - switch to next pane
```

## Panes
```bash
Prefix + %     - split the active pane vertically
Prefix + "     - split the active pane horizontally
Prefix + ,     - rename window
Prefix + z     - toggle zoom on active pane
Prefix + space - rotate panes
```

## Navigation
```
Prefix + [     - enable Vim key bindings to move the cursor through the terminal output
```

## Exit and kill processes
```bash
Prefix + x     - force kill unresponsive task
Prefix + &     - force kill-all processes in an unresponsive window
exit           - close window
```
