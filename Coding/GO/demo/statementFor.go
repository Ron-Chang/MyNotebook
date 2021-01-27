package main

import (
    "fmt"
    "time"
    "strings"
)

func divider(s string, count int) {
    fmt.Println(strings.Repeat(s, count))
}

func methodA() {
    // "Python"
    // for i in range(1, 11, 1):
    //    print(i)

    fmt.Println(" - Method A")
    divider("-", 35)
    fmt.Println("for i := 1; i < 11; i++ {\n\tfmt.Println(i)\n}")
    divider("-", 35)
    for i := 1; i < 11; i++ {
        fmt.Println(i)
    }
}

func methodB() {
    // "Python"
    // i = 1
    // while i < 11:
    //     print(i)
    //     i += 1

    fmt.Println(" - Method B")
    divider("-", 35)
    fmt.Println("i := 1\nfor i < 11 {\n\tfmt.Println(i)\n\ti ++\n}")
    divider("-", 35)
    i := 1
    for i < 11 {
        fmt.Println(i)
        i ++
    }
}

func methodC() {
    // "Python"
    // words = ['Hello', 'World']
    // for index, word in enumerate(words):
    //     print(index, word)

    fmt.Println(" - Method C")
    divider("-", 35)
    fmt.Println("words := []string{\"Hello\", \"World\"}\nfor index, word range := words {\n\tfmt.Println(index, word)\n}")
    divider("-", 35)
    words := []string{"Hello", "World"}
    for index, word := range words {
        fmt.Println(index, word)
    }
}

func methodD() {
    // "Python"
    // numbers = [2, 4, 8, 16]
    // for index, number in enumerate(numbers):
    //     print(index, number)

    fmt.Println(" - Method D")
    divider("-", 35)
    fmt.Println("numbers := []string{2, 4, 8, 16}\nfor index, number range := numbers {\n\tfmt.Println(index, number)\n}")
    divider("-", 35)
    numbers := []int{2, 4, 8, 16}
    for index, number := range numbers {

        fmt.Printf("INDEX[%d] = %d\n", index, number)
    }
}

func methodE() {
    fmt.Println(" - Method E")

    // "Python"
    // while True:
    //    time.sleep(2)
    //    print('<ctrl + c> to stop function')

    divider("-", 35)
    fmt.Println("for {\n\tfmt.Println(\"<ctrl + c> to stop function\")\n\ttime.Sleep(time.Duration(2) * time.Second)\n}")
    divider("-", 35)
    for {
        fmt.Println("<ctrl + c> to stop function")
        time.Sleep(time.Duration(2) * time.Second)
    }
}

func main() {
    divider("=", 35)
    methodA()
    divider("=", 35)
    methodB()
    divider("=", 35)
    methodC()
    divider("=", 35)
    methodD()
    divider("=", 35)
    methodE()
    divider("=", 35)
}
