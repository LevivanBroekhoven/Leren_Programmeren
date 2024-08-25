import time, sys, os, json, string
from datetime import datetime
from termcolor import cprint
from data import player as playerdata
from data import route as routedata
from data import story as storydata

class story:
    roomorder:tuple
    player:playerdata
    route:routedata
    data:storydata
    start:str
    end:str

    def __init__(self, roomorder:tuple):
        self.roomorder = roomorder
        self.start = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.initData()

    def initData(self):
        self.player = playerdata()
        self.route = routedata()
        self.data = storydata()

    def print_title(self, text, color="magenta"):
        print('')
        cprint(text, attrs=["bold"], color=color)
    
    def get_step_title(self):
        return f'stap {string.ascii_uppercase[len(self.route.roomsvisted)]}'

    def write(self, msg, okAwnsers=[], attempts=0):
        if attempts > 1:
            self.write(f'Nog {attempts} pogingen over...')
        elif attempts == 1:
            self.write(f'Nog 1 poging over...')

        for char in msg:
            time.sleep(0.005)
            sys.stdout.write(char)
            sys.stdout.flush()

        if len(okAwnsers) > 0:
            awnser = input(" ").lower()
            self.data.choices.append(msg + " : " + awnser)

            if awnser not in okAwnsers and attempts != 1:
                self.write('Error, ongeldige invoer, probeer opnieuw!')

                if attempts == 0:
                    error = self.data.choices.pop()
                    self.data.fullstory.pop()
                    self.data.errors.append(error)
                else:
                    attempts = attempts - 1
                
                awnser = self.write(msg, okAwnsers, attempts)
            elif awnser not in okAwnsers and attempts == 1:
                self.write('Te veel incorrecte pogingen')
                awnser = False

            return awnser
        else:
            self.data.fullstory.append(msg)
            time.sleep(0.2)
            sys.stdout.write("\n")
        
    def checkAnswerByOrder(self, index:int, answer:str):
        try:
            room_number = self.roomorder[index]
            return self.route.get_answer_by_roomnumber(room_number) == answer
        except IndexError as e:
            return False
    
    def executeByOrder(self, index:int):
        try:
            roomNumber = self.roomorder[index]
        except IndexError:
            roomNumber = '?'
            self.route.errors.append(f'{self.get_step_title()} : ROOMORDER index {index} not found')
            
        import dungeon
        rooms = dungeon.rooms(self, self.player, self.route)
        answer = rooms.executeByNumber(roomNumber)
        
        self.route.add_to_route(str(roomNumber))
        self.route.add_to_answers(answer)

    def finish(self):
        import dungeon
        result = 'failed'
        self.end = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        self.print_title('Resultaat')
        if self.route.roomanswers.count(dungeon.rooms.DEFAULT_ROOM_ANSWER) > 0:
            self.write('Je bent ergens waar je niet verwacht te zijn.')
            self.write('Je bent verdwaald geraakt in de dungeon.')
            result = 'lost'
        elif self.route.get_last_answer() == False:
            self.write(f'Je hebt de juiste deurcode niet ingevoerd en gefaald om de uitgang te bereiken.')
        elif self.route.get_last_answer() == dungeon.rooms.DIE_IN_ROOM_ANSWER:
            self.write(f'Je bent omgekomen in kamer {self.route.get_last_room()}.')
            result = 'unsafe'
        elif self.route.get_last_answer() == '?':
            self.write('Besluiteloos blijf je zitten waar je bent.')
            self.write('Je denkt minutenlang na over welke kant je op moet gaan.')
            self.write('De minuten veranderen in uren en de uren in een dag.')
            self.write('Plotseling hoor je gerommel boven je...')
            self.write('Een touwladder verschijnt door het gat waar je eerder naar beneden viel.')
            self.write('Je klimt snel omhoog en verlaat de dungeon ongedeerd, maar niet wijzer.')
            result = 'rescued'
        elif self.route.get_last_answer().isnumeric():
            self.write('Je bent succesvol ontsnapt uit de dungeon.')
            result = 'escaped'
        elif len(self.roomorder) != 10 or len(set(self.roomorder)) != 10:
            self.write('Je bent best wel sneaky, je probeert vals te spelen.')
        else:
            self.write('Waarom toets je in het geheim de code in?')
            self.write('Zo kunnen we niet zien of je weet wat je aan het testen bent!')
            result = 'cheated'

        return result

    def proccess_attempt(self, dungeon_result:str):
        filename = datetime.now().strftime("%Y%m%d_%H%M%S")
        attempt_type = ''
        if dungeon_result in ['escaped', 'unsafe']:
            filename = dungeon_result+'_route_'+self.route.get_code()
            attempt_type = 'succesfull'
            succes_type = 'unsafe' if dungeon_result == 'unsafe' else 'save'
            self.print_title(f'Succesfull {succes_type} route found', "green")
        elif dungeon_result in ['cheated', 'rescued']:
            self.print_title('Secret attempt recorded', "yellow")
            attempt_type = 'secret'
        else:
            self.print_title('Failed attempt saved', "red")
            attempt_type = 'failed'

        self.save_result(filename, attempt_type)


    def save_result(self, filename, attempt_type):
        result_dir_name = 'attempts'
        
        if not os.path.exists(result_dir_name):
            os.makedirs(result_dir_name)

        if not os.path.exists(result_dir_name+'/'+attempt_type):
            os.makedirs(result_dir_name+'/'+attempt_type)

        filepath = result_dir_name+'/'+attempt_type+"/"+filename+".json"

        if os.path.exists(filepath):
            cprint(f'File "{result_dir_name}/{attempt_type}/{filename}.json" already exists', "yellow")
            return False

        f = open(filepath, "a")
        f.write(json.dumps(self.get_full_data(), indent=4))
        f.close()

        cprint(f'File "{result_dir_name}/{attempt_type}/{filename}.json" saved', "green")
        return True
    
    def to_dict(self):
        return {
            'roomorder' : ','.join(self.roomorder),
            'start' : self.start,
            'end' : self.end
        }
    
    def get_full_data(self):
        full_dict = self.to_dict() 
        full_dict['data'] = {}
        full_dict['data']['player'] = self.player.to_dict()
        full_dict['data']['route'] = self.route.to_dict()
        full_dict['data']['story'] = self.data.to_dict()

        return full_dict