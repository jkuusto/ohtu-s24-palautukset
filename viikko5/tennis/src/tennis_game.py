class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE_GAME = 4
    PLAYER1_ADVANTAGE = 1
    PLAYER2_ADVANTAGE = -1
    WIN_MARGIN = 2
    CHECK_PLAYER1_SCORE = 1
    CHECK_PLAYER2_SCORE = 2
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        if self.m_score1 == self.m_score2:
            score = self.equal_score()
        elif self.m_score1 >= self.ADVANTAGE_GAME or \
            self.m_score2 >= self.ADVANTAGE_GAME:
            score = self.advantage_score()
        else:
            score = self.normal_score(score)
        return score

    def equal_score(self):
        if self.m_score1 == self.LOVE:
            return "Love-All"
        elif self.m_score1 == self.FIFTEEN:
            return "Fifteen-All"
        elif self.m_score1 == self.THIRTY:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def advantage_score(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == self.PLAYER1_ADVANTAGE:
            return "Advantage player1"
        elif minus_result == self.PLAYER2_ADVANTAGE:
            return "Advantage player2"
        elif minus_result >= self.WIN_MARGIN:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def normal_score(self, score):
        score = ""
        temp_score = 0
        for i in range(self.CHECK_PLAYER1_SCORE,
                       self.CHECK_PLAYER2_SCORE + 1):
            if i == self.CHECK_PLAYER1_SCORE:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            if temp_score == self.LOVE:
                score = score + "Love"
            elif temp_score == self.FIFTEEN:
                score = score + "Fifteen"
            elif temp_score == self.THIRTY:
                score = score + "Thirty"
            elif temp_score == self.FORTY:
                score = score + "Forty"
        return score
