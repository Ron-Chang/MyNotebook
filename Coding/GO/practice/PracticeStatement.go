package main

import (
    "fmt"
)

func divisibleBy(n int, start int, end int) {
    index := 0
    for num := start; num <= end; num++ {
        if num % n == 0 {
            index += 1
            fmt.Printf("[%d] %d\n", index, num)
        }
    }
}

func fizzBuzz() {
    for num := 1; num <= 100; num++ {
        if num % 3 == 0 && num % 5 == 0 {
            fmt.Println("FizzBuzz", num)
        }else if num % 3 == 0{
            fmt.Println("Fizz", num)
        }else if num % 5 == 0{
            fmt.Println("Buzz", num)
        }else{
        }
    }
}

func main() {
    divisibleBy(3, 1, 100)
    fizzBuzz()
}
