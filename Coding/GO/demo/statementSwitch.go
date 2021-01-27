package main

import "fmt"

func main() {
    var foo string

    fmt.Println("Enter a number: ")
    fmt.Scanf("%s", &foo)
    switch foo {
        case "0": fmt.Println("[-  off -]")
        case "1": fmt.Println("[-  on  -]")
        default: fmt.Println("Unknown Input")
    }
}
