# 🎵 Music Recommender Simulation

## Project Summary

This is a small music recommender that runs in the terminal. It reads songs from a CSV file, scores each song against a user's taste profile, and prints the top 5 songs with the reasons for each score.

---

## How The System Works

Real apps like Spotify use collaborative filtering (what similar users liked) and content-based filtering (song features like genre and energy). My version only uses content-based filtering, since I don't have data about other users. It cares about genre most, then mood, then energy.

- **Song features:** genre, mood, energy, tempo_bpm, valence, danceability, acousticness (my scoring only uses genre, mood, and energy)
- **UserProfile:** favorite_genre, favorite_mood, target_energy, likes_acoustic (not used in scoring yet)

**Algorithm Recipe:**

- +2.0 points for a genre match
- +1.0 point for a mood match
- Up to +1.0 point for energy: `1 - |song energy - target energy|`

Every song gets a score, then the songs are sorted from highest to lowest and the top 5 are returned with their reasons.

**Expected bias:** genre is worth the most, so the system may ignore great songs from other genres that match the mood and energy.

---

## Getting Started

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate         # Windows
   source .venv/bin/activate      # Mac or Linux
   ```

2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python -m src.main`
4. Run tests: `python -m pytest`

---

## Sample Recommendation Output

Profile: favorite_genre = pop, favorite_mood = happy, target_energy = 0.8

```
Loaded songs: 10

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy closeness (+0.87)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy closeness (+0.96)

Night Drive Loop - Score: 0.95
Because: energy closeness (+0.95)

Storm Runner - Score: 0.89
Because: energy closeness (+0.89)
```

---

## Experiments You Tried

(to fill in)

---

## Limitations and Risks

(to fill in)

---

## Reflection

See [**Model Card**](model_card.md).

(to fill in)