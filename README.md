
<!-- start project-info -->
<!--
project_title: Finit Automat
github_project: https://github.com/manudiv16/Finit_Automat
license: MIT
icon: /home/manu/PycharmProjects/Finit_Automat/doc/Unambiguous_finite_automaton.svg.png
homepage: 
license-badge: False
contributors-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![Contributors](https://img.shields.io/github/contributors-anon/manudiv16/Finit_Automat)
![Last commit](https://img.shields.io/github/last-commit/manudiv16/Finit_Automat)
[![CodeFactor](https://www.codefactor.io/repository/github/manudiv16/Finit_Automat/badge/master)](https://www.codefactor.io/repository/github/manudiv16/Finit_Automat/overview/master)
<!-- end badges -->

<!-- start description -->
Flask tool that manages the behavior of a finite automata.
Generate photos of the automata through calls to the api 
with a json that describes the automata
<!-- end description -->

<!-- start prerequisites -->
pip install -r requirements.txt

install Graphviz
> https://graphviz.org/download/
<!-- end prerequisites -->

<!-- start installing -->

<!-- end installing -->

<!-- start using -->
Json describes finit automaton
```json
{
    "deterministic":true,
    "alphabet": [
      "a",
      "b"
    ],
    "states": [
      {
        "state": 0,
        "final": false,
        "start": true,
        "morphs": {
          "a": 1,
          "b": 2
        }
      },
      {
        "state": 1,
        "final": false,
        "start": false,
        "morphs": {
          "a": 3,
          "b": 5
        }
      }
    ]
  }
```
<!-- end using -->

<!-- start contributing -->

<!-- end contributing -->

<!-- start contributors -->

<!-- end contributors -->

<!-- start table-contributors -->

<table id="contributors">
	<tr id="info_avatar">
	</tr>
	<tr id="info_name">
	</tr>
	<tr id="info_commit">
	</tr>
</table>
<!-- end table-contributors -->
