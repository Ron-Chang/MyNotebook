package main

import (
    "fmt"
    "strings"
    "reflect"
)

var screen_width int=76

func divider(s string) {
    fmt.Println(strings.Repeat(s, screen_width))
}
func printTitle(s string) {
    format := fmt.Sprintf("%%%ds\n", screen_width/2 + len(s)/2)
    fmt.Printf(format, s)
}

func assignMethodA() []int {
    printTitle("assignMethodA")
    divider("-")
    fmt.Println("var result[]int\nresult = append(result, 100)\nfmt.Printf(\"%v\\n\", result)")
    var result []int
    result = append(result, 100)
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func assignMethodB() []int {
    printTitle("assignMethodB")
    divider("-")
    fmt.Println("result := []int{}\nresult = append(result, 100)\nfmt.Printf(\"%v\\n\", result)")
    result := []int{}
    result = append(result, 100)
    divider("-")
    fmt.Printf(fmt.Sprintf("%%%ds\n", screen_width), fmt.Sprintf("output: %v", result))
    return result
}

func assignMethodC() []int {
    // make(slice, length, capacity)
    // be aware of append it may let the slice size over its capacity
    printTitle("assignMethodC")
    divider("-")
    fmt.Println("result := make([]int, 1)\nresult[0] = 100\nfmt.Printf(\"%v\\n\", result)")
    result := make([]int, 1)
    result[0] = 100
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

func applyCompare() {
    //slice[low:high]
    //including index low but not index high
    divider("▽")
    printTitle("APPLY")
    divider("△")
    divider("=")
    sliceA := []int{1, 2, 3,  4, 5}
    fmt.Println("Get sliceA whitout the first element")
    fmt.Printf("sliceA     -> %v\n", sliceA)
    fmt.Printf("sliceA[1:] -> %v\n", sliceA[1:])
    fmt.Printf("sliceA[1:2] -> %v\n", sliceA[1:2])
    fmt.Printf("sliceA == sliceA[:] is %t\n", reflect.DeepEqual(sliceA, sliceA[:]))
    divider("=")
}


func main() {
    showAssign()
    applyCompare()
}
