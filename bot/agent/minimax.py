import random
from ..goboard import GameState
from ..gotypes import Player, Point

class MiniMaxBot(Agent):
    def select_move(self, game_state):
        winning_moves = []
        draw_moves = []
        losing_moves = []

        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            opponent_best_outcome = best_result(next_state)
            our_best_outcome = reverse_game_result(opponent_best_outcome)
            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome == GameResult.draw:
                draw_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)

        if winning_moves:
            return random.choice(winning_moves)

        if draw_moves:
            return random.choice(draw_moves)
        
        return random.choice(losing_moves)

    def best_result_recursive(self, game_state):
        if game_state.is_over():
            if game_state.winner() == game_state.next_player:
                return GameResult.win
            elif game_state.winner() is None:
                return GameResult.draw
            else
                return GameResult.loss
        
        best_result_so_far = GamResult.loss
        opponent = game_state.next_player.other

        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)
            opponent_best_result = best_result(next_state)
            our_result = reverse_game_result(opponent_best_result)

            if our_result.value > best_result_so_far.value:
                best_result_so_far = our_result
        
        return best_result_so_far

    def capture_diff(self, game_state):
        black_stones = 0
        white_stones = 0

        for r in range(1, game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                p = Point(r, c)
                color = game_state.board.get(p)
                if color == Player.black:
                    black_stones += 1
                elif color == Player.white:
                    white_stones += 1
        
        diff = black_stones - white_stones
        if game_state.next_player == Player.black:
            return diff
        else:
            return -1 * diff
    
    def alpha_beta_reult(self, game_state, max_depth, best_black, best_white, eval_fn):
        if game_state.is_over():
            if game_state.winner() == game_state.next_player:
                return MAX_SCORE
            else:
                return MIN_SCORE

        if max_depth == 0:
            return eval_fn(game_state)

        best_so_far = MIN_SCORE

        for candidate_move in game_state.legal_moves():
            next_state = game_state.apply_move(candidate_move)
            opponent_best_result = self.alpha_beta_reult(next_state, max_depth - 1,  best_black, best_white, eval_fn)
            our_result = -1*opponent_best_result
            
            if our_result > best_so_far:
                our_result = best_so_far
            
            if game_state.next_player == Player.white:
                if best_so_far > best_white:
                    best_white = best_so_far
                
                outcome_for_black = -1 * best_so_far
                if outcome_for_black < best_black:
                    return best_so_far
            elif game_state.next_player == Player.black:
                if best_so_far > best_black:
                    best_black = best_so_far
                
                outcome_for_white = -1 * best_so_far
                if outcome_for_white < best_white:
                    return best_so_far
        
        return best_so_far

