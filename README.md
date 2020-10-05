
<!-- start project-info -->
<!--
project_title: API Finit Automaton
github_project: https://github.com/manudiv16/API-Finit-Automaton
license: MIT
icon: /home/manu/PycharmProjects/Finit_Automat/doc/Thompson-kleene-star.svg
homepage: https://github.com/manudiv16/API-Finit-Automaton
Docker:https://n
license-badge: False
contributors-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![Contributors](https://img.shields.io/github/contributors-anon/manudiv16/API-Finit-Automaton)
![Last commit](https://img.shields.io/github/last-commit/manudiv16/API-Finit-Automaton)
![CodeFactor](https://www.codefactor.io/repository/github/manudiv16/api-finit-automaton/badge)
<!-- end badges -->

<!-- start description -->
# Welcome to Finit Automat
<img id="icon" width="128" height="128" align="right" src="doc/icon.png"/>
Flask tool that manages the behavior of a finite automata.
Generate photos of the automata through calls to the api 
with a json that describes the automata

<!-- end description -->

<!-- start prerequisites -->
## Prerequisites

pip install -r requirements.txt

install Graphviz
> https://graphviz.org/download/

<!-- end prerequisites -->

<!-- start installing -->


<!-- end installing -->

<!-- start using -->
## How generate json of automaton

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
## contributors 
<table id="contributors">
	<tr id="info_avatar">
		<td id="manudiv16" align="center">
			<a href="https://github.com/manudiv16">
				<img src="https://avatars3.githubusercontent.com/u/38869988?v=4" width="100px"/>
			</a>
		</td>
	</tr>
	<tr id="info_name">
		<td id="manudiv16" align="center">
			<a href="https://github.com/manudiv16">
				<strong>Fran Martin</strong>
			</a>
		</td>
	</tr>
	<tr id="info_commit">
		<td id="manudiv16" align="center">
			<a href="/commits?author=manudiv16">
				<span id="role">💻</span>
			</a>
		</td>
	</tr>
</table>
<!-- end table-contributors -->
