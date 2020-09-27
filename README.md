# aliens_board_game
Simulation of Aliens(1989) board game

Main file is aliens.py, run the game loop by creating an instance of AliensSimulation, there is a test instance below AliensSimulation.  Currently runs limited game turns where marines are stationary, and aliens move randomly across the board.  
Aliens will attack marines if they occupy the same space.  Marines have no actions currently, aside from defending alien attacks.

 - Spawns in aliens into the game board per the board game rules (4 for first turn, 2 on each subsequent turn)
 - Spawns in 9 marines
 - Marines don't move, yet.
 - Aliens move randomly, for now.
 - Print calls at bottom of main_loop method are just checking various alien/marine values for testing purposes.
