package main

import "fmt"

func main() {

    /*
        variable: var
        constant: const
    */

    // The standard way to declare what type variable is, then assign a value to it.
    var x int
    x = 1

    // The standard way to declare what type it is and assign a value at the same time.
    var y int = 2

    // To assign a value and automatically to declare what type it is.
    z := 3

    //constant a cannot be changed
    const a int = 5

    // assign (1 + 2 + 3) * 5 to result
    var result int = (x + y + z) * a

    var line string = "(x + y + z) * a ="

    fmt.Println("x:", x)
    fmt.Println("y:", y)
    fmt.Println("z:", z)
    fmt.Println("a:", a)
    fmt.Println(line, result)

    // multi-assignments
    var (
        foo = 100
        zoo = 2
    )
    const (
        price = "Price:"
        amount = "Amount:"
        total = "Total:"
    )
    fmt.Println(price, foo)
    fmt.Println(amount, zoo)
    fmt.Println(total, foo * zoo)
}
