from typing import List
from game.game_cell import Cell

class Calculate_word_value:
    
    def Calculate_word_value(word: List[Cell]) -> int:
        total_value = 0
        word_multiplier = 1

        for cell in word:
            tile = cell.letter
            letter_value = tile.value
            letter_multiplier = cell.multiplier

        if cell.multiplier_type == 'letter':
            letter_value *= letter_multiplier
        elif cell.multiplier_type == 'word':
            word_multiplier *= letter_multiplier

        total_value += letter_value

        return total_value * word_multiplier
