package main

import (
	"fmt"
	gc "github.com/rthornton128/goncurses"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"time"
)

func main() {
	stdscr, err := gc.Init()

	if err != nil {
		log.Fatal("init:", err)
	}

	defer gc.End()

	gc.CBreak(true)
	stdscr.Keypad(true)

	// Read in data source
	b, err := ioutil.ReadFile("data")
	if err != nil {
		fmt.Print(err)
	}

	str := string(b)

	parsedInput := strings.Fields(str)

	msg := "Enter your name:"

	row, col := stdscr.MaxYX()
	row, col = (row/2)-1, (col-len(msg))/2
	stdscr.MovePrint(row, col, msg)

	str, err = stdscr.GetString(20)

	if err != nil {
		stdscr.MovePrint(row+1, col, "GetString Error:", err)
	} else {
		stdscr.MovePrint(row+1, col, "Entry was succesful")
	}

	//time.Sleep(1 * time.Second)

	stdscr.Erase()

	for i := 0; i < len(parsedInput); i++ {
		numTime, err := strconv.ParseInt(parsedInput[i], 10, 64)
		if err != nil {
			panic(err)
		}
		uniTime, err := time.Unix(numTime, 0)
		if err != nil {
			panic(err)
		}

		stdscr.MovePrint(row/2+i, col/2, uniTime.Format("8 41 PM"))
	}

	stdscr.Refresh()
	stdscr.GetChar()
}
