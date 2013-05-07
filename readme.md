#pokehelp.py

Pokehelp is the main module. Import this to use functions that can compute type relations, multipliers and such and return an easily formatted result. The functions you will probably use the most are mentioned below, and the code is properly documented so you can go through it yourself.

##attackEffectivity

`atype` and `type1` are required. `type2` is optional, and fully works. Using these two/three, the module will calculate the effectivity of an `atype` attack against a Pokémon of types `type1` and `type2`.

`STAB` is optional, but if left as None, it will prompt the console for an input. In order to calculate an attack without STAB, just set it to 1.0.

`typedict` and `typedefdict` are best left alone, except if you're using custom types in another dictionary - which fully works.

Note that the functions checks for doubles between `type1` and `type2`. These lines:
```python
    if type1.lower() == type2.lower(): ## Check for two of the same type.
        type2 = None```
can be commented out to disable double checking.

##typegen()

Returns a random type from `typel`. Can be changed for choosing in a custom type list, but then you're probably better off using `random.choice()`.

##typeadv(), typedef(), typed(), typeadvD(), typedefD(), typedD()

Returns tuples containing advantages and defenses of `typec`. The D versions return the very same thing in dictionary form. `typed()` and `typedD()` have the `typedict` argument, which is able to set which dictionary to pick from.

#PokeAide.py

PokeAide uses `pokehelp.py` to compute effectivities and print tables for types that the user inputs. Useful for quick info.

#trainertrainer.py

Uses `pokehelp.py` to play a quiz game. It trains trainers! It's got a kinda cool but rudimentary 'dynamic learning' function that counts how often you get questions about a certain type right, and when you've reached a certain number of right answers it only asks you about other types. Can be turned off in its config. Try it!

#Usage

By all means, use `pokehelp.py` (and the other scripts, though they might not be as useful) for your own projects! No-one should have to go through manual data entry of every type ever again. If you do use it, I'd love to hear about your project! Just drop me a line at *@LpSamuelm* on Twitter or at *powpowd@gmail.com*.