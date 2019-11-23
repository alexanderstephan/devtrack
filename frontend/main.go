package mainsldalsdjasldj

import (
	"bufio"
	"fmt"
	gc "github.com/rthornton128/goncurses"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
)

func readByLine() (myString []string) {
	file, err := os.Open(data)
	defer file.Close()

	if err != nil {
		return err
	}

	reader := bufio.NewReader(file)
	lineCounter := 0

	var line string

	for {
		line, err = reader.ReadString('\n')
		lineCounter++
		if err != nil {
			break
		}
	}

	var myStrings []string

	for i := 0; i < lineCounter; i++ {
		myStrings[i] = reader.ReadString('\n')
		if err != nil {
			break
		}
	}

	if err != io.EOF {
		fmt.Printf("Failed")
	}

	return myStrings
}

func main() {
	stdscr, err := gc.Init()

	if err != nil {
		log.Fatal("init:", err)
	}

	defer gc.End()

	gc.CBreak(true)
	stdscr.Keypad(true)

	var output []string = readByLine()

	output = readByLine()

	var singleLines []string

	for i := 0; i < len(output); i++ {
		singleLines[i] = strings.Fields(output[i])
	}

	msg := "Enter your name:"

	row, col := stdscr.MaxYX()
	row, col = (row/2)-1, (col-len(msg))/2

	stdscr.MovePrint(row, col, msg)

	str, err := stdscr.GetString(20)

	if err != nil {
		stdscr.MovePrint(row+1, col, "GetString Error:", err)
	} else {
		stdscr.MovePrint(row+1, col, "Entry was successful")
	}

	stdscr.Erase()

	for i := 0; i < len(parsedInput); i++ {
		numTime, err := strconv.ParseInt(parsedInput[i], 10, 64)
		if err != nil {
			panic(err)
		}
		uniTime := time.Unix(numTime, 0)

		stdscr.MovePrint(row/2+2*i, col/2, uniTime.Format("Mon Jan _2 15:04:05 2006"))

	}

	stdscr.Refresh()
	stdscr.GetChar()
}
