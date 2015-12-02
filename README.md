# sudoku.jl

An HTTP service that solves sudoku puzzles.

## Setup Instructions


### Dependencies

This program has dependencies on three Julia packages. JuMP is used to model the Sudoku board as a linear programming problem. GLPK is used to solve that linear programming problem. HttpServer is used to provide the solver as a web service.

```bash
julia -e 'Pkg.add("GLPKMathProgInterface")'
julia -e 'Pkg.add("JuMP")'
julia -e 'Pkg.add("HttpServer")'
```

### sudoku.jl

```bash
git clone http://github.com/aj-michael/sudoku.jl
```

## Running the service

```bash
julia server.jl
```

## Requests and responses

The service expects GET requests of the form `http://localhost:8001/solve/<puzzle>` where `<puzzle>` is an 81 character string of the digits of your initial grid read row by row starting at the top. Replace all unknown digits with zeros. The response will be of the same form with all of the zeros replaced with values that solve the puzzles.

It is not guaranteed that the returned solution is unique.

If the puzzle cannot be solved, the server will return 422.
