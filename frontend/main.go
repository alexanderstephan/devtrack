package main

import (
	"fmt"
	"github.com/dtylman/gowd"
	"io/ioutil"
	//"time"
)

var body *gowd.Element

func main() {
	// Read in data source
	b, err := ioutil.ReadFile("data")
	if err != nil {
		fmt.Print(err)
	}

	str := string(b)
	fmt.Println(str)
	body, err := gowd.ParseElement("<h1>Welcome to devtrack</h1", nil)

	//start the ui loop
	gowd.Run(body)
}
