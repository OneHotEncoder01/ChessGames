# ChessGames


List of API Commands in MainWindow
__init__(self)
Initializes a new instance of MainWindow.
Configures window properties and sets up the chess board and UI components.
setup_ui(self)
Sets up the user interface components for the chess application.
This includes the SVG widget for the chess board, move input field, submit button, and status label.
update_board(self)
Updates the visual representation of the chess board.
Converts the chess board to an SVG image and displays it in the SVG widget.
make_move_from_input(self)
Retrieves the move from the input field, attempts to make the move on the chess board, and updates the UI accordingly.
Validates the move, clears the input field if successful, and updates the game status.
make_move(self, move_uci)
Processes a chess move given in UCI (Universal Chess Interface) format.
Checks if the move is legal, makes the move on the board if valid, and updates the board display.
get_board_state(self)
Retrieves the current state of the chess board in FEN (Forsyth-Edwards Notation).
Useful for analysis, saving the game state, or interfacing with chess engines.
current_turn(self)
Determines whose turn it is to move (either "white" or "black").
Useful for making decisions based on turn in external scripts or bots.
game_status(self)
Checks the current status of the game, such as checkmate, stalemate, and other draw conditions.
Provides a string describing the current game status, which is useful for game end detection and user notifications.
undo_move(self)
Reverts the last move made on the chess board.
Updates the board state and the UI, and removes the last move from the move history.
These commands provide a comprehensive interface for managing a chess game, making moves, and retrieving game information, which can be utilized in developing interactive chess applications or bots.
