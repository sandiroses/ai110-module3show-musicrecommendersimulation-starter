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
Loaded songs: 18

Top recommendations:

Sunrise City - Score: 3.98
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.98)

Gym Hero - Score: 2.87
Because: genre match (+2.0), energy closeness (+0.87)

Summer Streets - Score: 2.00
Because: mood match (+1.0), energy closeness (+1.00)

Rooftop Lights - Score: 1.96
Because: mood match (+1.0), energy closeness (+0.96)

Bassline Riot - Score: 0.95
Because: energy closeness (+0.95)
```

---

## Profile Test Results

```
Loaded songs: 18

=== High-Energy Pop ===

Sunrise City - Score: 3.97
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.97)

Gym Hero - Score: 2.92
Because: genre match (+2.0), energy closeness (+0.92)

Summer Streets - Score: 1.95
Because: mood match (+1.0), energy closeness (+0.95)

Rooftop Lights - Score: 1.91
Because: mood match (+1.0), energy closeness (+0.91)

Bassline Riot - Score: 1.00
Because: energy closeness (+1.00)


=== Chill Lofi ===

Library Rain - Score: 4.00
Because: genre match (+2.0), mood match (+1.0), energy closeness (+1.00)

Midnight Coding - Score: 3.93
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.93)

Focus Flow - Score: 2.95
Because: genre match (+2.0), energy closeness (+0.95)

Spacewalk Thoughts - Score: 1.93
Because: mood match (+1.0), energy closeness (+0.93)

Coffee Shop Stories - Score: 0.98
Because: energy closeness (+0.98)


=== Deep Intense Rock ===

Storm Runner - Score: 3.99
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.99)

Gym Hero - Score: 1.99
Because: mood match (+1.0), energy closeness (+0.99)

Festival Fever - Score: 0.97
Because: energy closeness (+0.97)

Iron Cathedral - Score: 0.95
Because: energy closeness (+0.95)

Bassline Riot - Score: 0.93
Because: energy closeness (+0.93)


=== Edge Case: High Energy + Sad ===

Sunday Porch - Score: 3.40
Because: genre match (+2.0), mood match (+1.0), energy closeness (+0.40)

Storm Runner - Score: 0.99
Because: energy closeness (+0.99)

Gym Hero - Score: 0.97
Because: energy closeness (+0.97)

Festival Fever - Score: 0.95
Because: energy closeness (+0.95)

Bassline Riot - Score: 0.95
Because: energy closeness (+0.95)
```

---

## Experiments You Tried

**Experiment: weight shift.** I cut the genre points from +2.0 to +1.0 and doubled the energy points (up to +2.0), then ran all 4 profiles again.

What changed:
- **High-Energy Pop:** "Summer Streets" (reggaeton, happy) moved from #3 to #2, and "Gym Hero" dropped from #2 to #3. Gym Hero only matched on genre and energy. Summer Streets matched on mood and energy, so once genre was worth less it moved ahead.
- **Chill Lofi and Deep Intense Rock:** the top 5 stayed in the same order. Their best songs matched on everything, so the weights didn't matter.
- **Edge Case (High Energy + Sad):** "Sunday Porch" was still #1, but its score dropped from 3.40 to 2.80. The other four were still just loud songs that aren't sad.

Result: the change made the recommendations different, not more accurate. "Summer Streets" isn't really a better pick for a pop fan than "Gym Hero," it just moved up because energy now counts more.

Pop profile with the new weights:

```
Sunrise City - Score: 3.94
Because: genre match (+1.0), mood match (+1.0), energy closeness (+1.94)

Summer Streets - Score: 2.90
Because: mood match (+1.0), energy closeness (+1.90)

Gym Hero - Score: 2.84
Because: genre match (+1.0), energy closeness (+1.84)

Rooftop Lights - Score: 2.82
Because: mood match (+1.0), energy closeness (+1.82)

Bassline Riot - Score: 2.00
Because: energy closeness (+2.00)
```

---

## Limitations and Risks

(to fill in)

---

## Reflection

See [**Model Card**](model_card.md).

(to fill in)