class Note:
    def __init__(self, note, is_long=False):
        if is_long is not True:
            self.note = note
        else:
            self.note = dic[note]
        self.index = PITCHES.index(note)
        self.long = is_long

    def __str__(self):
        if self.long is True:
            for k, v in dic.items():
                if v == self.note:
                    return self.note
        else:
            return self.note

    def __lt__(self, other):
        return self.index < other.index

    def __gt__(self, other):
        return self.index > other.index

    def __le__(self, other):
        return self.index <= other.index

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __ge__(self, other):
        return self.index >= other.index

    def __rshift__(self, other):
        return Note(PITCHES[(self.index + other) % 7], self.long)

    def __lshift__(self, other):
        return Note(PITCHES[(self.index - other) % 7], self.long)

    def get_interval(self, other):
        return INTERVALS[abs(self.index - other.index)]


class Melody:
    def __init__(self, note=''):
        self.melody = ''
        for elem in note:
            self.melody += str(elem) + ', '
        self.melody = self.melody.capitalize()

    def __str__(self):
        return self.melody[:-2]

    def __len__(self):
        if self.melody:
            return len(self.melody.split())
        return 0

    def append(self, elem):
        self.melody += str(elem) + ', '

    def replace_last(self, elem):
        self.melody = self.melody[:-2].split()[:-1]
        self.melody = ' '.join(self.melody)
        self.melody += ' ' + str(elem) + ', '

    def remove_last(self):
        self.melody = self.melody.split()[:-1]
        self.melody = ' '.join(self.melody)
        self.melody += ' '

    def clear(self):
        self.melody = '  '

    def __rshift__(self, other):
        spisok = ''
        for elem in self.melody.split():
            if self.melody.split().index(elem) + other > len(self.melody.split()) + 1:
                return self.melody
            else:
                spisok += self.melody.split()[self.melody.split().index(elem) + other] + ' '



dic = {'до': "до-о", 'ре': "ре-э", 'ми': "ми-и", 'фа': "фа-а", 'соль': "со-оль", 'ля': "ля-а",
           'си': "си-и"}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]

melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
# melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
#print('<< 1:', melody_down)
print(melody)
