class Grade:
    def __init__(self, grade, credit_amount):
        self.TUAS_grade = grade
        self.credit_amount = credit_amount
        self.JASSO_grade = self.get_JASSO_grade()

    def get_JASSO_grade(self):
        match self.TUAS_grade:
            case 5:
                return 3
            case 3 | 4:
                return 2
            case 1 | 2:
                return 1
            case _:
                return 0