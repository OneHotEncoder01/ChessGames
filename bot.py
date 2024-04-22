from PyQt5.QtWidgets import QApplication
from game import MainWindow
import chess
import random
import sys 

class ChessBot:
    def __init__(self, game_window):
        self.game_window = game_window
        self.game_window.moveMade.connect(self.respond_to_move)  # Connect to the signal
        self.game_window.show()

    def respond_to_move(self):
        """Respond to a move if it's the bot's turn."""
        if self.game_window.current_turn() == "black":  # Assuming the bot plays as black
            legal_moves = list(self.game_window.chessboard.legal_moves)
            if legal_moves:
                move = random.choice(legal_moves)
                move_uci = move.uci()
                self.game_window.make_move(move_uci)
                print(f"Bot played: {move_uci}")
                print(f"Game status: {self.game_window.game_status()}")

if __name__ == "__main__":
    app = QApplication([])
    game_window = MainWindow()
    bot = ChessBot(game_window)
    sys.exit(app.exec_())
