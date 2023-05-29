class MusicNotes:

    def __init__(self):
        self._list_of_notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._index_octabs = 1
        self._index_note = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index_octabs == 5 and self._index_note >= len(self._list_of_notes) - 1:
            raise StopIteration

        elif self._index_note >= len(self._list_of_notes ) - 1:
            self._index_note = -1
            self._index_octabs += 1
        self._index_note += 1
        return self._list_of_notes[self._index_note] * (2 ** (self._index_octabs - 1))