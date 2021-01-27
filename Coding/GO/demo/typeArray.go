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
