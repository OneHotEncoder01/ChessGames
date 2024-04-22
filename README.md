## `MainWindow` API Documentation

### Overview

`MainWindow` extends `QWidget` from PyQt5 to create an interactive chess game interface. This class handles the game logic, user interactions, and updates the graphical representation of the chess board.

### Constructor

- **`__init__(self)`**
  - **Purpose**: Initializes a new instance of `MainWindow`.
  - **Description**: Sets up the main window dimensions, title, and initializes the chess board. It calls `setup_ui` to create the UI components.

### Methods

- **`setup_ui(self)`**
  - **Purpose**: Sets up the user interface components within the main window.
  - **Description**: Creates and positions the SVG widget for displaying the chess board, a text input for moves, a button for submitting moves, and a status label for game messages.

- **`update_board(self)`**
  - **Purpose**: Updates the SVG widget with the current state of the chess board.
  - **Description**: Converts the current state of the `chess.Board` to an SVG and loads it into the SVG widget. Called after each move to refresh the board display.

- **`make_move_from_input(self)`**
  - **Purpose**: Reads the user's input for a move, tries to execute it, and updates the board and game status.
  - **Description**: Extracts a move from the text input, calls `make_move` to process it, and clears the input field if the move is successful. Updates the move history and the status label with the result of the move.

- **`make_move(self, move_uci)`**
  - **Purpose**: Processes a chess move given in UCI (Universal Chess Interface) format.
  - **Description**: Checks if the move is legal, makes the move on the board if valid, and updates the board display.

- **`get_board_state(self)`**
  - **Purpose**: Retrieves the current state of the chess board in FEN (Forsyth-Edwards Notation).
  - **Description**: Useful for analysis, saving the game state, or interfacing with chess engines.

- **`current_turn(self)`**
  - **Purpose**: Determines whose turn it is to move.
  - **Description**: Returns "white" or "black" indicating whose turn it is to move. Useful for decision-making in external scripts or bots.

- **`game_status(self)`**
  - **Purpose**: Checks the current status of the game.
  - **Description**: Provides a string describing the current game status, such as checkmate, stalemate, or draw conditions. Useful for game end detection and user notifications.

- **`undo_move(self)`**
  - **Purpose**: Reverts the last move made on the chess board.
  - **Description**: Updates the board state and the UI, and removes the last move from the move history.
