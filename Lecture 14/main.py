# Football Team Managmenet System
#
# შექმენით კლასი FootballTeam შემდეგი ატრიბუტებით:
# team_name (string) - კლუბის სახელი
# coach (string) - მწვრთნელი
# players - მოთამაშეების სია(შექმნისას ცარიელი უნდა იყოს)
#
# კლასს უნდა გააჩნდეს შემდეგი მეთოდები:
# 1. მოთამაშის დამატება - მოთამაშის სახელი, პოზიცია, სათამაშო ნომერი,
#    ასაკი და ეროვნება(დიქტის სახით უნდა დაემატოს მოთამაშეების სიაში)
#
# 2. მოთამაშის წაშლა - მოთამაშე უნდა წაიშალოს სიიდან სათამაშო ნომრის მიხედვით
#
# 3. მოთამაშის ინფორმაციის განახლება - მოთამაშე უნდა მონახოთ სათამაშო ნომრის მიხედვით
#    და უნდა დაუსეტოთ ისეთი ინფორმაცია, რომელსაც გადასცემთ ამ მეთოდს, მაგ: "goal": 1
#    ანუ key და value უნდა იყოს გადაცემული ამავე მეთოდის გამოძახებისას!
#
# 4. კლუბის ინფორმაციის ჩვენება - გამოიტანეთ კლუბის სახელი, მწვრთნელის სახელი და მოთამაშეების სია
#
# 5. მოთამაშის ინფორმაციის ჩვენება - უნდა გამოიტანოთ ინფორმაცია მოთამაშის ნომრის მიხედვით

class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player_info):
        self.players.append(player_info)

    def remove_player(self, jersey_number):
        self.players = [player for player in self.players if player['jersey_number'] != jersey_number]

    def update_player_info(self, jersey_number, **kwargs):
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                player.update(kwargs)
                break

    def show_team_info(self):
        print(f"Team Name: {self.team_name}, Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def show_player_info(self, jersey_number):
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                print(player)
                break

if __name__ == "__main__":
    team = FootballTeam("FC Example", "John Doe")

    team.add_player({"name": "Alice Smith", "position": "Forward", "jersey_number": 10,"age": 25, "nationality": "USA"})

    team.add_player({"name": "Bob Johnson", "position": "Midfielder", "jersey_number": 8, "age": 27, "nationality": "Canada"})

    team.add_player({"name": "Charlie Brown", "position": "Defender", "jersey_number": 5, "age": 22, "nationality": "UK"})

    team.remove_player(5)

    team.update_player_info(10, goals=1, assists=2, matches_played=5)



    team.show_team_info()
