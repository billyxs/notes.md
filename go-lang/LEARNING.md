# Learning Go

## Books, Courses, and Tutorials

+ [Go Bootcamp Book](http://www.golangbootcamp.com/book)
+ [The Little Go Book](http://openmymind.net/The-Little-Go-Book/)
+ [Learning go as a nodejs developer](https://nemethgergely.com/learning-go-as-a-nodejs-developer/)
+ [Building a JSON API in Go](https://pragmacoders.com/building-a-json-api-in-golang/)
+ [Greater Commons](https://greatercommons.com/cwg)
+ [Applied Go](https://appliedgo.com/p/workplace-automation-with-go)


## Structs

```go

import "fmt"

type person struct {
 name   string
 age    int
 height float64
 weight float64
}

func (p person) get_info() {
 fmt.Println("Name:- " + p.name)
 fmt.Println("Age:- ", p.age,"years ")
 fmt.Println("Height:- ", p.height,"cm")
 fmt.Println("Weight:- ", p.weight,"KG")
}

func main() {
 me := person{
   name: "Umar",
   age: 29,
   height: 1.6,
   weight: 68,
 }
 me.get_info()
}
```

