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
        print("Команды для двери: закрыть - закрывает дверь, открыть - открывает дверь")
        print("Команды для замка двери: отпереть - отперает замок, запереть - запераает замок")
        print("\nДверь сейчас " + self.door_state + ", кстати замок на двери " + self.lock_state)

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
        self.door= " "
        while self.door not in door_action:
            print("Введите корректную команду для двери")
            self.door = str.lower(input())
            if self.door in door_action:
                if self.random_state_door == door_action[1] and self.random_state_door != self.door: # открываем закрытую дверь
                    if self.random_state_lock == lock_action[0]:
                        print("Дверь открыта!")
                    else:
                        print("Дверь закрыта на замок, увы!")
                        continue
                elif self.random_state_door == door_action[1] == self.door:
                    print("Дверь и так закрыта, попробуй её открыть!")
                    self.door = ""
                elif self.random_state_door == door_action[0] and self.random_state_door != self.door:   # закрываем открытую дверь
                    print("Вы закрыли дверь!")
                else:
                    print("Дверь и так открыта, попробуй её закрыть!")
                    self.door = ""
            else:
                self.door = ""
                print("Ошибка в команде двери")


    # ввод комманды для замка и вывод статуса
    def lock_command(self):
        self.lock = " "
        while self.lock not in lock_action:
            print("Введите корректную команду замка двери")
            self.lock = str.lower(input())
            if self.lock in lock_action:
                if self.random_state_lock == lock_action[0] and self.random_state_lock != self.lock: #замок открыт
                    if self.door == door_action[1]:
                        print("Вы закрыли замок!")
                    else:
                        print("Дверь открыта, замок закрыть нельзя!")
                elif self.random_state_lock == lock_action[0] == self.lock:
                    print("Дверь уже отперта!")
                if self.random_state_lock == lock_action[1] and self.random_state_lock != self.lock: #открываем закрытую дверь
                    if self.door == door_action[0]:
                        print("Вы отперли замок!")
                    else:
                        print("Дверь уже заперта, попробуй открыть замок!")
                        self.lock = " "
            else:
                self.lock = ""
                print("Ошибка в команде замка")


room_class = RoomAction()
room_class.state_door() #вызываем генерацию комнаты
room_class.door_command() #вызываем функцию ввода состояния двери
room_class.lock_command() #вызываем функцию ввода состояния замка

