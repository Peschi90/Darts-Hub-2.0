# Create your own Caller soundpacks

[Deutsch](CALLER_SOUNDPACKS.de.md) · [Using Caller](CALLER_CONFIGURATION_AND_LOCALIZATION.md)

This guide describes the sound names and triggers **currently used by Darts-Hub 2.0**. A soundpack contains audio files. The filename without its extension is the **key** used to find a recording: `180.wav` has the key `180`. Record in any language; the recording language is independent of the interface language.

## 1. Quick start: use a custom pack

1. Create a folder, for example `en-MyVoice`.
2. Put recordings **directly inside that folder**. Subfolders are not scanned.
3. Put the folder inside your configured soundpack root. Alternatively, set a custom **media path** in Caller as the root. This root contains individual pack folders, not the recordings themselves.
4. Refresh the library or reopen Caller. Local pack folders appear under their folder names. Select your pack as the voice and disable random voice selection (`RandomCaller = 0`) so it is not replaced at the next match.
5. Enable Caller and local playback, apply settings and test. After replacing files, select/apply the voice again or restart Darts-Hub to reload the file list.

The default root is inside the Darts-Hub data directory (normally `%LOCALAPPDATA%\DartsHub\soundpacks` on Windows). Your configured path takes precedence. Custom media paths must be absolute paths.

```text
C:\MySoundpacks\                 ← select as the media path in Caller
└── en-MyVoice\                   ← select as the voice
    ├── gameon.wav
    ├── matchon.wav
    ├── gameshot.wav
    ├── matchshot.wav
    ├── matchcancel.wav
    ├── busted.wav
    ├── 0.wav
    ├── 60.wav
    ├── 180.wav
    ├── player1.wav
    ├── player2.wav
    ├── you_require.wav
    ├── bulling_start.wav
    └── bulling_end.wav
```

This is a starter selection, not a complete set of scores. A manually created local folder needs **no JSON manifest or CSV mapping**. A ZIP file placed in the root is not loaded as a pack: share a ZIP containing your pack folder, ask recipients to extract it, and select it as described above. This does not automatically add it to the online download library.

### Formats and recordings

- The loader recognizes `.wav`, `.mp3`, `.ogg` and `.flac`. Actual playback also depends on the operating system's audio backend. **PCM WAV** is the simplest choice for custom packs across platforms; for example 44.1 kHz, 16 bit, mono or stereo. This is a recommendation, not a fixed loader requirement.
- On Linux, Darts-Hub uses `paplay`/`aplay` for WAV; other formats require a suitable player such as `ffplay`. See [Raspberry Pi / Linux audio](RASPBERRY_PI.md).
- Keep recordings short and remove leading/trailing silence. Caller waits for a recording to finish, so silence inside the file still delays subsequent announcements.
- Use one extension per key. Do not supply both `180.wav` and `180.mp3`: selection between them is not reliably defined.
- Keys are looked up case-insensitively. Still use the lowercase filenames shown here. Special characters must match the requested name exactly.
- Avoid Windows-reserved filenames such as `CON` or `AUX` for custom player names. Downloaded managed packs have an internal encoding for these names; ordinary custom packs do not need it.

### Random variants and shared recordings

**Any key** supports variants: `180.wav`, `180+1.wav`, `180+2.wav`. Each request randomly selects the base recording or a variant. The base file is optional: `180+1.wav` alone is sufficient. The `+` suffix must contain digits. `180_alt.wav` is not a variant of `180`.

The **shared media path** (`MediaPathShared`) supplements the selected pack. Files also go directly inside this folder. Multiple voices can reuse player-name or ambient recordings. An **identically spelled key** in the shared folder overrides the pack entry. Avoid differences in capitalization and multiple extensions for the same key to keep selection unambiguous. The selected pack folder must exist; the shared path is not a standalone pack.

## 2. Settings that control which files are used

Internal setting names help when using TUI, headless or searching for an option. GUI and TUI expose the same settings on the Caller page.

| Setting | Effect on your pack |
| --- | --- |
| `Enabled`, `LocalPlayback` | Both must be enabled for local announcements and ambient sounds. |
| `EnableScoreCalls` | Enables numeric scores, including single-dart mode 1 and the numeric checkout fallback. |
| `CallEveryDart` / `-E` | `0`: no regular single-dart announcements; `1`: points; `2`: segment; `3`: sound effect. |
| `CallEveryDartTotalScore` / `-ETS` | Adds the visit total in single-dart modes 1–3. Mode 0 requests the visit total regardless of this switch. |
| `EnableSpecialSounds` | Enables the `100plus` fallback and additional `reaction_<points>` sounds. |
| `CallCurrentPlayer` / `-CCP` | `0`: no regular player names; `1`: at start, before checkout hints and for winners; `2`: also on player/visit changes. |
| `CallBotActions` / `-CBA` | When disabled, bot darts, names and winner announcements are skipped. |
| `PossibleCheckoutCall` / `-PCC` | `0`: no checkout hints; greater than 0: limits hints per player while their remaining score is unchanged. |
| `PossibleCheckoutCallYourselfOnly` / `-PCCYO` | Checkout hints only for players on your own board. |
| `CallerRealLife` / `-CRL` | `1`: X01 uses special set/leg start and leg-winning sounds if available. |
| `CallBlindSupport` / `-CBS` | `1`: explains targets and hits for visually impaired players; replaces regular single-dart modes. |
| `AmbientSounds` / `-A` | `0`: background effects off; greater than 0: relative ambient volume. Effective volume = Caller volume × this value. |
| `AmbientSoundsAfterCalls` / `-AAC` | Off: start ambient before its associated announcement; on: start after that announcement. Ambient uses an independent channel. |
| `TtsEnabled` | Optional speech fallback for certain missing files. Off by default; not available on every platform. |

**Important:** `EnablePlayerNameCalls` does not replace `CallCurrentPlayer`. Regular live name announcements use `CallCurrentPlayer`. The extra option in the score helper does not generate a separate player-name announcement after each score in the current live pipeline.

## 3. Start, wins, cancellation and bull-off

In these tables, **silent** means there is no automatic speech fallback. “TTS” only works when enabled and available on the system.

| Key / example | Trigger / suggested recording | If missing |
| --- | --- | --- |
| `matchon` → `matchon.wav` | A new regular match, including the transition from bull-off to the actual game. “Match on”. | `gameon`, otherwise silent. |
| `gameon` | Start of another leg; also fallback for a missing match/set-leg start recording. “Game on”. | Silent. |
| `s<set>_l<leg>_n`, e.g. `s1_l2_n` | X01 with `CallerRealLife = 1`: start of that set/leg. Record a complete phrase, e.g. “First set, second leg”. | `gameon`. |
| `first_to_throw` | X01 with `CallerRealLife = 1`: after the start recording and optional player name. “First to throw”. | Silent. |
| `gameshot` | A leg has been won. “Game shot”. | Silent. |
| `gameshot_l<leg>_n`, e.g. `gameshot_l2_n` | Leg win with `CallerRealLife = 1`. “Game shot, second leg”. No separate set index in this key. | `gameshot`. |
| `matchshot` | A match has been won, including forfeits with a known winner. “Game shot and the match”. | `gameshot`. |
| `matchcancel` | Autodarts reports the match being deleted (`delete`) from the board; once per match. “Match cancelled”. Deleting an already finished match can also trigger this announcement. | TTS “Match cancelled” / “Match abgebrochen”, otherwise silent. |
| `busted` | A bust, even before dart three. “Bust”. | TTS “Bust” / “Überworfen”, otherwise silent. |
| `bulling_start` | A new, unfinished bull-off. A phrase introducing the bull-off. | Silent. |
| `bulling_end` | Bull-off has a bull winner. The optional winner name is spoken **before** this recording, e.g. “starts”. | Silent. |

Replace `<set>` and `<leg>` with actual numbers from Autodarts. A literal file `s<set>_l<leg>_n.wav` will not work. Record each combination you need separately. Numbers come from the game state; individual number recordings are not combined into a set/leg phrase.

**Bull-off is a separate phase:** it does not play regular score, single-dart effect, bust, checkout or leg-win announcements. For a forfeit during bull-off without a bull winner, Caller uses `matchshot` (fallback `gameshot`) and optionally the winner name. A board `finish` message without winner data is not a new start announcement and does not identify the winner on its own.

Restarting during an active game can trigger a start announcement once a usable game state is available. Existing darts establish a baseline and are not announced individually again. This Caller pipeline has no separate “application start” or “application exit” soundfile key.

## 4. Scores and special reactions

| Key | Usage / recording | Fallback |
| --- | --- | --- |
| `<points>`, e.g. `0`, `26`, `60`, `140`, `180` | Completed visit total; also dart points in `CallEveryDart = 1`, and optionally the checkout number. Record the number. `0` may say “No score”. | For ≥100, first `100plus` if special sounds are enabled; otherwise numeric TTS, otherwise silent. |
| `100plus` | General fallback for a **missing** exact number ≥100. For example “One hundred plus”. Not an additional sound after an available exact number. | TTS of the exact number, otherwise silent. |
| `reaction_<points>`, e.g. `reaction_180` | Additional reaction **after** a numeric request for that exact score ≥100, when special sounds are enabled. | No additional reaction. |

For complete scores without speech fallback, a set `0.wav` through `180.wav` is useful. Not every number is reachable with three darts, but manual corrections may also supply values. Field numbers are also needed for blind-target announcements. No leading zeros: `060.wav` is not requested as `60`.

**When is the visit total called?** Usually after three darts. Caller can also treat a visit with existing darts as completed by bust, win, player change or a reported takeout, allowing one- or two-dart visits. A bust requests `busted` instead of a numeric score. Score and reaction recordings are foreground audio; `reaction_180` is not ambient audio.

This implementation does not request keys `noscore`, `no_score`, `bust_reaction_1` or `cpu`. Use `0` for no score, `busted` for bust, and a bot's name or `player<N>` for bots.

## 5. Single darts: points, segments and effects

| Mode | Requested keys | Examples and behaviour |
| --- | --- | --- |
| `CallEveryDart = 0` | No regular single-dart keys. | Visit total at the end; special events remain active. |
| `CallEveryDart = 1` | Numeric dart score. | T20 → `60`; D20 → `40`; Single20 → `20`; miss → `0`. Fallback as in section 4. |
| `CallEveryDart = 2` | `s<field>`, `d<field>`, `t<field>`, `m<field>`. | T20 → `t20`; D20 → `d20`; Single20 → `s20`; zero points → `m` plus the reported field. If missing, TTS “Triple 20”, “Double 20”, “Single 20” or “Miss”, otherwise silent. |
| `CallEveryDart = 3` | `effect_s<field>`, `effect_d<field>`, `effect_t<field>`, `effect_m<field>`. | Segment-specific effects instead of spoken numbers. Fallback: `effect_single`, `effect_double`, `effect_triple`, `effect_miss`. If also missing, silent; no TTS fallback. |

Regular fields use 1–20. Bull uses field **25**: mode 2 requests `s25` for single bull or `d25` for bullseye; mode 3 uses `effect_s25` / `effect_d25`. Mode 1 uses `25` / `50`. The `bull` and `bullseye` keys are part of blind support (section 8), not automatically part of regular segment mode.

Misses use the reported field, for example `m0`, `m20`, `effect_m0`, `effect_m20`. The general effect `effect_miss` covers all zero-point darts. Segment mode 2 has **no** general `miss` file fallback; only the specific `m<field>` recording or TTS.

A new dart interrupts a regular single-dart announcement that is still playing and replaces it. Stale queued single darts are skipped. When visit totals are enabled, the total takes priority after dart three, so the third single-dart announcement/effect may be skipped. Visit totals, busts and winner announcements finish normally. Explanatory blind-mode announcements are not interrupted like regular single darts.

## 6. Player names and bots

| Key | Trigger / recording | Fallback |
| --- | --- | --- |
| `<player name>`, e.g. `alice` or `bot level 4` | Record that player's name. Requested name = display name trimmed at both ends and lowercased; internal spaces remain. | `player<N>`. |
| `player<N>`, e.g. `player1`, `player2`, `player3` | “Player 1”, “Player 2”, etc.; `<N>` = current player position + 1. | TTS “Player N” / “Spieler N”, otherwise silent. |

There is no automatic bot key `cpu`. A bot named `Bot Level 4` uses `bot level 4.wav` or its positional fallback. Enable `CallBotActions` for bot announcements. Positions can change after bull-off; `player1` refers to a position, not a fixed person. A player-name key such as `180` collides with the score key; use positional fallback in that case.

Names require `CallCurrentPlayer > 0`: at start, before checkout hints and after regular win announcements; for the bull-off winner, before `bulling_end`. Select `CallCurrentPlayer = 2` for each player/visit change.

## 7. Checkout hints

X01 only, with checkout hints enabled. Remaining scores **2–170** are eligible, except 159, 162, 163, 165, 166, 168 and 169. Hints are requested at match/leg start and player/visit changes; blind support can additionally request them after a new dart. Repeat limits and the own-board restriction still apply.

| Priority / key | Recording / usage |
| --- | --- |
| 1. `yr_<remaining>`, e.g. `yr_40` | **Complete phrase**, e.g. “You require forty”. When present, neither `you_require` nor another number is played. |
| 2. `you_require` | Introduction “You require”. If missing, introductory TTS or silence; the number is still requested afterwards. |
| 3. `c_<remaining>`, e.g. `c_40` | Checkout number after the introduction, e.g. “forty”. Separate from the regular `40` recording. |
| 4. `<remaining>`, e.g. `40` | If `c_40` is missing, use the regular numeric score request: exact number → optional `100plus` → TTS → silence. Enabled `reaction_<remaining>` sounds may also follow. |

An optional player name precedes the hint. Recordings contain no placeholders; `yr_40.wav` must contain the complete phrase for 40. These files are not combined into checkout routes such as “Single 8, Double 16”.

## 8. Blind support: explain targets and hits

`CallBlindSupport = 1` enables this logic and replaces regular single-dart modes. It uses target information actually supplied by Autodarts. No target means no target announcement. Bull-off still uses only its dedicated logic.

| Key | Trigger / suggested recording | Fallback |
| --- | --- | --- |
| `bs_target_is` | Before an available target announcement: “Target is”. | Introductory TTS. |
| `bs_any_double` | Target is any double. | TTS “Double”. |
| `bs_any_triple` | Target is any triple. | TTS “Triple”. |
| `bull` | Target/hit field 25 without double. “Bull”. | TTS “Bull”. |
| `bullseye` | Target/hit field 25 with double. “Bullseye”. | TTS “Bullseye”. |
| `bs_<lowercase target bed>` | Target bed other than absent/`Full`, e.g. `bs_double`, `bs_triple`, `bs_singleinner` or `bs_singleouter` when supplied by Autodarts. | TTS of the supplied bed name, followed by the field number if present. |
| `bs_single_inner` | Before a hit whose bed is `SingleInner` or `Inner Single`: “Inner single”. **Notice the underscore: this is different from `bs_singleinner`.** | TTS “Inner single” / “Single innen”. |
| `d<field>`, `t<field>`, `m<field>` | Complete hit phrase for a double, triple or zero-point dart: `d20`, `t20`, `m0`, etc. | Bed prefix from the next row, then field number. |
| `bs_double`, `bs_triple`, `bs_outside` | Fallback prefix before a field number when the complete hit key is missing. “Double”, “Triple”, “Outside”. | Prefix TTS. |
| `<field>`, e.g. `20` | Single hit or field number following a prefix/target announcement. | Numeric TTS. |

All TTS fallbacks remain silent when TTS is disabled/unavailable. Bull/bullseye uses a dedicated phrase, not prefix plus number. Inner single may add `bs_single_inner` before the number. A completed visit can also request the regular total score afterwards.

## 9. Ambient sounds: independent background channel

| Key | Trigger |
| --- | --- |
| `ambient_<visit total>`, e.g. `ambient_60`, `ambient_140`, `ambient_180` | Completed visit with that exact total. Not every individual dart. |
| `ambient_busted` | Completed bust visit, replacing `ambient_<visit total>`. |
| `ambient_matchcancel` | Match deletion alongside the cancellation announcement. |

Ambient requires `AmbientSounds > 0`. There is no generic fallback and no TTS fallback: the exact recording must exist. Ambient is independent of spoken score requests. Disabling score announcements does not prevent the matching ambient sound while Caller is otherwise enabled. Bull-off does not generate regular ambient score effects.

Ambient is never interrupted because of a new foreground announcement. Background effects play sequentially within their own channel while the foreground can speak. Stopping Caller stops both channels. `AmbientSoundsAfterCalls` controls whether the effect starts before/after its score/bust/cancellation announcement; it does not make ambient block the foreground.

## 10. Example sequences and testing checklist

| Situation | Example requested recordings |
| --- | --- |
| Regular match start, Alice, checkout hints disabled | `matchon` → `alice` (or `player1`). |
| Three T20, single darts off, special sounds and ambient on | Foreground `180` → optional `reaction_180`; background `ambient_180` independently. |
| T20 in segment mode | `t20`; missing file uses TTS “Triple 20” if enabled. |
| T20 in effect mode | `effect_t20`, otherwise `effect_triple`. |
| Checkout hint for 40 | Name → `yr_40`; otherwise name → `you_require` → `c_40` or `40`. |
| Bust | Foreground `busted`, optional background `ambient_busted`. |
| Match win | Possibly a completed visit, then `matchshot` (otherwise `gameshot`) → winner name if enabled. |
| Bull-off | `bulling_start`; bull winner: optional name → `bulling_end`; next regular game starts with `matchon`. |

For testing, disable random voices and TTS first so missing recordings are obvious. Local pack preview prefers `180`, then `matchon`, then `gameon`, otherwise an available recording; it does **not** test every event. Test single, double, triple, zero points, bust, checkout, leg/match win and bull-off. Enable Caller debug in the console: `Sound not found` identifies missing keys; `Played sound` identifies the used key. Skipping stale single darts is intentional.

**Headless example** (Windows; on Linux use `./DartsHub` instead of `.\DartsHub.exe`):

```powershell
.\DartsHub.exe --headless --caller-media-path "C:/MySoundpacks" --caller-caller "en-MyVoice" --caller-random-caller 0 --caller-enabled true --caller-local-playback true --caller-tts-enabled false --caller-call-every-dart 3 --caller-call-every-dart-total-score true
```

GUI, TUI and headless share these settings. Use `--help` to check the options supported by your version; the names above reflect the current implementation. The short option is **`-E`** (uppercase E). See [startup arguments](START_ARGUMENTS.md).

## Continuous announcements on Windows

GUI and terminal share the same playback. Related recorded sentence parts (such as player name, “you require” and score) use one continuous audio output. Short files are cached during playback. Very quiet clip edges are trimmed with a small safety margin; pauses within recordings remain intact. Original files are never modified. Long ambient recordings remain streamed. Legacy Python mixer options are still reported as unsupported.
