# Bash Cheatsheet

## Try/Catch

https://stackoverflow.com/a/22010339

```bash
{
  # run command
} || {
  # if first command failed, run this one
}

```

## Error handling

```bash
set -e # throw errors
set +e # ignore errors
```
