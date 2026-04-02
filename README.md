# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a content-based music recommendation system. Given a user's taste profile (preferred genre, mood, and energy level), the system scores every song in a dataset and returns the top recommendations ranked by relevance. It works like a simplified version of what Spotify or TikTok do behind the scenes.

---

## How The System Works

### Real-World Context
Streaming platforms like Spotify and YouTube use two main approaches:
- **Collaborative Filtering**: Recommends based on what similar users liked
- **Content-Based Filtering**: Recommends based on the song's own attributes like genre, mood, and energy

This project uses **content-based filtering**.

### Algorithm Recipe
Each `Song` has: `genre`, `mood`, `energy` (0.0–1.0), `tempo_bpm`
Each `UserProfile` has: `favorite_genre`, `favorite_mood`, `target_energy`

**Scoring Rule:**
| Feature | Points | Condition |
|---|---|---|
| Genre | +2.0 | Exact match |
| Mood | +1.0 | Exact match |
| Energy | 0.0–1.0 | 1.0 - abs(song.energy - user.target_energy) |

Maximum possible score: **4.0 points**

**Data Flow:**
Input (User Prefs) → Score every song → Sort by score → Output (Top 5 Recommendations)

### Potential Bias
This system may over-prioritize genre since a genre match alone is worth +2.0 — twice as much as mood. Songs in underrepresented genres will rarely surface unless the user asks for them.

---

## Getting Started

### Setup
1. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python -m src.main
```

### Running Tests
```bash
pytest
```

---

## Experiments You Tried

### Profile 1: High-Energy Pop Fan
- Settings: genre=pop, mood=happy, energy=0.85
- Top Result: Dynamite (BTS) — genre + mood match + high energy aligned perfectly
- Observation: All top 5 results were pop songs. Genre weight dominates strongly.

### Profile 2: Chill Hip-Hop Listener
- Settings: genre=hiphop, mood=chill, energy=0.40
- Top Result: Sunflower (Post Malone) — only hiphop/chill song, ranked first easily
- Observation: When genre and mood both match, the song tops the list regardless of energy.

### Profile 3: Intense Rock Lover
- Settings: genre=rock, mood=intense, energy=0.95
- Top Result: Enter Sandman (Metallica) — perfect genre, mood, and energy match
- Observation: Rock songs dominated. Classical songs scored near 0 for this profile.

### Weight Experiment
When I doubled the energy weight and halved the genre weight, low-energy classical songs climbed the rankings for low-energy profiles — showing how strongly weights shape results.

---

## Limitations and Risks

- Small catalog: Only 20 songs — real systems use millions
- No lyrics or language understanding
- Genre dominance creates filter bubbles — users rarely discover cross-genre songs
- No user history — the system treats every session identically
- Binary mood matching — no concept of similar moods

---

## Reflection

Building this recommender showed me how much a simple scoring formula shapes what a user sees. I was surprised that just by changing one weight, the entire ranking flipped. This mirrors real debates about Spotify's algorithm — it tends to lock users into what they already know.

Real music recommenders must balance accuracy (give users what they like) against discovery (show them something new). My system has no discovery mechanism at all.

See `model_card.md` for the full technical analysis.

