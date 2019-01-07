class Macros:
    def __init__(self):
        self.calories = 0
        self.protein = 0
        self.carbs = 0
        self.fats = 0

    def add_macros(self, cal, p, c, f):
        self.calories += cal
        self.protein += p
        self.carbs += c
        self.fats += f

    def get_total(self):
        return {
            "calories": self.calories,
            "protein": self.protein,
            "carbs": self.carbs,
            "fats": self.fats
        }