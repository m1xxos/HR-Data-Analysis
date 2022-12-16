import pandas as pd

chart_dict = {"artist": {0: "The Weeknd", 1: "Dua Lipa", 2: "Roddy Ricch", 3: "Post Malone", 4: "Harry Styles", 5: "Tones And I", 6: "Future & Drake", 7: "Lewis Capaldi"}, "song": {0: "Blinding Lights", 1: "Don't Start Now", 2: "The Box", 3: "Circles", 4: "Adore You", 5: "Dance Monkey", 6: "Life Is Good", 7: "Before You Go"}, "peak_us": {0: 1, 1: 2, 2: 1, 3: 1, 4: 6, 5: 4, 6: 2, 7: 9}, "peak_uk": {0: "1", 1: "3", 2: "2", 3: "19", 4: "7", 5: "-", 6: "3", 7: "1"}, "peak_de": {0: "1", 1: "10", 2: "12", 3: "37", 4: "83", 5: "1", 6: "8", 7: "42"}, "peak_fr": {0: "1", 1: "12", 2: "7", 3: "77", 4: "126", 5: "3", 6: "33", 7: "49"}, "peak_ca": {0: 1, 1: 3, 2: 1, 3: 3, 4: 10, 5: 1, 6: 3, 7: 16}, "result_place": {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8}}

chart2020 = pd.DataFrame(chart_dict)

# your code here
print(chart2020[["artist", "song"]].tail(3))
