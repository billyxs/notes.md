# Bash


## awk

+ [Write AWK Commands and Scripts](https://www.lifewire.com/write-awk-commands-and-scripts-2200573)


## xargs

+ [xargs: How To Control and Use Command Line Arguments](https://www.cyberciti.biz/faq/linux-unix-bsd-xargs-construct-argument-lists-utility/)


## sed

+ [A Quick Guide to Using Sed Commands](https://www.lifewire.com/example-uses-of-sed-2201058)


## nl

https://www.computerhope.com/unix/nl.htm

Output contents of file with line numbers

```bash
nl filename
```


## ssh

[SSH config](http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/)

**Remove hostname**

```bash
ssh-keygen -R hostname
```



## Tools

+ dtrace


## Snippets

Use ripgrep to search and replace
```bash
riplace() {
  if [ ${#1} -eq 0 ]; then
    read "a?Search: "
  else
    a=${#1}
  fi

  if [ ${#2} -eq 0 ]; then
    read "b?Replace:"
  else
    b=${#2}
  fi

  rg -l "$a" | xargs sed -i "" "s|$a|$b|g"
}

riplace
# or
riplace searchTerm
# or
riplace searchTerm replaceTerm
```

Do the same thing but with prompts
```bash
# bash uses `read -p` while zsh only uses `read`
# This is a zsh example
riplace() {
  read "a?Search: "
  read "b?Replace:"
  rg -l "$a" | xargs sed -i "" "s|$a|$b|g"
}

$ riplace
$ Search: Hello
$ Replace: Goodbye
```

## rm
- [Unraveling `rm`: What happens when you run it](https://blog.safia.rocks/post/173241985600/unraveling-rm-what-happens-when-you-run-it)
