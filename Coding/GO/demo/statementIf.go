package main

import (
    "fmt"
)

func main() {
    var foo string

    fmt.Println("Enter a number: ")
    fmt.Scanf("%s", &foo)
    if foo == "1" {
        fmt.Println("[-  ON  -]")
    } else if foo == "0" {
        fmt.Println("[-  OFF -]")
    } else {
        fmt.Println("INVALID INPUT:", foo)
    }
}
