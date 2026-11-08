# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder suggests songs from a small catalog based on a user's favorite genre, favorite mood, and target energy. It is for classroom exploration only. It assumes the user can describe their taste with one genre, one mood, and one energy number. It is not meant for real users or a real music app.

---

## 3. How the Model Works

The model gives every song a score, then shows the songs with the highest scores.

- If the song's genre matches the user's favorite genre, it gets 2 points.
- If the song's mood matches the user's favorite mood, it gets 1 point.
- For energy, the closer the song is to the user's target, the more points it gets, up to 1 point.

The best possible score is 4. The model also keeps a list of reasons for each score, so you can see why a song was picked. The starter code was empty, so I wrote all of the scoring logic myself using this recipe.

---

## 4. Data

The catalog has 18 songs. The starter file had 10, and I added 8 more. The genres include pop, lofi, rock, jazz, ambient, synthwave, indie pop, country, hip hop, R&B, metal, folk, EDM, classical, and reggaeton. The moods include happy, chill, intense, relaxed, moody, focused, nostalgic, confident, romantic, angry, sad, euphoric, and peaceful.

Most genres only have one song. Lofi has three, and pop has two. The data does not have lyrics, language, or artist popularity, so a lot of musical taste is missing.

---

## 5. Strengths

The system works well when the user's taste is clear and the catalog has several songs that fit it. The Chill Lofi profile gave three lofi songs at the top, and "Library Rain" got a perfect 4.00. The Deep Intense Rock profile put "Storm Runner" first. Both results matched my intuition. The reasons list also makes it easy to see why a song ranked where it did.

---

## 6. Limitations and Bias

The system only uses genre, mood, and energy. It ignores tempo, valence, danceability, and acousticness. Genre and mood must match exactly, so "indie pop" does not count as "pop," and "Rooftop Lights" missed the genre points for the pop profile. Genre is worth the most points, so a song that matches the genre can beat a song that fits the user's mood and energy better. For example, "Gym Hero" is an intense song, but it keeps showing up for pop users just because it is pop and has high energy. The catalog is also small. Rock only has one song, so after "Storm Runner" the rest of the rock list is just loud songs from other genres.

---

## 7. Evaluation

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge case with high energy but a sad mood. I looked at whether the top songs matched what I would expect for each profile.

Comparing the profiles:
- **Pop vs. Lofi:** Pop picked loud, danceable songs. Lofi picked quiet, slow songs. This makes sense because their target energy is very different (0.85 vs. 0.35).
- **Pop vs. Rock:** Both lists had "Gym Hero" near the top. It is high energy, so it fits both profiles, even though it is not really "happy."
- **Lofi vs. Rock:** These two lists were almost completely different, which is what I expected. One wants calm songs and the other wants intense ones.
- **Edge case vs. the others:** The edge case wanted high energy but a sad mood. The system gave "Sunday Porch," a quiet folk song, as the top pick. Matching genre and mood gave it more points than the energy gap took away. The rest of the list was just loud songs that are not sad.

What surprised me most was how often "Gym Hero" appeared. I also ran one experiment, where I cut the genre points to 1.0 and doubled the energy points. "Summer Streets" moved up above "Gym Hero" for the pop profile, but the other profiles stayed the same. The change made the results different, not more accurate.

---

## 8. Future Work

- Use more features, like valence, danceability, and acousticness. The user profile already has a `likes_acoustic` setting that the score does not use yet.
- Treat similar genres as close, so "indie pop" gets some credit for a pop fan.
- Add more songs so each genre has several, and make the top 5 less repetitive.
- Let users have more than one favorite genre or mood.

---

## 9. Personal Reflection

I learned that a recommender can feel smart even when it is just adding up a few points. Simple rules like "genre matches" and "energy is close" were enough to give results that made sense. The biggest surprise was "Gym Hero" showing up for pop and rock users. It showed me how one heavy rule, like genre, can shape the whole list.

I used an AI assistant to help explain errors. I still had to check its work. When I ran the app, I hit errors in the starter's `main.py`, and the profile keys had to match what my scoring code expected. I ran the tests myself (2 passed), compared the results to my own sense of what fits each profile, and restored the original weights after my experiment. I would not trust the output without running it.

Next I would add more features, like danceability and acousticness, and more songs. This also changed how I think about music apps. When an app keeps recommending the same kind of song, it may be because its rules weigh one thing too much, and a user with an unusual taste can get ignored.