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

# song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

# user_tag_1 = 'warm'
# user_tag_2 = 'exciting'
# user_tag_3 = 'electric'
#
# tag_set = set(song_data['Retro Words'])
# tag_set.add(user_tag_1)
# tag_set.add(user_tag_2)
# tag_set.add(user_tag_3)
# print(tag_set)
# print(song_data)
# song_data['Retro Words'] = tag_set
# print(song_data)


# ---------- Removing From a Set

# song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}
#
# tag_set = set('Retro Words')
# tag_set.remove('onion')
# tag_set.remove('helloworld')
# tag_set.remove('spam')
# song_data_users = {'Retro Words': tag_set}


# ---------- Finding Elements in a Set

# allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']
#
# song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}
# tag_set = set(song_data_users['Retro Words'])
# # Write your code below!
# bad_tags = []
# for i in tag_set:
#     if i not in allowed_tags:
#         bad_tags.append(i)
# for i in bad_tags:
#     tag_set.remove(i)
#
# song_data_users['Retro Words'] = tag_set
# print(song_data_users)


# ---------- Introduction to Set Operations

