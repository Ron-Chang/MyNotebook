# GO
---
### 1. The first GOLANG porgram
> Get a basic comprehension with `helloWorld.go`

*__demo/helloWorld.go__*
```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println("Hello, World!")
}
```
Testing
```bash
go run demo/helloWorld.go
```

First of all, we apart this file to the 3 different blocks.

- Part A
```go
package main
```

- Part B
```go
import (
    "fmt"
)
```

- Part C
```go
func main() {
    fmt.Println("Hello, World!")
}
```

At the __Part A__ we can see __package declaration__, all the `GO` files must start with package declaration, and `main` means this is the entry of the project.


The second part __Part B__, this is how we import dependency. You can
import single module without parentheses.

_Note: The non-used dependencies will make the file compile error._

```go
import "fmt"  // "fmt" stands for "format", handling standard input/output.
```

The last part, __Part C__ is the __main__ function where we write down the code.

---
## 2. assign.go
*__demo/assign.go__*
```go
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
```
There are few ways to declare and assign a value to the variable, but it's only two method for the constant.

##### variable
- A
```go
var foo int
foo = 10
```
- B
```go
var foo int = 10
```
- C
```go
foo := 10
```
- D
```go
var (
    foo = 1
    zoo = 2
    poo = 3
)
```

##### constant
- A
```go
const foo int = 10
```
- B
```go
const (
    number = 10
    amount = 20
    cost = 30
)
```
___
## 3. statement
##### - `if`, `else if`, `else`
*__demo/statementIf.go__*
```go
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
```
##### - `for`
*__demo/statementFor.go__*
```go
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
        fmt.Println(index, number)
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
```
##### - `switch`
*__demo/statementSwitch.go__*
```go
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
```
## 4. Data Type
##### - `Array`
>A data structure which contains data orderly, we can call data by index, The index must starts from 0.
*__demo/typeArray.go__*
```go
package main

import (
    "fmt"
    "strings"
)

var screen_width int=76

func divider(s string) {
    fmt.Println(strings.Repeat(s, screen_width))
}
func printTitle(s string) {
    format := fmt.Sprintf("%%%ds\n", screen_width/2 + len(s)/2)
    fmt.Printf(format, s)
}

func assignMethodA() [5]int {
    printTitle("assignMethodA")
    divider("-")
    fmt.Println("var result[5]int\nresult[2] = 100\nfmt.Printf(\"%v\\n\", result)")
    var result[5]int
    result[2] = 100
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func assignMethodB() [5]int {
    printTitle("assignMethodB")
    divider("-")
    fmt.Println("result := [5]int{}\nresult[2] = 100\nfmt.Printf(\"%v\\n\", result)")
    result := [5]int{}
    result[2] = 100
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func assignMethodC() [5]int {
    printTitle("assignMethodC")
    divider("-")
    fmt.Println("result := [5]{0, 0, 100, 0, 0}\nfmt.Printf(\"%v\\n\", result)")
    result := [5]int{0, 0, 100, 0, 0}
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func applyGetAverageMethodA() float64 {
    printTitle("applyGetAverageMethodA")
    divider("-")
    var sum float64
    var scoreList [5]float64
    scoreList[0] = 98
    scoreList[1] = 93
    scoreList[2] = 77
    scoreList[3] = 82
    scoreList[4] = 83
    for index := 0; index < 5; index++ {
        sum += scoreList[index]
    }
    result := sum / 5
    fmt.Println(
        "var sum float64",
        "\nvar scoreList [5]float64",
        "\nsocreList[0] = 99",
        "\nscoreList[1] = 93",
        "\nscoreList[2] = 77",
        "\nscoreList[3] = 82",
        "\nscoreList[4] = 83",
        "\nfor index := 0; index < 5; index++ {",
        "\n\tsum += scoreList[index]",
        "\n}",
        "\nresult := sum / 5",
        "\nfmt.Println(result)",
    )
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func applyGetAverageMethodB() float64 {
    printTitle("applyGetAverageMethodB")
    divider("-")
    scoreList := [5]float64{98, 93, 77, 82, 83}
    var sum float64
    for index := 0; index < len(scoreList); index++ {
        sum += scoreList[index]
    }
    result := sum / float64(len(scoreList))  //convert type to float64 instead of int
    fmt.Println(
        "var sum float64",
        "\nvar scoreList [5]float64{98, 93, 77, 82, 83}",
        "\nfor index := 0; index < len(scoreList); index++ {",
        "\n\tsum += scoreList[index]",
        "\n}",
        "\nresult := sum / len(scoreList)",
        "\nfmt.Println(result)",
    )
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func applyGetAverageMethodC() float64 {
    printTitle("applyGetAverageMethodC")
    divider("-")
    scoreList := [5]float64{98, 93, 77, 82, 83}
    var sum float64
    for _, score := range scoreList {
        sum += score
    }
    result := sum / float64(len(scoreList))  //convert type to float64 instead of int
    fmt.Println(
        "var sum float64",
        "\nvar scoreList [5]float64{98, 93, 77, 82, 83}",
        "\nfor _, score := range scoreList {",
        "\n\tsum += score",
        "\n}",
        "\nresult := sum / len(scoreList)",
        "\nfmt.Println(result)",
    )
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func showAssign() {
    divider("▽")
    printTitle("ASSIGN")
    divider("△")
    divider("=")
    assignMethodA()
    divider("=")
    assignMethodB()
    divider("=")
    assignMethodC()
    divider("=")
}

func showApply() {
    divider("▽")
    printTitle("APPLY")
    divider("△")
    divider("=")
    applyGetAverageMethodA()
    divider("=")
    applyGetAverageMethodB()
    divider("=")
    applyGetAverageMethodC()
    divider("=")
}

func main() {
    showAssign()
    showApply()
}
```

