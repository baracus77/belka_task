class RoomAction():

    def __init__(self):
        self.door_action = ("открыть", "закрыть")  # статус и команды двери
        self.lock_action = ("отпереть", "запереть")  # статус и команды замка
        self.quit = "выход"

    def door_default_state(self, door, lock, quit):
        self.door = door
        self.lock = lock
        self.quit = quit
        print("Дверь сейчас открыта, замок на двери не заперт")

    def door_actions(self):
        self.command = ""
        while self.command != self.quit:
            self.command = str.lower(input())

            if self.command in self.door_action: #открываем дверь
                if self.command == self.door_action[0] == self.door: #дверь открыта
                    print("Дверь уже открыта")
                elif self.command == self.door_action[0] != self.door: #дверь закрыта
                    if self.lock == self.lock_action[0]: #замок открыт
                        self.door = self.command
                        print("Вы открыли дверь")
                    else: #замок закрыт
                        print("Дверь открыть нельзя, заперта на замок")
                elif self.command == self.door_action[1] == self.door: #дверь закрыта
                    print("Дверь уже закрыта")
                elif self.command == self.door_action[1] != self.door:
                    if self.lock == self.lock_action[0]: #замок открыт
                        self.door = self.command
                        print("Вы закрыли дверь")
                    else: #замок закрыт
                        print("Дверь уже закрыта")

            elif self.command in self.lock_action: #открываем замок
                if self.command == self.lock_action[0]: #команда отпереть
                    if self.door == self.door_action[0]: #дверь открыта
                        print("Открытую дверь нельзя отпереть")
                    elif self.door == self.door_action[1]: #дверь закрыта
                        if self.lock == self.lock_action[0]: #замок отперт
                            print("Замок уже отперт")
                        else:
                            self.lock = self.command
                            print("Вы отперли замок")
                elif self.command == self.lock_action[1]: #команда запереть
                    if self.door == self.door_action[0]: #дверь открыта
                        print("Закрой дверь, чтобы Запереть замок")

                    elif self.door == self.door_action[1]: #дверь закрыта
                        if self.lock == self.lock_action[0]: #замок отперт
                            self.lock = self.command
                            print("Вы заперли замок")
                        else:
                            print("Замок уже заперт")
            elif self.command != self.quit :
                print("Введите корректную команду или выдите командой Выход")



room_class = RoomAction()
room_class.door_default_state(room_class.door_action[0],room_class.lock_action[0], room_class.quit)
room_class.door_actions()

