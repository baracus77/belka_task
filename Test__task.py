from random import randrange

Commands_door = ["открыть", "закрыть"] #статус и команды двери
Door_actions = ["запереть", "отпереть"] #статус и команды замка


class RoomAction():
    def stateDoor(self):    #генератор состояния двери и замка
        self.random_state_door = Commands_door[randrange(0, 2)]     # генерируем состояние двери
        if self.random_state_door == Commands_door[1]:  # генерируем состояние Замка исходя из состояния двери
            self.random_state_lock = Door_actions[randrange(0, 2)]
        else:
            self.random_state_lock = Door_actions[1]
            print("")
        print(self.random_state_door, self.random_state_lock)


    # ввод комманды для двери и вывод статуса
    def send_door_command(self):
        self.command = " "
        while self.command not in Commands_door:
            print("Введите корректную команду для двери")
            self.command = str.lower(input())
            if self.random_state_door == Commands_door[1] and self.random_state_door != self.command:   # открываем закрытую дверь
                if self.random_state_lock == Door_actions[1]:
                    print("Дверь открыта!")
                else:
                    print("Дверь закрыта на замок, увы!")
                    continue
            elif self.random_state_door == Commands_door[1] == self.command:
                print("Дверь и так закрыта, попробуй её открыть!")
                self.command = ""
            elif self.random_state_door == Commands_door[0] and self.random_state_door != self.command:     # закрываем открытую дверь
                print("Вы закрыли дверь!")
            else:
                print("Дверь и так открыта, попробуй её закрыть!")
                self.command = ""


    # ввод комманды для замка и вывод статуса
    def send_lock_command(self):
        self.action = " "
        while self.action not in Door_actions:
            print("Введите корректную команду замка двери")
            self.action = str.lower(input())
            if self.random_state_lock == Door_actions[0] and self.random_state_lock != self.action: #закрытая дверь, закрытие замка
                if self.command == Commands_door[1]:
                    print("Вы закрыли замок!")
                else:
                    print("Дверь открыта, замок закрыть нельзя!")
            elif self.random_state_lock == Door_actions[1] == self.action:
                print("Дверь уже закрыта!")
            if self.random_state_lock == Door_actions[1] and self.random_state_lock != self.action: #открываем закрытую дверь
                if self.command == Commands_door[1]:
                    print("Вы открыли замок замок!")
                else:
                    print("Дверь открыта, замок закрыть нельзя!")


room_class = RoomAction()
room_class.stateDoor()
room_class.send_door_command()
room_class.send_lock_command()

