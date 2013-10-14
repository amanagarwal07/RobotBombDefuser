//Created by Aman Agarwal.



A robo bomb defuser game using the curses library in python.


The game is played in a F × F square grid called the field. A robot (which is a r × r square grid) moves in the field and cannot go outside the field.

The field has a bomb (b × b square grid) which you have to defuse. In order to defuse a bomb, the robot must have d number of defuse codes (a D × D square grid). Each of these codes contains vital information on how to defuse the bomb, and the bomb cannot be defused without exactly d codes.

The field has exactly d diffuse codes located at random positions. The user should move the robot around in order to collect these codes. When a robot approaches a diffuse code, it collects the code automatically (like in the Snake game, popular on cell phones, the snake eats its food automatically when it approaches the food).

When a robot approaches a bomb, the following things may happen

if the robot has exactly d defuse codes, the bomb is defused. The user gets s points for this.
if the robot has less than d defuse codes, the bomb explodes and the game ends.
Once the bomb is successfully defused, the game ends.

There are 2 levels in the game.The first level is easy with simple grid and the second level contains walls which increases the difficulty of the game.
