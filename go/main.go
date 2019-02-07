package main

import (
	"fmt"
	"os"
        "bytes"
	"time"
        "net/http"
)

var (
	sink string
)

func main() {

	sink = os.Getenv("SINK")

	for true {
                var msg = []byte(`{"Hello":"World"}`)

	        req, err := http.NewRequest("POST", sink, bytes.NewBuffer(msg))
	        req.Header.Set("Content-Type", "application/json")

	        client := &http.Client{}
	        resp, err := client.Do(req)
	        if err != nil {
		    panic(err)
	        }
	        defer resp.Body.Close()

		fmt.Println("Sending Event")
		time.Sleep(30 * time.Second)
	}
}
