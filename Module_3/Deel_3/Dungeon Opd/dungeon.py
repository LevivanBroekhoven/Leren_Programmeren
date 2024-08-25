from data import player as playerdata
from data import route as routedata
from game import story as gamestory

class rooms:
    DEFAULT_ROOM_NUMBER = 0
    DEFAULT_ROOM_ANSWER = None
    DIE_IN_ROOM_ANSWER = 'x'

    story:gamestory
    player:playerdata
    route:routedata

    def __init__(self, story:gamestory, player:playerdata, route:routedata):
        self.story = story
        self.player = player
        self.route = route

    def executeByNumber(self, roomNumber:int):
        awnser = self.DEFAULT_ROOM_ANSWER

        try :
            self.story.print_title('Route: ' + self.story.get_step_title(), "cyan")
            roomFnc = getattr(self, f'room{roomNumber}')
            awnser = roomFnc()
        
        except AttributeError:
            awnser = self.DEFAULT_ROOM_ANSWER
            self.story.route.errors.append(f'{self.story.get_step_title()} : function room{roomNumber} not found')

        if awnser == None:
            self.story.write('...')

        return awnser

    def room1(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.get_previous_room() == False:
            self.story.write('Je herinnert je alleen nog de val door een diep gat, na een zware aardbeving.')
            self.story.write('Versuft sta je op.')
            self.story.write('Je ziet links van je een deur en rechts van je een gang met aan het einde een standbeeld.')
            answer = self.story.write('Neem je A) de deur links of B) de gang rechts?', ['a', 'b', '?'])

        return answer

    def room2(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.get_previous_room() == '8':
            self.story.write('Je komt uit de fontein en wringt het water uit je kleren.')
            self.story.write('Je kijkt op.')
        elif self.route.get_previous_room() in ['4', '6', '9']:
            self.story.write('Je loopt door het hek en het valt achter dicht.')

        if self.route.get_previous_room() in ['4', '6', '9', '8']:
            answer = '-'

            self.story.write('Voor een kolosale ijzeren deur zie je een wezen van onmetelijke kracht en grandeur: Een Draak...')
            if self.player.get_noice() > 1 or self.player.has_pickup('crystal'):
                if self.player.get_noice() > 1:
                    self.story.write('Zijn gigantische ogen zijn op jouw gericht, hij is klaarwakker.')
                else:
                    self.story.write('De Draak opent zijn ogen langzaam, alsof hij uit een diepe slaap ontwaakt.')

                if self.player.has_pickup('sword'):
                    self.story.write('Gewapend met je zwaard val je de draak aan.')
                    self.story.write('Verrast door je aanval en je kleine postuur heeft de draak geen schijn van kans.')
                    self.story.write('Je trekt je zwaard uit de draak en een er zit een sleutel aan je zwaard die de draak waarschijnlijk ingeslikt had.')
                elif self.player.has_pickup('crystal'):
                    answer = self.DIE_IN_ROOM_ANSWER
                    self.story.write('"Wie ben jij om mijn kristallen te stelen", zegt de draak met een luide stem.')
                    self.story.write('De draak haalt zijn kop naar achteren en spuwt een vuurzee op je af.')
                elif self.player.has_pickup('shield'):
                    self.story.write('De draak springt op je af en probeert je met 1 op op te slokken.')
                    self.story.write('Je aarzelt geen moment en houd je schild tussen jou en de draak.')
                    self.story.write('Het schild blijkt sterker dan je had gedacht en houd de beet van de draak tegen.')
                    self.story.write('Het is zelfs zo sterk dat het vast blijft zitten in zijn bek.')
                    self.story.write('Voor je neus, aan een gouden koort, aan de nek van de draak, bungelt een sleutel, je grijpt het.')
                else:
                    answer = self.DIE_IN_ROOM_ANSWER
                    self.story.write('Je staat hulpeloos tegenover de draak, zonder enige bescherming of wapens.')
                    self.story.write('Met een snelle beweging grijpt de draak je vast, tilt je van de grond en veslint je in 1 hap.')

            else:
                self.story.write('De draak ligt rustig te slapen, zijn machtige flanken rijzen gelijkmatig op en neer met zijn ademhaling.')
                self.story.write('Je ziet een sleutel om zijn nek zitten, die zal wel voor die grote ijzeren deur zijn.')
                self.story.write('Voorzichtig sluip je richting het beest en rijkt naar de sleutel.')

                if self.player.has_pickup('shield'):
                    answer = self.DIE_IN_ROOM_ANSWER
                    self.story.write('Het schild, dat op je rug vast zat, valt op de grond en de draak die zo vredig lag te slapen opend zijn ogen.')
                    self.story.write('Met een vloeiende beweging slokt de draak je in 1 keer op.')
                else:
                    self.story.write('Met veel beleid pak je de sleutel van de nek van de draak.')

            if answer == '-':
                self.story.write('Met de sleutel in je hand snel je je naar de grote ijzeren deur.')
                self.story.write('Hij past perfect en je opent de deur soepel.')
                self.story.write('Je stapt de deur door.')

        return answer

    def room3(self):
        answer = self.DEFAULT_ROOM_ANSWER
            
        if self.route.get_previous_room() == '8':
            answer = 'b'
            self.story.write('Je laat de fontein achter je voor wat het is en loopt verder.')
            self.story.write('Je komt langs een uitstulping in de muur waar een schatkist staat.')

            if self.story.write('Maak je de schatkist open? (Y/N)', ['y', 'n']) == 'y':
                self.story.write('Je ziet een zwaard in de kist liggen.')
                if self.story.write('Neem je het zwaard mee? (Y/N)', ['y', 'n']) == 'y':
                    self.story.write('Je pakt het zwaard op, het voelt goed in je handen.')
                    self.player.add_pickup('sword')
                else:
                    self.story.write('Je laat het zwaard in de kist liggen en loopt verder.')
            else:
                self.story.write('Dapper volg je de gang verder de dungeon in.')
                
            if not self.player.has_pickup('sword') and not self.player.has_pickup('shield'):
                self.story.write('Een donkere stem klinkt vanuit het niets en zegt,')
                self.story.write('"Bedankt voor het laten liggen van mijn schild en zwaard."')
                self.story.write('"Als beloning geef ik je deze versnelde route..."')
                self.story.write('Naast je begint de muur te verschuiven en een kleine kamer met daarin een rood punt komt tevoorschijn...')
                self.story.write('"Ga daar naar beneden", zegt de stem "en vind je weg naar je vrijheid"')
                answer = self.story.write('Wat doe je? A) Neem de versnelde route B) loop er aan voorbij', ['a', 'b'])

                if answer == 'b':
                    self.story.write('Je loopt de versnelde route voorbij.')
                else:
                    self.story.write('Je tilt de putdeksel open en klimt naar beneden.')
                    self.story.write('Beneden aangekomen zie je dat je maar 1 kant op kunt.')
                    self.story.write('Je vervolgt je route door de gang.')

                    if self.player.get_noice() > 1:
                        self.story.write('Halverwege hoor je boven je flink gestommel en gegrom.')
                    else:
                        self.story.write('De gang vult zich met een zacht gebrom dat op gesnurk lijkt.')

        return answer

    def room4(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.get_previous_room() == '1':
            self.story.write('Je opent de deur en stapt er doorheen.')
            self.story.write('Tot je verbazing laat je de deur los.')
            self.story.write('De deur valt achter je in het slot en lijkt niet meer open te kunnen.')
        elif self.route.get_previous_room() == '7':
            self.story.write('Je baant je een weg door een smalle, slingerende gang.')
            self.story.write('Je komt bij een muur met een afdruk van een hand erop.')
            self.story.write('Je legt je hand erop...')
            self.story.write('De muur voor je schuift als een deur open en je stapt erdoorheen.')
            self.story.write('Je ziet dat je uit een geheime deur in de vorm van een boekenkast bent gestapt.')
            self.story.write('De boekenkast gaat langzaam dicht.')
            self.story.write('Schuin voor je zie je een echte deur.')
            self.story.write('Je probeert hem te openen, maar hij zit op slot.')
            self.story.write('Je kijkt om je heen.')
        
        if self.route.get_previous_room() in ['1', '7']:
            self.story.write('Je staat in een kamer met allemaal boekenkasten en een grote tafel in het midden.')
            self.story.write('Je ziet 2 trappen aan het einde van de kamer.')
            self.story.write('Een trap naar beneden en een trap naar boven.')
            answer = self.story.write('Welke trap neem je? A) links die naar boven gaat of B) rechtdoor die naar beneden gaat?', ['a', 'b'])

            if answer == 'a':
                self.story.write('Je loopt de trap en ziet een grote kamer voor je afgesloten met een hek.')
                self.story.write('Je rammelt wat aan het hek en het schiet open.')

        return answer

    def room5(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.get_previous_room() == '7':
            self.story.write('Je stapt een grote hal gevuld met rijen kolossale pilaren.')
            self.story.write('Het schamele licht van flikkerende fakkels voorspelt niets goeds.')
            self.story.write('Een muffe vochtige geur hangt in de lucht, vermengd met een vage geur van bedorven voedsel.')
            self.story.write('Tussen de pilaren zie je een grote schim bewegen.')
            self.story.write('Je stapt voorzichtig verder de ruimte in.')
            self.story.write('Plots schrik je op van een hard gegrom achter je.')
            self.story.write('Je kijkt om en achter je staat een enorme trol die zijn knuppel naar achterwaarts beweegt om je te slaan.')
            answer = self.story.write('Wat doe je? A) Rennen of B) Bukken?', ['a', 'b'])

            if answer == 'b':
                self.story.write('Je bukt net op tijd en een van de pilaren krijgt het voor zijn kiezen.')
                self.story.write('Een groot brokstuk vliegt de hal door en maakt een gat in de muur.')
                self.story.write('De pilaar stort in op het hoofd van de trol, die alleen maar bozer wordt.')
                self.story.write('Even neem je de tijd om om je heen te kijken en zie je 2 opties.')
                self.story.write('Een gang verderop of door het zojuist ontstane gat.')
                answer = self.story.write('Wat doe je? A) Naar de gang of B) Door het gat?', ['a', 'b'])

                direction = 'de gang' if answer == 'a' else 'het gat'
                self.story.write(f'Je staat op en trekt een sprintje naar {direction}.')
            else:
                self.story.write('Je rent de eerste de beste afslag in die je ziet.')

        return answer


    def room6(self):
        answer = self.DEFAULT_ROOM_ANSWER
        sharts = False
        crystat_type = ''
        
        if self.route.get_previous_room() == '3':
            self.story.write('Je stapt een volgende kamer binnen.')
        elif self.route.get_previous_room() == '9':
            self.story.write('Je baant je een weg met je pickhouweel door de smalle gang die schuin naar boven gaat.')
            self.story.write('Klimmend, klauterend en met gebruik van je nieuwe tool vind je je weg naar boven.')
            self.story.write('Boven aangekomen stuit je op een muur van klimop en licht gloeiende objecten.')
            self.story.write('Met een grote zwaai sla je er een weg doorheen en hoort iets vallen op de grond.')
            self.story.write('Je stapt een kamer binnen.')
            self.player.add_noice()
            sharts = True
            crystat_type = 'een'

        if self.route.get_previous_room() in ['3', '9']:
            answer = 'b'

            self.story.write('De kamer is verlicht door een zacht gloeiend schijnsel dat wordt uitgezonden door tientallen paarse en roze glinsterende kristallen.')
            self.story.write('De muren zijn ruw en bedekt met klimop, maar tussen de weelderige begroeiing fonkelen de kristallen helder, als kleine juwelen in de duisternis.')
            self.story.write('Ondanks de vredige uitstraling van de kamer, voelt het als een plaats van rust en bezinning te midden van de grimmige sfeer van de dungeon.')

            if self.player.has_pickup('sword'):
                if self.story.write('Wil je een kristal los maken met je zwaard (Y/N)?', ['y', 'n']) == 'y':
                    self.story.write('Met je zwaard peuter je een kristal los van de muur en het springt van de muur.')
                    sharts = True
                    crystat_type = 'het losgemaakte'

            if sharts:
                self.story.write(f'Op de grond ligt {crystat_type} paarse kristal.')
                if self.story.write('Wil je het kristal oppakken (Y/N)?', ['y', 'n']) == 'y':
                    self.player.add_pickup('crystal')
                    self.story.write('Je pakt het kristal op en stopt het in je zak.')

            self.story.write('Vanuit je ooghoek zie je een standbeeld in de hoek van de kamer, met daarnaast een doorgang met een hek.')
            
            if self.player.has_pickup('shield'):
                self.story.write('Het standbeeld lijkt als twee druppels water op het standbeeld dat je eerder bent tegengekomen.')
                self.story.write('Alleen heeft deze geen schild vast.')

                if self.story.write('Wil je je schild bij het standbeeld plaatsen? (Y/N)', ['y', 'n']) == 'y':
                    self.player.remove_pickup('shield')
                    self.story.write('Je plaatst je schild bij het standbeeld.')
                    self.story.write('Een donkere stem spreekt in je hoofd.')
                    self.story.write('"Bedankt voor het terugbrengen van mijn schild."')
                    self.story.write('"Ik beloon je met een verkorte route."')
                    self.story.write('Het standbeeld begint opzij te schuiven en laat een donkere gang zien.')
                    self.story.write('"Let op, deze gang kan gevaarlijk zijn."')
                    answer = self.story.write('Wat doe je? A) Neem de verkorte route of B) doorlopen', ['a', 'b'])

                    if answer == 'a':
                        self.story.write('Je stapt de donkere gang binnen.')
                        self.story.write('Spinnenwebben vouwen over je gezicht terwijl je verder gaat.')
                        self.story.write('De gang wordt donkerder en donkerder.')
                        self.story.write('Voor je zie je een vaag groen licht.')
                        if self.player.has_pickup('crystal'):
                            self.story.write('Je broekzak begint lichtjes te trillen.')
                            self.story.write('Je haalt het kristal uit je broekzak.')
                            self.story.write('De gloed van het kristal vult de ruimte, en dat is maar goed ook.')
                            self.story.write('Voor je zie je een gat in de grond.')
                            self.story.write('Met gemak spring je over het gat heen en na een kort stukje lopen kom je bij het licht aan.')
                            self.story.write('Je hand gaat over het licht, en de muur schuift open.')
                            self.story.write('Je stapt door de opening.')
                        else:
                            self.story.write('Plotseling voel je de grond onder je verdwijnen.')
                            self.story.write('Je valt en verdwijnt in de diepte.')
                            answer = self.DIE_IN_ROOM_ANSWER
                
                if answer == 'b':
                    self.story.write('Je loopt richting het hek, opent het.')

        return answer


    def room7(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.get_previous_room() == '1':
            self.player.add_noice()

            self.story.write('Je stapt de gang binnen en opnieuw begint de grond te schudden.')
            self.story.write('Je rent zo hard als je kunt door de lange gang richting het standbeeld terwijl de gang achter je instort.')
            self.story.write('Zodra je bij het einde van de gang komt en bij het standbeeld staat, stopt de grond met schudden.')
            self.story.write('Je kijkt achterom en ziet de gang volledig ingestort.')
            self.story.write('Voor je staat een standbeeld, met in zijn handen een schild.')

            if self.story.write('Wil je het schild meenemen? (Y/N)', ['y', 'n']) == 'y':
                self.story.write('Je pakt het schild van het standbeeld, het voelt licht en handzaam.')
                self.player.add_pickup('shield')
            else:
                self.story.write('Je laat het schild en standbeeld voor wat het is.')
            
            self.story.write('Nu je nog eens goed om je heen kijkt, zie je dat de gang links steeds breder wordt en de gang rechts smaller.')
            answer = self.story.write('Neem je de gang A) links of B) rechts?', ['a', 'b'])
        
        return answer

    def room8(self):
        answer = self.DEFAULT_ROOM_ANSWER
        
        if self.route.get_previous_room() == '5':
            self.story.write('Je duikt door het gat heen en kruipt tegen de verre muur.')
            self.story.write('De arm van de trol komt door het gat heen maar kan je net niet grijpen.')
            self.story.write('Na een paar keer proberen geeft hij het op en druipt, blazend uit zijn neus, af.')
            self.story.write('Je oog valt op een fontein in deze kamer.')
            self.story.write('Je kruipt er naartoe en begint jezelf te wassen.')
            self.story.write('Het water is helder en verfrissend, en nu je beter kijkt, zweer je dat je een doorgang onderin het bassin ziet.')

            answer = self.story.write('Wat doe je? A) Laten voor wat het is of B) Zwemmen?', ['a', 'b'])

            if answer == 'b':
                self.story.write('Je neemt een grote hap lucht en duikt het water in.')
                self.story.write('Je wordt meegenomen door een stevige stroming.')

        return answer


    def room9(self):
        answer = self.DEFAULT_ROOM_ANSWER
        lowerlevel = False
        
        if self.route.get_previous_room() == '4':
            self.story.write('Je stapt de trap op naar beneden.')
            self.story.write('Tot dusver loopt alles gesmeerd, denk je bij jezelf.')
            self.story.write('Bij de derde trede hoor je een onheilspellende klik.')
            self.story.write('Achter je valt er een rotsblok uit het plafond op de trap en rolt jouw kant op.')
            self.story.write('Je rent zo hard je kunt naar beneden en net voor dat het rotsblok je zou raken spring je door een deur opening.')
            self.story.write('Je kijkt achter je en ziet dat het rotsblok is blijven steken.')
            self.story.write('Voor nu is de kust weer even veilig.')
            lowerlevel = True
        elif self.route.get_previous_room() == '5':
            self.story.write('Plots sta je voor een houte loopbrug met de trol op je hielen.')
            self.story.write('Je probeert voorzichtig te doen maar je enige optie is nu om door te lopen.')
            answer = 'a'

            if self.player.has_pickup('shield'):
                self.story.write('Dan herinner je het schild dat je zojuist hebt opgepakt.')
                answer = self.story.write('Wat doe je? A) toch de brug over of B) Verdedigen?', ['a', 'b'])
                if answer == 'b':
                    lowerlevel = True
                    self.story.write('Je houd je schild voor je terwijl de trol op je af komt rennen.')
                    self.story.write('Hij heeft telaat door dat jij en de verdediging zit en struikelt over je.')
                    self.story.write('De impact van de trol brengt je uit balans en samen vallen jullie naar beneden.')
                    self.story.write('Hij aan de rechterkant van de brug en jij aan de linkerkant.')
                    self.story.write('Het wordt donker voor je ogen.')
                    self.story.write('Versuft word je wakker op de grond.')
                    self.story.write('Je kijkt om je heen en ziet dat de trol bewusteloos vast zit in een deuropening.')
                    self.story.write('Je kijkt omhoog.')
                else:
                    self.story.write('Die trol is wel erg groot en je besluit het schild niet te gebruiken.')
                
        if lowerlevel:
            self.story.write('Helaas is er geen weg terug.')
            self.story.write('Dus je begint de kamer te onderzoeken.')
            self.story.write('Aan 1 van de muren vindt je een kleine opening in de muur met een hendel er naast.')
            self.story.write('De hendel staat in de middelste positie en vraagt er om bewogen te worden.')
            answer = self.story.write('Welke kant duw je de hendel op? A) Omhoog | B) Naar beneden?', ['a', 'b'])
            
            if answer == 'b':
                self.player.add_pickup('lever')
                self.story.write('Je trek de hendel naar benenden en hij breekt af.')
                self.story.write('Een scherpe kant laat zich zien aan de andere kant van de hendel.')
                self.story.write('Dit zou wel eens een goede pickhouweel kunnen zijn om dat gat groter te maken...')
                self.story.write('Ijverig begin je te hakken op het gat net zolang totdat het groot genoeg is om doorheen te kruipen')
            else:
                self.story.write('Je duwt de hendel naar boven en je hoort wat gepiep en gekraak.')
                self.story.write('Je kijkt omhoog en vanuit het donker komt langzaam een trap naar beneden.')
                self.story.write('De trap land met 1 kant op de grond en gaat naar boven aan de andere kant.')
                self.story.write('Aan de constructie kun je zien dat dit een brug geweest moet zijn.')
        else:
            self.story.write('Je rent over de brug met de trol op je hielen.')
            self.story.write('De houte loopbrug kraakt en beweegt heftig.')
            self.story.write('Net voor je bij het einde bent voel je de brug breken achter je.')
            self.story.write('Zonder twijfel neem je een sprong en komt aan de overkant op solide aarde terecht.')
            self.story.write('Je kunt nog net zien hoe de trol met brug en al de diepte in valt en je hoort een harde plof.')
            self.story.write('Je staat op en stoft jezelf af.')
            self.story.write('Je ziet voor je een open hek.')
            self.player.add_noice()

        return answer

    def room10(self):
        answer = self.DEFAULT_ROOM_ANSWER

        if self.route.roomanswers.count(self.DEFAULT_ROOM_ANSWER) == 0:
            if self.route.get_previous_room() == '2':
                self.story.write('Achter je slaat de deur dicht.')
                self.story.write('Recht voor je zie je een trap naar boven.')
            elif self.route.get_previous_room() == '3':
                self.story.write('Je vervolgt je weg door de gang en komt bij een eindpunt.')
                self.story.write('Je kijkt omhoog en ziet een andere deksel van zo een zelfde put.')
                self.story.write('Je klimt er naartoe, opent deze en klimt er uit.')
                self.story.write('Je staat voor een trap die naar boven gaat.')
            elif self.route.get_previous_room() == '6':
                self.story.write('Je bevindt je in een gang met aan de linkerkant een grote gesloten deur en aan de rechterkant een kamer met een trap naar boven.')

            if self.route.get_previous_room() in ['2', '3', '6']:
                doorcode = self.route.get_doorcode()
                codelen = len(str(doorcode))

                self.story.write('Dat moet de uitgang zijn, denk je bij jezelf.')    
                self.story.write('Je loopt de ronde, ijzeren trap op.')
                self.story.write('Boven aan de trap kom je bij een dichte deur.')
                self.story.write('Naast de deur zit een plaat met de cijfers 1 t/m 9 en een beschrijving er onder.')
                self.story.write('De beschrijving luidt:')
                self.story.write('"Toets de route in die u heeft bewandeld om hier te geraken".')
                self.story.write(f'"U heeft 3 pogingen om de {codelen}-cijferige code correct in te voeren".')
                answer = self.story.write(f'Welke {codelen} cijfers voer je in?', [doorcode, '*'*codelen], 3)

                if answer != False:
                    self.story.write('Met een harde toon zwaait de deur open en je rent naar buiten.')
        
        return answer
