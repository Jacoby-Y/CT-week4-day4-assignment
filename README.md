## Coding Temple Week 4 Day 4 Assignment

###### CT-week4-day4-assignment


#### Structure
- Put "View reading list" in function
- Put "Remove book from reading list" in function
- Import `first_match()` from `iter_help` to get the first item that matches a criteria for more readable code
- Import `mprint` from `pretty` for better printing of multi-line strings
- Replaced all instances of `list(filter(...` with `first_match()`

#### Efficiency
- `first_match()` function brings book looping best efficiency down to O(1)
- In `browse_books()` I reduced multiple loops of books to one with the variable `sel_book` 
- Utilized `first_match()` to only loop through books once in `remove_book()`

#### Functionality
- Double check password in registration
- Save and load `reading_list` from a file
- User can delete their account