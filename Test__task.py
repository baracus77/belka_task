from random import randrange

door_action = ["открыть", "закрыть"] #статус и команды двери
lock_action = ["отпереть", "запереть"] #статус и команды замка


class RoomAction():

    #сообщение состояния двери
    def state_door_message(self, door_state, lock_state):
        self.door_state = door_state
        self.lock_state = lock_state
        if self.door_state == door_action[0]:
            self.door_state = "открыта"
        else:
            self.door_state = "закрыта"
        if self.lock_state == lock_action[1]:
            self.lock_state = "закрыт"
        else:
            self.lock_state = "открыт"
        print("Дверь сейчас " + self.door_state + ", кстати замок на двери " + self.lock_state)

    def state_door(self):    #генератор состояния двери и замка
        self.random_state_door = door_action[randrange(0, len(door_action))]     # генерируем состояние двери
        if self.random_state_door == door_action[1]:  # генерируем состояние Замка исходя из состояния двери
            self.random_state_lock = lock_action[randrange(0, len(lock_action))]
        else:
            self.random_state_lock = lock_action[0]
        #показываем состояние двери
        RoomAction.state_door_message(self, door_state=self.random_state_door, lock_state=self.random_state_lock)

    # ввод комманды для двери и вывод статуса
    def door_command(self):
        self.command = " "
        while self.command not in door_action:
            print("Введите корректную команду для двери")
            self.command = str.lower(input())
            if self.random_state_door == door_action[1] and self.random_state_door != self.command:   # открываем закрытую дверь
                if self.random_state_lock == lock_action[0]:
                    print("Дверь открыта!")
                else:
                    print("Дверь закрыта на замок, увы!")
                    continue
            elif self.random_state_door == door_action[1] == self.command:
                print("Дверь и так закрыта, попробуй её открыть!")
                self.command = ""
            elif self.random_state_door == door_action[0] and self.random_state_door != self.command:     # закрываем открытую дверь
                print("Вы закрыли дверь!")
            else:
                print("Дверь и так открыта, попробуй её закрыть!")
                self.command = ""


    # ввод комманды для замка и вывод статуса
    def lock_command(self):
        self.action = " "
        while self.action not in lock_action:
            print("Введите корректную команду замка двери")
            self.action = str.lower(input())
            if self.random_state_lock == lock_action[0] and self.random_state_lock != self.action: #замок открыт
                if self.command == door_action[1]:
                    print("Вы закрыли замок!")
                else:
                    print("Дверь открыта, замок закрыть нельзя!")
            elif self.random_state_lock == lock_action[0] == self.action:
                print("Дверь уже отперта!")
            if self.random_state_lock == lock_action[1] and self.random_state_lock != self.action: #открываем закрытую дверь
                if self.command == door_action[0]:
                    print("Вы отперли замок!")
                else:
                    print("Дверь уже заперта, попробуй открыть замок!")
                    self.action = " "


room_class = RoomAction()
room_class.state_door()
room_class.door_command()
room_class.lock_command()

