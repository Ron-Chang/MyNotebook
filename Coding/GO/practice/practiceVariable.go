package main

import (
    "fmt"
)

func fahrenheitToCelsius(fahrenheit float64) float64 {
    //華氏轉為攝氏 C = (F - 32) * 5/9
    celsius := (fahrenheit - 32) * 5/9
    fmt.Println(fahrenheit, "˚F", "=", celsius, "˚C ")
    return celsius
}

func feetToMeter(ft float64) float64 {
    //另外寫個程式將英尺 (ft) 轉換為公尺 (m) (1 ft = 0.3048 m)
    if ft == 0.0 {
        fmt.Println("Input feet convert to meter:")
        fmt.Scanf("%f", &ft)
    }
    memter := ft * 0.3048
    fmt.Println(ft, "ft.", "=", memter,"m")
    return memter
}


func main() {
    fahrenheitToCelsius(180)
    feetToMeter(20)
}
