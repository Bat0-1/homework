# წინა დავალება გადააკეთეთ შემდეგნაირად:
#
# ცალკე შექმენით მოთამაშის კლასი შემდეგი ატრიბუტებით:
# მოთამაშის აიდი: ავტომატურად ენიჭებოდეს და იზრდებოდეს ერთით ყოველი მოთამაშის ობიექტის შექმნისას,
# სახელი, პოზიცია, სათამაშო ნომერი(private), ასაკი(private) და ეროვნება.
#
# მეთოდები:
# მოთამაშის სრული ინფორმაციის ჩვენება,
# __str__,
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები
#
# ცალკე შექმენით მწვრთნელის კლასი შემდეგი ატრიბუტებით:
# სახელი და გამოცდილების წლები(private).
#
# მეთოდები:
# მწვრთნელის სრული ინფორმაციის ჩვენება,
# __str__
# სურვილისამებრ შეგიძლიათ დაუმატოთ მეთოდები
#
# საბოლოოდ შექმენით Team კლასი შემდეგი ატრიბუტებით:
# სახელი, მწვრთნელი(მწვრთნელის ობიექტი) და მოთამაშეები(მოთამაშის ობიექტების სია).
# მეთოდები:
# მოთამაშის დამატება,
# მოთამაშის ძებნა აიდის მიხედვით და ინფორმაციის გამოტანა,
# მოთამაშის ინფორმაციის განახლება(წინა დავალების ანალოგიურად ოღონდ აიდის მიხედვით),
# მოთამაშის წაშლა(აიდის მიხედვით),
# კლუბის სრული ინფორმაციის ჩვენება(სახელი, მწვრთნელი, მოთამაშეები),
# __str__
#
# ბონუსი: კლუბში ვერ უნდა ემატებოდეს 25 მოთამაშეზე მეტი,
# აწარმოეთ მოთამაშის სტატისტიკა(რამდენი მატჩი ითამაშა, რამდენი გოლი გაიტანა და ა.შ.)


class Player:
    def __init__(self, name, position, jersey_number, age, nationality):
        self.id = Player.generate_id()
        self.name = name
        self.position = position
        self.__jersey_number = jersey_number
        self.__age = age
        self.nationality = nationality
        self.goals = 0
        self.assists = 0
        self.matches_played = 0

    def __str__(self):
        return (
            f"Player ID: {self.id}, Name: {self.name}, Position: {self.position}, "
            f"Jersey Number: {self.__jersey_number}, Age: {self.__age}, Nationality: {self.nationality}, "
            f"Goals: {self.goals}, Assists: {self.assists}, Matches Played: {self.matches_played}"
        )

    def display(self):
        print(self.__str__())

    @staticmethod
    def generate_id():
        if not hasattr(Player, '_id_counter'):
            Player._id_counter = 0
        Player._id_counter += 1
        return Player._id_counter


class Coach:
    def __init__(self, name, years_of_experience):
        self.name = name
        self.__years_of_experience = years_of_experience

    def __str__(self):
        return f"Name: {self.name}, Years of Experience: {self.__years_of_experience}"

    def display(self):
        print(self.__str__())


class Team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []
        self.max_players = 25

    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)
        else:
            print("Cannot add player: Team is full (maximum 25 players allowed).")

    def find_player_by_id(self, player_id):
        for player in self.players:
            if player.id == player_id:
                return player
        return None

    def update_player(self, player_id):
        player = self.find_player_by_id(player_id)
        if player:
            print("Enter new statistics for the player:")

            def get_int_input(prompt):
                while True:
                    try:
                        return int(input(prompt))
                    except ValueError:
                        print("Please enter a valid number.")

            player.goals = get_int_input("Goals: ")
            player.assists = get_int_input("Assists: ")
            player.matches_played = get_int_input("Matches Played: ")

            print("Player statistics updated.")
        else:
            print("Player not found.")

    def remove_player(self, player_id):
        player = self.find_player_by_id(player_id)
        if player:
            self.players.remove(player)
        else:
            print("Player not found.")

    def show_team_info(self):
        print(f"Team Name: {self.team_name}")
        print(f"Coach: {self.coach}")
        print("Players:")
        for player in self.players:
            print(player)

    def __str__(self):
        return f"Team Name: {self.team_name}, Coach: {self.coach}, Players Count: {len(self.players)}"

    def display(self):
        print(f"Team Name: {self.team_name}")
        print("Coach Info:")
        self.coach.display()
        print("Players:")
        for player in self.players:
            player.display()

if __name__ == "__main__":
    coach = Coach("John Doe", 10)
    team = Team("FC Example", coach)

    player1 = Player("Alice Smith", "Forward", 10, 25, "USA")
    player2 = Player("Bob Johnson", "Midfielder", 8, 27, "Canada")
    player3 = Player("Charlie Brown", "Defender", 5, 22, "UK")
    player4 = Player("David Wilson", "Goalkeeper", 1, 30, "Australia")
    player5 = Player("Eve Davis", "Forward", 9, 24, "Germany")
    player6 = Player("Frank Miller", "Midfielder", 11, 28, "France")
    player7 = Player("Grace Lee", "Defender", 3, 26, "Spain")
    player8 = Player("Hank Taylor", "Goalkeeper", 12, 29, "Italy")
    player9 = Player("Ivy Anderson", "Forward", 7, 23, "Brazil")
    player10 = Player("Jack Thomas", "Midfielder", 4, 21, "Argentina")
    player11 = Player("Kathy Martinez", "Defender", 2, 20, "Mexico")
    player12 = Player("Leo Garcia", "Goalkeeper", 6, 31, "Portugal")
    player13 = Player("Mia Rodriguez", "Forward", 14, 19, "Netherlands")
    player14 = Player("Nina Hernandez", "Midfielder", 15, 18, "Sweden")
    player15 = Player("Oscar Lopez", "Defender", 13, 32, "Russia")
    player16 = Player("Paul Walker", "Goalkeeper", 16, 33, "Japan")
    player17 = Player("Quinn Young", "Forward", 17, 34, "South Korea")
    player18 = Player("Rita King", "Midfielder", 18, 35, "China")
    player19 = Player("Sam Scott", "Defender", 19, 36, "India")
    player20 = Player("Tina Green", "Goalkeeper", 20, 37, "South Africa")
    player21 = Player("Uma White", "Forward", 21, 38, "Nigeria")
    player22 = Player("Vera Black", "Midfielder", 22, 39, "Egypt")
    player23 = Player("Will Blue", "Defender", 23, 40, "Turkey")
    player24 = Player("Xena Gray", "Goalkeeper", 24, 41, "Greece")
    player25 = Player("Yara Brown", "Forward", 25, 42, "Poland")
    player26 = Player("Zane Red", "Midfielder", 26, 43, "Ukraine")

    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)
    team.add_player(player4)
    team.add_player(player5)
    team.add_player(player6)
    team.add_player(player7)
    team.add_player(player8)
    team.add_player(player9)
    team.add_player(player10)
    team.add_player(player11)
    team.add_player(player12)
    team.add_player(player13)
    team.add_player(player14)
    team.add_player(player15)
    team.add_player(player16)
    team.add_player(player17)
    team.add_player(player18)
    team.add_player(player19)
    team.add_player(player20)
    team.add_player(player21)
    team.add_player(player22)
    team.add_player(player23)
    team.add_player(player24)
    team.add_player(player25)
    team.add_player(player26)  # არ დაემატება ლიმიტის გამო

    team.show_team_info()

    # team.remove_player(player24.id)
    # print("\nAfter removing a player:")
    # team.show_team_info()

    # team.update_player(player25.id)
    # print("\nAfter updating a player's information:")
    # team.show_team_info()

    # print("\nFinding player by ID:")
    # found_player = team.find_player_by_id(player1.id)
    # if found_player:
    #     print(found_player)
    # else:
    #     print("Player not found.")

