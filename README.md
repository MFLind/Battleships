# Massive Battleship Game

Massive Battleship game is a console based Python game that can run via webpage terminal.

User will be playing against a brutal computer opponents, each opponent will try to find each others ship, the first one that sunk all the opponent fleet wins.

A live view of the game of the game:
<img width="1051" alt="image" src="https://user-images.githubusercontent.com/106115510/197335860-e5644e5e-d3cf-433f-b0e3-a336d218c950.png">

# How to play the game
When starting up the game you will be asked for enter your name.

<img width="745" alt="image" src="https://user-images.githubusercontent.com/106115510/197336002-a4e13199-fc2e-434f-aff4-227a0c06d25c.png">

Then you should place out your 4 ships using X and Y coordinated of the playfield grid. Your ships are represented with "X" character.
<img width="745" alt="image" src="https://user-images.githubusercontent.com/106115510/197336027-4efd31da-5442-4ba2-8b42-a9100331fa82.png">

The computer opponent ships will be randomly placed on computer playfield.

The game starts with that the you will shoot your cannon on the computers playfield, by selecting X and Y coordinates, your result will be either a hit or miss (BOOM). Hits are represented with a "@" and misses (BOOM) "b" character.

<img width="745" alt="image" src="https://user-images.githubusercontent.com/106115510/197336252-39eaa2a2-c934-4e71-b72b-571b6f33e78a.png">

The first opponent that sink all the ships wins.

# Features
- Random placement of computers ships
- Player input for placement of ships
- Player can't see computer ships during the game
<img width="745" alt="image" src="https://user-images.githubusercontent.com/106115510/197336317-7079910a-56c7-4e13-bdcb-729ddba27e5a.png">
- Play againt computer
- Inputs are validated in all field
- Checks for if shooting on same positions
- Object oriented code with inheritance of child classes
- Board size and number of ships are defined in variables
- For generating computer placement using random.sample() getting all ships placement in one line.

## Future improvement
- Player can select the size of the playfield
- Implementation of score
- Make it possible for ships to be other sizes that 1 x 1 character

# Data model
The design is using classes to represent the BoardCell that get instancated either as empty, ship or BOOM.

<img width="426" alt="image" src="https://user-images.githubusercontent.com/106115510/197336737-cf53caf6-6304-4832-9f3f-1abf9c42c53b.png">

The main object is based on the Game class that holds a instance of Board class that has a array that represent that game field, the Board class has methods for setting and getting the X and Y coordinates that convert it to the array index.

The Game class has method to help the game flow for player placement of ships  player_ship_placement(). For shooting there is help function for player_fire() and computer_fire().

The Board class has helper function for printing the playfield show().

# Testing

I have done manual testing with the following methods:
- Running thru pylint for PEP8 validation and getting no errors
- Test playing the game both locally on my command prompt and also on Heroku: https://battleships-3.herokuapp.com/
- Testing inputs with both incorrect values and correct values

## Bugs
The development was done iterative and testing and finding bugs occure during the coding process.

## Remaining bugs
All KNOWN bugs are fixed.

## Validator Testing
- PEP8 via pylint locally on my computer

## Deployment
The Game is deployed using Code Institute's mock terminal for Heroku.
- Steps
  - For or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to to Python and NodeJS in that order
  - Link the Heroku app to the directory
  - Click on **Deploy**

# Credits
- Code Institute for deployment terminal
- Wikipedia for Battleship gameplay
- 
