# Learn Hanzi with Sudoku!

I wrote this app in Python before I came to App Academy.  It scrapes a sudoku puzzle off of [Kjell Ericson's site](http://kjell.haxx.se/sudoku/) and returns it with 1-9 swapped out for any set of characters you input.

### Usage
    ./sudoku.py [difficulty (17-81)] [characters]

### Examples
    ./sudoku.py
returns a puzzle of random difficulty using the chinese characters for 1-9.

    ./sudoku.py 55 'ABCDEFGHI'
returns a puzzle with 55 squares already filled using letters A-I.

    ./sudoku.py random 'jklmnopqr'
returns a puzzle of random difficulty using letters j-r.
