# Vim

[My vimrc](https://github.com/billyxs/.vim/blob/master/vimrc)

[My vim cheat sheet as found through my journey](https://github.com/billyxs/notes.md/blob/master/vim/CHEAT_SHEET.md)


## Articles

+ [Vim Text Objects: The Definitive Guide](https://blog.carbonfive.com/2011/10/17/vim-text-objects-the-definitive-guide/)
+ [Good reasources for learning Vim](https://www.quora.com/What-are-some-good-resources-for-learning-Vim)
+ [Vim graphical cheat sheet](http://www.viemu.com/vi-vim-cheat-sheet.gif)
+ [Use Vim](https://antjanus.com/blog/thoughts-and-opinions/use-vim/)
+ [Using argdo to change multiple files](http://vimcasts.org/episodes/using-argdo-to-change-multiple-files/)
+ [Advanced Vim Tutorial](http://tebrik.kampanya.org.tr/Linux/Books/advanced_vim_tutorial.pdf)
+ [Vim for Frontend Developers](https://speakerdeck.com/csswizardry/vim-for-front-end-developers)
+ [5 Plugins I can't live without](https://hackernoon.com/5-vim-plugins-i-cant-live-without-for-javascript-development-f7e98f98e8d5)
+ [Simplifying regular expressions using magic and no-magic](http://vim.wikia.com/wiki/Simplifying_regular_expressions_using_magic_and_no-magic)
+ [Setting up Vim for React development](https://drivy.engineering/setting-up-vim-for-react/)
+ [Vim Splits - Move Faster and More Naturally](https://robots.thoughtbot.com/vim-splits-move-faster-and-more-naturally)
+ [Vim search, find and replace in one or multiple files with examples](http://web-techno.net/vim-search/)


## Talks

+ [Learning Vim in a week](https://www.youtube.com/watch?v=_NUO4JEtkDw)
+ [Write code faster: expert-level vim](http://youtu.be/SkdrYWhh-8s)
+ [Impressive Ruby Productivity with Vim and Tmux](http://youtu.be/9jzWDr24UHQ)
+ [Harnessing the Power of Vim (workshop)](https://teamtreehouse.com/library/harnessing-the-power-of-vim)
+ [Your First Vim Plugin](https://youtu.be/lwD8G1P52Sk)
+ [Vim + Tmux](https://youtu.be/5r6yzFEXajQ)

# Tips and Tricks

+ [Configuring Vim Right](http://items.sjbach.com/319/configuring-vim-right)


## Key Mappings

+ [Vi Master By Learning These 30 Key Bindings](https://www.howtogeek.com/115051/become-a-vi-master-by-learning-these-30-key-bindings/)
+ [Key mapping best practices](https://vi.stackexchange.com/questions/6916/key-mapping-best-practices)
+ [8 Great Vim Mappings](https://hashrocket.com/blog/posts/8-great-vim-mappings)
+ [What is your most productive shortcut](https://stackoverflow.com/questions/1218390/what-is-your-most-productive-shortcut-with-vim)
+ [What Are The Dark Corners of Vim Your Mom Never Told You About](https://stackoverflow.com/questions/726894/what-are-the-dark-corners-of-vim-your-mom-never-told-you-about)


## Startup profiling

[Vim screencast #44: Profiling and optimization](https://www.youtube.com/watch?v=wQ9uB8I0cCg)

```bash
" verbose output
vim --startuptime startup.log +qall && vim startup.log && rm startup.log

" get the final result
vim -c\ q --startuptime /tmp/vim.log && tail -n1 $_
```

## Plugins

**Directory**

+ https://github.com/justinmk/vim-dirvish
+ https://github.com/jeetsukumaran/vim-filebeagle
+ https://github.com/tpope/vim-vinegar


**Git**

+ https://github.com/airblade/vim-gitgutter
+ https://github.com/tpope/vim-fugitive


**Lint**

+ https://github.com/w0rp/ale


**Syntax**

+ https://github.com/pangloss/vim-javascript
+ https://github.com/mxw/vim-jsx
+ https://github.com/jason0x43/vim-js-syntax
+ https://github.com/jelera/vim-javascript-syntax
+ https://github.com/othree/yajs.vim
+ https://github.com/tpope/vim-markdown
+ https://github.com/styled-components/vim-styled-components


**Search**
+ https://github.com/junegunn/fzf.vim


**Themes**

+ https://github.com/Alvarocz/vim-fresh
+ https://github.com/ajh17/Spacegray.vim
+ https://github.com/chriskempson/base16-vim
+ https://github.com/flazz/vim-colorschemes
+ https://github.com/larsbs/vimterial_dark
+ https://github.com/lifepillar/vim-solarized8
+ https://github.com/martinlindhe/base16-iterm2
+ https://github.com/mhartington/oceanic-next
+ https://github.com/nightsense/seabird
+ https://github.com/rainglow/vim
+ https://github.com/rakr/vim-one
+ https://github.com/tomasiser/vim-code-dark
+ https://github.com/widatama/vim-phoenix
+ https://github.com/wimstefan/vim-artesanal


**Tools/Performance**

+ https://github.com/skywind3000/asyncrun.vim
+ https://github.com/wakatime/vim-wakatime
+ https://github.com/JamshedVesuna/vim-markdown-preview
+ https://github.com/tpope/vim-dispatch
+ https://github.com/machakann/vim-highlightedyank


**Profiling**

+ https://github.com/tweekmonster/startuptime.vim


**Windows**

+ https://github.com/wesQ3/vim-windowswap
