# NBA SCRAPER

This little program handles the search for NBA players combined heights that match a given integer input. Their heights
and names are acquired from a database of NBA players' physical data for the 2008 - 2009 season (https://mach-eight.uc.r.appspot.com/).  

## Getting Started

Run the accompanying python file 'NBAsearch.py' in your IDE of choice. It will automatically ask you for the integer
input you want to run the code with. 

### Prerequisites

You only need Python 3.9 installed in your device, as well as the 'requisites' Python package. You may already have it
in your library, but otherwise, you can easily install it with a pip command like this 

'$ python -m pip install requests'


### Output

Once you enter an integer value, the program will find all possible pairs of players
whose height in inches adds up to the integer input, for example:

```
> insert some number: 140
['Chucky Atkins & Nate Robinson', 'Speedy Claxton & Nate Robinson', 'Brevin Knight & Mike Wilks']
```

If there's no matches, the output will simply be:

```
>insert some number: 127
No matches found, please try with a new number 
```

### Algorithm

The program works with a Divide and conquer Algorithm searching for all posible combinations of two 
NBA players' height. This algorithm is an improved version of the initial code, which followed a naive implementation.

## Authors

* **Miguel Figueroa** 
