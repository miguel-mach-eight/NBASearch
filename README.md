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

The program works with a nested for loop that sums all posible combinations of two 
NBA players' height. Following these cycles, the program searches for all matches. Two If statements give the final output,
either finding a definite amount of pairs or declaring a lack of them, prompting to try again with a different number.

## Authors

* **Miguel Figueroa** 
