import random


class TeamSplitter:
    def __init__(self, players, num_teams):
        """
        Инициализация объекта для разделения игроков на команды.
        :param players: Список имен игроков.
        :param num_teams: Количество команд.
        """
        self.players = [player.strip() for player in players]
        self.num_teams = num_teams
        self.teams = {}

    def validate_input(self):
        """
        Проверяет корректность входных данных.
        :return: Сообщение об ошибке или None, если всё корректно.
        """
        if self.num_teams <= 0:
            return "Ошибка: Количество команд должно быть положительным числом."
        if len(self.players) < self.num_teams:
            return f"Ошибка: Недостаточно игроков для создания {self.num_teams} команд."

        return None  # Все корректно

    def split_players_into_teams(self):
        """
        Разбивает список игроков на команды с максимально равным распределением.
        """
        random.shuffle(self.players)  # Перемешиваем список игроков случайным образом

        # Определяем количество игроков в каждой команде
        players_per_team = len(self.players) // self.num_teams
        extra_players = len(self.players) % self.num_teams  # Количество игроков, которых нужно распределить по командам

        # Разбиваем игроков по командам
        start_idx = 0
        for i in range(self.num_teams):
            end_idx = start_idx + players_per_team + (
                1 if extra_players > 0 else 0)  # Добавляем по 1 игроку в первые команды
            self.teams[f"Команда {i + 1}"] = self.players[start_idx:end_idx]
            start_idx = end_idx
            extra_players -= 1

    def print_teams(self):
        """
        Выводит команды на экран.
        """
        for team_name, members in self.teams.items():
            print(f"{team_name}: {', '.join(members)}")


if __name__ == "__main__":
    # Ввод данных от пользователя
    players_input = input("Введите имена игроков через запятую: ").split(",")

    try:
        num_teams = int(input("Введите количество команд: "))

        # Создаем объект TeamSplitter
        team_splitter = TeamSplitter(players_input, num_teams)

        # Проверяем корректность данных
        validation_error = team_splitter.validate_input()
        if validation_error:
            print(validation_error)
        else:
            # Разбиваем на команды и выводим результат
            team_splitter.split_players_into_teams()
            team_splitter.print_teams()

    except ValueError:
        print("Ошибка: Введите корректные числовые значения для количества команд.")
