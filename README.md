# war-game
Python card game "War"

Requirements:
1. The game starts by asking names of 2 players
2. After entering the second name, the deck card is initialized, shuffled, and split into 2
3. Input of 'next' should initiate round. The input of 'done' ends the game and outputs the current score
4. Every round two strings of cards names are displayed - 1 from each player. The cards are taken from their 'piles' in a row, not randomly
5. Cards are shown in a frame for more visual appeal
6. When a player wins the round it shows who the winner is.
7. If the same cards are shown the system outputs WAR and the next cards are put and the war continues until one player wins
8. The game continues until 'done' is inputted or one player has no more cards
9. If the game ends with one player having no cards, the game outputs "Game over, the winner is {player.name}"
