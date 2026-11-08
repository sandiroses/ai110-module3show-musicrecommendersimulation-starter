import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


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
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for the user."""
        prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
        }
        scored = []
        for song in self.songs:
            score, reasons = score_song(prefs, song.__dict__)
            scored.append((song, score))
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, score in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended."""
        prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
        }
        score, reasons = score_song(prefs, song.__dict__)
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # turn number columns into numbers so we can do math with them
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # +2.0 points if the genre matches
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # +1.0 point if the mood matches
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # energy: the closer to the target, the more points (max 1.0)
    energy_points = 1 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    # sorted() gives a new list, highest score first
    scored_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return scored_songs[:k]