N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.index = PITCHES.index(note)
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[self.index]
        return self.note

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __lt__(self, other):
        return self.index < other.index

    def __le__(self, other):
        return self.index <= other.index

    def __gt__(self, other):
        return self.index > other.index

    def __ge__(self, other):
        return self.index >= other.index

    def __lshift__(self, other):
        if self.index - other < 0:
            raise ValueError("Note cannot be shifted below the octave range.")
        return Note(PITCHES[(self.index - other) % N], self.is_long)

    def __rshift__(self, other):
        if self.index + other >= N:
            raise ValueError("Note cannot be shifted above the octave range.")
        return Note(PITCHES[(self.index + other) % N], self.is_long)


class Melody:
    def __init__(self, notes=None):
        self.notes = notes if notes else []

    def __str__(self):
        if not self.notes:
            return ""
        return ", ".join(
            str(note).capitalize() if i == 0 else str(note) for i, note in enumerate(self.notes)
        )

    def append(self, note):
        self.notes.append(note)

    def replace_last(self, note):
        if self.notes:
            self.notes[-1] = note

    def remove_last(self):
        if self.notes:
            self.notes.pop()

    def clear(self):
        self.notes.clear()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, shift):
        try:
            transposed_notes = [note >> shift for note in self.notes]
            return Melody(transposed_notes)
        except ValueError:
            return Melody(self.notes.copy())

    def __lshift__(self, shift):
        try:
            transposed_notes = [note << shift for note in self.notes]
            return Melody(transposed_notes)
        except ValueError:
            return Melody(self.notes.copy())
