package main

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
