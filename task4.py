# 🎬 Sayli's Smart Movie Recommender System 🎥

print("Welcome to Sayli's Movie Recommendation Bot!")
print("Tell me your favorite genre (comedy, action, drama, horror, sci-fi, romance):")

# Genre-based movie list
movie_data = {
    "comedy": ["3 Idiots", "Phir Hera Pheri", "Hera Pheri", "Welcome", "Andaz Apna Apna"],
    "action": ["War", "Pathaan", "KGF", "Baaghi", "Dhoom"],
    "drama": ["Taare Zameen Par", "Swades", "Dear Zindagi", "Udaan"],
    "horror": ["Stree", "Tumbbad", "Bhool Bhulaiyaa", "Bhoot", "Pari"],
    "sci-fi": ["Robot", "Krrish", "Ra.One", "PK", "Interstellar"],
    "romance": ["Dilwale Dulhania Le Jayenge", "Aashiqui 2", "Barfi", "Tamasha", "Yeh Jawaani Hai Deewani", "Sanam teri kasam","Tere Naam","saiyyara"]
}

genre = input("🎯 Enter your choice: ").strip().lower()

if genre in movie_data:
    print(f"\n🎬 Recommended {genre.title()} movies for you:")
    for movie in movie_data[genre]:
        print(" -", movie)
else:
    print("❌ Sorry! I don't have recommendations for that genre right now.")
 