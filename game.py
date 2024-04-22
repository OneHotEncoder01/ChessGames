import sys
import chess
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyChess')
        self.setGeometry(100, 100, 800, 850)
        self.chessboard = chess.Board()
        self.move_history = []

        self.setup_ui()

    def setup_ui(self):
        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 780, 780)

        self.moveEntry = QLineEdit(self, placeholderText="Enter your move (e.g., e2e4)")
        self.moveEntry.setGeometry(10, 800, 200, 40)
        
        self.submitButton = QPushButton('Make Move', self)
        self.submitButton.setGeometry(220, 800, 100, 40)
        self.submitButton.clicked.connect(self.make_move_from_input)

        self.statusLabel = QLabel(self)
        self.statusLabel.setGeometry(330, 800, 450, 40)
        self.statusLabel.setText("Status: Ready to play")

        self.update_board()

    def update_board(self):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)

    def make_move_from_input(self):
        move_uci = self.moveEntry.text()
        if self.make_move(move_uci):
            self.moveEntry.clear()
            self.move_history.append(move_uci)
            self.statusLabel.setText(f"Last move: {move_uci} - {self.game_status()}")

    def make_move(self, move_uci):
        try:
            move = chess.Move.from_uci(move_uci)
            if self.chessboard.is_legal(move):
                self.chessboard.push(move)
                self.update_board()
                return True
            else:
                self.statusLabel.setText("Illegal move. Please try again.")
                return False
        except ValueError:
            self.statusLabel.setText("Invalid move format. Please try again.")
            return False

    def get_board_state(self):
        return self.chessboard.fen()

    def current_turn(self):
        return "white" if self.chessboard.turn == chess.WHITE else "black"

    def game_status(self):
        if self.chessboard.is_checkmate():
            return "Checkmate"
        elif self.chessboard.is_stalemate():
            return "Stalemate"
        elif self.chessboard.is_insufficient_material():
            return "Draw due to insufficient material"
        elif self.chessboard.can_claim_draw():
            return "Draw can be claimed"
        return "Game continues"

    def undo_move(self):
        if self.move_history:
            self.chessboard.pop()
            self.move_history.pop()
            self.update_board()
            self.statusLabel.setText("Move undone. It's your turn again.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
