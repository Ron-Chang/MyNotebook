package main

import "fmt"

func main() {
    // declare foo as a list and contains 5 integer which which has been set a default value 0
    var foo [5]int
    // assign 99 to foo 3rd element which index is 2 (The index counts from 0).
    foo[2] = 99
    fmt.Println(foo)

    // easier way to declare and assign the value
    zoo := [5]int{10, 20, 30, 40, 50}
    fmt.Println(zoo)

    // easier way to declare and assign the value without mention size
    qoo := []int{10, 20, 30, 40, 50, 60, 70}
    fmt.Println(qoo)

    qoo = append(qoo, 100)
    fmt.Println(qoo)
}
