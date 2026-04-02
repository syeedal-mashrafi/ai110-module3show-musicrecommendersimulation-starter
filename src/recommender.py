from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        """Initialize with a list of Song objects."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Recommend top-k songs for the user by scoring each song.
        Returns a list of Song objects sorted by score descending.
        """
        scored = []
        for song in self.songs:
            score, _ = self._score(user, song)
            scored.append((song, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """
        Return a plain-language explanation of why a song was recommended.
        """
        _, reasons = self._score(user, song)
        return " | ".join(reasons) if reasons else "No strong match found."

    def _score(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Internal scoring logic shared by recommend and explain."""
        score = 0.0
        reasons = []

        # Genre match: +2.0
        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append("genre match (+2.0)")

        # Mood match: +1.0
        if song.mood == user.favorite_mood:
            score += 1.0
            reasons.append("mood match (+1.0)")

        # Energy similarity: up to +1.0
        energy_score = round(1.0 - abs(song.energy - user.target_energy), 2)
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score})")

        # Acoustic bonus: +0.5 if user likes acoustic and song is acoustic
        if user.likes_acoustic and song.acousticness >= 0.6:
            score += 0.5
            reasons.append("acoustic match (+0.5)")

        return round(score, 2), reasons


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    Returns a list of dictionaries (one per row).
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
            }
            songs.append(song)
    return songs


def recommend_songs(
    user_prefs: Dict, songs: List[Dict], k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Args:
        user_prefs: dict with keys genre, mood, energy
        songs: list of song dicts from load_songs()
        k: number of top results to return

    Returns:
        List of (song_dict, score, explanation) tuples
    """
    scored = []
    for song in songs:
        score = 0.0
        reasons = []

        if song["genre"] == user_prefs.get("genre"):
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song["mood"] == user_prefs.get("mood"):
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_score = round(
            1.0 - abs(song["energy"] - user_prefs.get("energy", 0.5)), 2
        )
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score})")

        explanation = " | ".join(reasons)
        scored.append((song, round(score, 2), explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
