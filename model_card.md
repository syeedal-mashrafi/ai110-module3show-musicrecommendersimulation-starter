# 🎧 Model Card — Music Recommender Simulation

## 1. Model Name
**VibeFinder 1.0** — A content-based music recommendation simulator.

---

## 2. Intended Use
- **What it does:** Suggests 3–5 songs from a small catalog based on a user's preferred genre, mood, and energy level.
- **Who it's for:** Students learning how recommendation systems work.
- **What it is NOT for:** Production use or real-time streaming.

---

## 3. How It Works (Short Explanation)

When a user provides their taste profile, the system looks at every song and calculates a match score:
- If a song's genre matches what the user wants, it gets +2 points
- If the mood also matches, it gets another +1 point
- The closer the song's energy is to the user's preferred energy, the more bonus points it earns (up to +1 point)

Once every song has a score, the system sorts them highest to lowest and returns the top results. There is no machine learning — it is purely a math-based rule system.

---

## 4. Data

- **Dataset:** `data/songs.csv` — 20 songs manually curated
- **Attributes per song:** title, artist, genre, mood, energy (0.0–1.0), tempo_bpm
- **Genres represented:** pop, hiphop, rock, classical, rnb
- **Moods represented:** happy, sad, chill, intense
- **Dataset skews toward:** mainstream Western music from 2010s–2020s

---

## 5. Strengths

- **Transparent:** Every recommendation comes with a plain-language explanation
- **Fast:** Scores all 20 songs instantly with no API calls
- **Predictable:** Same input always produces same output
- **Works well for clear preferences:** Strong genre preference surfaces best songs reliably

---

## 6. Limitations and Bias

- **Genre filter bubble:** Genre is worth +2.0 so users rarely see songs outside their preferred genre
- **Small dataset:** Only 20 songs means many profiles return the same top results
- **No collaborative signals:** Cannot discover that people who like X also like Y
- **Binary mood matching:** Sad and chill are treated as completely different
- **Genre imbalance:** Pop and hiphop have 5 songs each, R&B only has 2

---

## 7. Evaluation

I tested the system with three distinct user profiles:

| Profile | Top Result | Matched Expectation? |
|---|---|---|
| High-Energy Pop Fan | Dynamite (BTS) | Yes — genre + mood + high energy |
| Chill Hip-Hop Listener | Sunflower (Post Malone) | Yes — only hiphop/chill song |
| Intense Rock Lover | Enter Sandman (Metallica) | Yes — perfect all-around match |

I also tested an adversarial profile: genre=pop, mood=intense, energy=0.5. This revealed a weakness — no pop song has intense mood, so the recommender fell back to genre+energy matching only.

---

## 8. Future Work

- Add collaborative filtering by tracking which songs users with similar profiles chose
- Expand dataset to 100+ songs with more genre and mood diversity
- Add a diversity penalty so the same artist does not appear twice in top 5
- Replace binary mood matching with a mood similarity score
- Add tempo range matching so users who want fast songs are not shown slow ballads

---

## 9. Personal Reflection

This project changed how I think about recommendation algorithms. Even a simple rule-based system raises real fairness questions. By giving genre twice the weight of mood, I was deciding that what kind of music matters more than how you want to feel — and that is a human judgment embedded in code.

The most surprising moment was running the adversarial profile and realizing the system had no good answer. In a real app, this would mean the user gets bad recommendations and stops using the platform.
