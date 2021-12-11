import json

class Films:
    def __init__(self):
        try:
            with open("films.json", "r") as f:
                self.films = json.load(f)

        except FileNotFoundError:
            self.films = []

    def all(self):
        return self.films

    def get(self, id):
        return self.films[id]

    def create(self, data):
        data.pop('csrf_token')
        self.films.append(data)

    def save_all(self):
        with open("films.json", "w") as f:
            json.dump(self.films, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.films[id] = data
        self.save_all()

films = Films()