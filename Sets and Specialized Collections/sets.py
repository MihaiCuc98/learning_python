# ---------- Creating a set

# genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop',
# 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country',
# 'rock', 'classical', 'country', 'pop', 'rap', 'latin']


# survey_genres = set(genre_results)
# survey_abbreviated = {genre[0:3] for genre in survey_genres}
# print(survey_abbreviated)
# print(survey_genres)


# ---------- Creating a Frozenset

# top_genres = ['rap', 'rock', 'pop']
#
# # Write your code below!
# frozen_top_genres = frozenset(top_genres)
# print(frozen_top_genres)


# ---------- Adding to a Set

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

tag_set = set(song_data['Retro Words'])
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)
print(tag_set)
print(song_data)
song_data['Retro Words'] = tag_set
print(song_data)












