"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name: str, user_prefs: dict, results: list):
    """Print recommendations in a clean, readable format."""
    print(f"\n{'='*60}")
    print(f"  🎵 Recommendations for: {profile_name}")
    print(f"  Genre: {user_prefs['genre']} | Mood: {user_prefs['mood']} | Energy: {user_prefs['energy']}")
    print(f"{'='*60}")
    for i, (song, score, explanation) in enumerate(results, 1):
        print(f"  {i}. {song['title']} — {song['artist']}")
        print(f"     Score: {score:.2f} | Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # --- Profile 1: High-Energy Pop Fan ---
    pop_fan = {"genre": "pop", "mood": "happy", "energy": 0.85}
    results1 = recommend_songs(pop_fan, songs, k=5)
    print_recommendations("High-Energy Pop Fan", pop_fan, results1)

    # --- Profile 2: Chill Hip-Hop Listener ---
    chill_hiphop = {"genre": "hiphop", "mood": "chill", "energy": 0.4}
    results2 = recommend_songs(chill_hiphop, songs, k=5)
    print_recommendations("Chill Hip-Hop Listener", chill_hiphop, results2)

    # --- Profile 3: Intense Rock Lover ---
    rock_lover = {"genre": "rock", "mood": "intense", "energy": 0.95}
    results3 = recommend_songs(rock_lover, songs, k=5)
    print_recommendations("Intense Rock Lover", rock_lover, results3)


if __name__ == "__main__":
    main()
