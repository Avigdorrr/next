# i use macos and this module dosent work here so i cant check if its working
import winsound
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
split_notes = notes.split('-')
iter_notes = iter(split_notes)
while True:
    try:
        note = next(iter_notes)
        freq, duration = note.split(',')
        winsound.Beep(freqs[freq], duration)
    except StopIteration:
        break