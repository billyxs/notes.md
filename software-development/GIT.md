# Git

- [Git extras - commands](https://github.com/tj/git-extras/blob/master/Commands.md)
- [A monorepo, GitHub flow and automation](https://hackernoon.com/a-monorepo-github-flow-and-automation-ftw-c41a2d9c48bb)

## Commits and collaboration

- [Fixing commit messages](https://gist.github.com/billyxs/435bc1db0eac9eac722705a490192cb6)
- [Conventional commits](https://conventionalcommits.org/)
  - Conventions to automate semver and change logs
- [How to write a git commit message](https://chris.beams.io/posts/git-commit/)
- [4 rules for effective collaboration](https://github.com/salemove/github-review-helper/blob/master/doc/rules.md#four-rules-for-effective-collaboration)
- [On commit messages](http://who-t.blogspot.com.ee/2009/12/on-commit-messages.html)


## Git Diff

### Get diff between branches
[How do I see the commit differences betweenk](https://stackoverflow.com/questions/13965391/how-do-i-see-the-commit-differences-between-branches-in-git)
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

### Git diff files between commits
[Find all files modified between commits in Git](https://coderwall.com/p/lz0uva/find-all-files-modified-between-commits-in-git)

File diff between the last two commits on current branch
```bash
git diff --name-only HEAD HEAD~1
```

File diff between two SHAs
```bash
git diff --name-only <SHA1> <SHA2> 
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

