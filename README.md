# Diminishing-Squares-Metaballs
An experimental way of rendering Metaballs

Set **show_working** to true in main.py for a demonstration for how it calculates the metaballs

## Method
This program divides the screen into squares and if those squares are determined to have the line going through them
(at least one but not all of the corners are inside the shape) the square is subdivided and the process repeates down
to a minimum size where the square is filled in.

### Pros
- Speed

### Cons
- If a square has a section of line going through it but all of the corners are out or all of the corners are in the shape,
the square will be marked as not having a line through it and be missed
- If the line goes through the center of four squares it can miss two 
