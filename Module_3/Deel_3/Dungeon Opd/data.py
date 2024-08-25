import string

class player:
    noice:int = 0
    pickups:list = []

    def add_noice(self):
        self.noice += 1

    def add_pickup(self, pickup:str):
        self.pickups.append(pickup)

    def remove_pickup(self, pickup:str):
        self.pickups.remove(pickup)

    def get_noice(self):
        return self.noice
    
    def has_pickup(self, pickup):
        return pickup in self.pickups
    
    def to_dict(self):
        return {
            'noice' : self.noice,
            'pickups' : self.pickups
        }

class route:
    roomsvisted:list = []
    roomanswers:list = []
    errors:list = []

    doorcode:str = ''
    doorcode:str = ''

    def add_to_route(self, roomNumber:str):
        self.roomsvisted.append(roomNumber)

    def add_to_answers(self, answer):
        self.roomanswers.append(answer)

    def get_previous_room(self):
        if len(self.roomsvisted) == 0:
            return False

        return self.get_last_room()

    def get_last_answer(self) -> str:
        if len(self.roomanswers) == 0:
            return ''
        
        return self.roomanswers[-1]
    
    def get_last_room(self) -> str:
        if len(self.roomsvisted) == 0:
            return '?'

        return self.roomsvisted[-1]

    def get_answer_by_roomnumber(self, room_number):
        try:
            awnserIndex = self.roomsvisted.index(room_number)
        except ValueError as e:
            return ''
    
        return self.roomanswers[awnserIndex]

    def get_doorcode(self):
        self.doorcode = ''.join(self.roomsvisted)
        return self.doorcode
    
    def get_code(self):
        self.routecode = '_'.join(self.roomsvisted)
        return self.routecode
    
    def to_dict(self):
        return {
            'routetaken' : [f'step {string.ascii_uppercase[i]} : {self.roomsvisted[i]}' for i in range(len(self.roomsvisted))],
            'doorcode' : self.doorcode,
            'errors' : self.errors,
            'roomanswers' : [f'room{self.roomsvisted[i]} : {self.roomanswers[i]}' for i in range(len(self.roomanswers))]
        }
    
class story:
    fullstory:list = []
    choices:list = []
    errors:list = []
    
    def to_dict(self):
        return {
            'fullstory' : self.fullstory,
            'choices' : self.choices,
            'errors' : self.errors
        }