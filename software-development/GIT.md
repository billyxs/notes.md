# Git

## Fixit

[Fixing commit messages](https://gist.github.com/billyxs/435bc1db0eac9eac722705a490192cb6)


## Get diff between branches
[https://stackoverflow.com/questions/13965391/how-do-i-see-the-commit-differences-between-branches-in-git]
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
## Migrate from one repo to another

https://medium.com/collaborne-engineering/how-to-migrate-a-private-repository-from-bitbucket-to-github-6cddedd5d73

# Videos

[200~### Git version control

+ [Get Together with Git
(workshop)](https://teamtreehouse.com/library/get-together-with-git)
+ [Everything I Wish I Knew When I Started Using
Github](https://youtu.be/KDUtjZHIx44)

