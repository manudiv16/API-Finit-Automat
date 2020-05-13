#Deterministic finite automaton
Esta clase dará comportamiento a los autómatas finitos deterministas. Para inicializarla crearemos
una tabla de hash que es la estructura de datos en la que me apoyare, una lista de los estados que
serán inicializados dentro de esta clase y los valores del alfabeto. Aparte de las funciones descritas
en el apartado de la interfaz esta clase también tendrá la función de minimizar.

## Dfa *class*
Create deterministic finite automaton
An example of how to initialize the class would be as follows.
The form of the json is described in the section itself.
> dfa = Dfa(json_dfa)

### minimize
Initialize sets with final states and the others , generate _dictionary with the minimized automaton
```pydocstring
        :return: _dictionary: Dict
```
### read
the firsts states determines the start of the automaton
```pydocstring
        :param: word: srt
        :return: is final ? : Bool
```
### dot_dictionary
Generate svg for automaton. Interactions with automata_IO api and graphviz.
```pydocstring
        :param: name of svg file:
```

