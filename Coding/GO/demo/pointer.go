package main

import "fmt"

func main() {
    // Assign integer 5 to variable x and store the value to a physical memory
    var x int = 5

    // Get x value
    fmt.Println("x:", x)
    // Get x address
    fmt.Println("x address:", &x)

    // Assign x address to int pointer variable pX and store the value to another physical memory
    var pX *int = &x

    // Get pX value
    fmt.Println("px value:", pX)
    // Get pX address
    fmt.Println("px address:", &pX)
    // Get the value which stored at pX value(x address) 
    fmt.Println("px value(x address)'s value:", *pX)
}
