# Git

## Fixit

[Fixing commit messages](https://gist.github.com/billyxs/435bc1db0eac9eac722705a490192cb6)


## Get diff between branches

View commits that are not on the master branch

```bash
git log master..develop --oneline --decorate
git log origin/master..origin/develop

# So pretty
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative master..branch-X
```

View file changes

```bash
git diff --stat  master..develop
git diff --stat origin/master..origin/develop
```

## Git config

To make git log nicer by default, I typically set these global preferences:

```bash
git config --global log.decorate true
git config --global log.abbrevCommit true
```

