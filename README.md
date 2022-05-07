<h2>Adventure Game!!</h2>

<h3>Project Instructions</h3>
  
<ol>1. Print descriptions of what's happening for the player</ol>

<li>One thing the game will need to do is to print messages for the player to describe what is happening. Like at the start of the example game, these lines are printed:</li>

<i>You find yourself standing in an open field, filled with grass and yellow wildflowers.  
Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.
...</i>

<body>This is a very small step, but a good way to get started!</body>

  <h4>Task List</h4>
  
  <ol>2. Pausing between printing descriptions</ol>
  
<li>Now, one thing you might have noticed is that when you have multiple print statements, they get displayed in the terminal so fast that it looks like they all just show up at the same time. That's no good.</li>

<i>If you look at the example game, there's a short delay after each line is printed.</i>

<span>You may remember that earlier in the course, we briefly introduced the time module and the <blockquote>time.sleep()</blockquote> function:</span>

<blockquote>import time
print("Hello")
time.sleep(2)
  print("world!")</blockquote>

  <body>This will cause a 2-second delay after the first <blockquote>print()</blockquote> statement. Give it a try with the messages in your code!</body>

<h4>Task List</h4>

<sup>In the example game, each time we make a choice, something happens, and we are offered 2 choices again till we win or lose. For now, just focus on writing code for the 2 choices you have.</sup>

<sub>If the player knocks on the door of the house, what happens?
If the player enters the cave, what happens?
We will be dealing with subsequent choices after the first choice in the upcoming steps.
  </sub>
<ol>4. Make sure the player gives a valid input</ol>
<li>Up till now, our program prints a description of the game-world to the player, gives them a choice, and prints what happens depending on their choice. An important thing to notice in the example game is that if the player enters something other than 1 or 2, the game keeps asking them for a 1 or 2. We don't want the game to accept invalid input, like 75 or foo!</li>

<blockquote>(Please enter 1 or 2.)
75
(Please enter 1 or 2.)
foo
(Please enter 1 or 2.)
If the player tries to respond with something invalid, your program should ask them to try again—and it should keep asking them to try again until they give valid input.</blockquote>

<h4>Task List</h4>

<div>Recall the data type in which the <blockquote>input()</blockquote> functions stores the user input, and add code accordingly.</div>

<ol>5. Add functions and refactor your code</ol>
<li>By now, you may have noticed that some of your code is getting pretty messy, and some parts may be kind of repetitive. If you haven't already, this would be a good time to consider defining some functions, and moving some of your code into those functions.</li>

<i>For example, you probably have a lot of code that looks like this:<i>

  <blockquote>print("You find yourself standing in an open field, filled with grass and",
      "yellow wildflowers.")
time.sleep(2)
print("Rumor has it that a wicked fairie is somewhere around here, and has",
      "been terrifying the nearby village.")
time.sleep(2)
print("In front of you is a house.")
time.sleep(2)
print("To your right is a dark cave.")
time.sleep(2)
print("In your hand you hold your trusty (but not very effective) dagger.")
time.sleep(2)
    ....</blockquote>
  
<i>This is quite repetitive—we are using print, sleep, print, sleep, print, sleep, over and over ...<i>

<strong>One improvement that you can make is to define your own function so that it will both print and sleep—you might call it the print_pause function.</strong>

<span>With such a function, you could simply pass it a message to print, and it would take care of the pausing:</span>
<blockquote>
print_pause("You find yourself standing in an open field, filled with grass",
            "and yellow wildflowers.")
print_pause("Rumor has it that a wicked fairie is somewhere around here,",
            "and has been terrifying the nearby village.")
print_pause("In front of you is a house.")
print_pause("To your right is a dark cave.")
print_pause("In your hand you hold your trusty (but not very effective)",
            "dagger.")
....</blockquote>
  
<i>Here's another way you can use functions in a game like this—you can define a function for each place the player can go. In the example game, the code looks something like this:</i>
  
<blockquote>
def fight():
    # Things that happen when the player fights  

def cave():
    # Things that happen to the player goes in the cave  

def field():
    # Things that happen when the player runs back to the field

def house():
    # Things that happen to the player in the house</blockquote>

  <span>That way, when the player chooses to go to one of these places, you can simply call the function that displays the description and choices for that place. This is especially good if you want the player to be able to go back to the same place repeatedly, from different locations in the code. In the example game, the player can get back to the field from both the house and the cave, and having the field function makes this much easier.

Usually, each function will print what happens after the player takes a certain choice, then offer another choice, and call the specific function depending on the choice the player makes. In the end, you would want to have a <blockquote>play_game()</blockquote> or <blockquote>main()</blockquote> function, which starts the game.

These are just a few examples of how you can use functions in your project. You'll probably find other ways you can clean up the code and reduce repetitiveness by defining (and calling) functions. (In fact, it's possible to do this project with almost every line of code being placed inside a function definition!)</span>

<h4>Task List</h4>

  <ol>6. Use randomness in your game</ol>
<li>Another key feature of most games is randomness or chance. If everything always happens exactly the same way, it can become boring and predictable.</li> 

<body>There are all sorts of ways you could use randomness in your game. Here are just a few possibilities:

In the example game, the enemy creature is selected randomly each time they play. Sometimes it's a pirate, sometimes it's a troll, and so on.
You could do something similar to randomize which weapons or magical items the player encounters.
You could include a combat simulation in which the player and enemy deal random amounts of damage to one another <i>(you may remember that we did something like this earlier in the course)</i>.
All of these can be done using Python's random module and the <blockquote>random.choice <blockquote> and <blockquote>                                     random.randint</blockquote> functions that we learned about earlier. <i>For example: At the start of each game, you can set the random enemy creature.</i>

<body>There are countless other possible ways to use randomness in your game—feel free to be creative here.</body>

<h4>Task List</h4>


<ol>7. Create win and lose conditions</ol>
  <li>Eventually, the game should come to an end—and tell the player that they won or lost.</li>

<body>The end result of the game should be influenced by the player's choices (and possibly some degree of randomness as well). Generally, it's a good idea to use randomness to only partially influence the outcome. If what happens to the player is completely random, the player will feel out of control and probably won't enjoy it.</body>

<strong>For example, in our example game, the player fights the enemy creature. If they win the fight, they win the game!</strong>

<h4>Task List</h4>

<ol>8. Check if the player wants to play again</ol>
<li>When Python gets to the end of your script, it will exit back to the terminal. But that's not a good player experience. Instead, it would be better if the game asked the player whether they want to play again:</li>

<strong>GAME OVER</strong>

<i>Would you like to play again? (y/n)</i>

  <body>Just like with other choices you've asked the player to make, this will need to get the player's input and then check if the input is valid.

If the player indicates that yes, they want to play again, then the game should start over. Depending on what you added to your game, there may be some things that need to be reset. For example, if your player has a health score or they picked up magical items, these should go back to the way they were when the game starts over..</body>

<i>For example, in our example game, after the player fights the enemy, they are asked if they want to play the game again irrespective of whether or not they won</i>




