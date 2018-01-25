# Git

[Fixing commit messages](https://gist.github.com/billyxs/435bc1db0eac9eac722705a490192cb6)

**Get commit diff between branches**
```bash
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s
%Cgreen(%cr)%Creset' --abbrev-commit --date=relative master..branch-X
```
