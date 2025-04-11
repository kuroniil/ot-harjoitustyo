# Arkkitehtuuri

## Tulokset-näkymä

Alla oleva sekvenssikaavio kuvaa kuinka käyttäjän napin painalluksesta tallennetut tulokset päätyvät tietokannasta käyttäjälle.

```mermaid
    sequenceDiagram
    actor User
    participant UI
    participant Leaderboard
    participant Scores
    participant Score
    User->>UI: "Tulokset" button
    UI->>UI: show_view("leaderboard")
    UI->>Leaderboard: Leaderboard(root, ...)
    Leaderboard->>Leaderboard: get_scores()
    Leaderboard->>Scores: Scores(mode)
    Leaderboard->>Scores: get_all_scores()
    Scores->>Scores: scores_by_mode()
    Scores->>Scores: sort_scores()
    Scores->>Score: Score(*self.scores[i])
    Scores->>Leaderboard: complete_scores
```

## Luokkakaavio

Luokkakaavio kuvaa sovelluksen kahden keskeisen luokan yhteyttä.

```mermaid
    classDiagram
    GameLogic "1" -- "1" Grid
    class GameLogic {
        grid
        score
        game_over
    }
    class Grid {
        size
        .move
        .collisions
        .find_all_zeros
    }
```
