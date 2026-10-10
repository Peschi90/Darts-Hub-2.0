# Caller sound keys and their triggers

[Deutsch](CALLER_SOUND_KEYS.de.md) · [Soundpack setup](CALLER_SOUNDPACKS.en.md)

A key is the filename without its extension: `effect_cricket_scored.wav` uses `effect_cricket_scored`. WAV, MP3, OGG and FLAC are supported. Lookup is case-insensitive. Variants such as `key+1`, `key+2` and `key+cheer` are chosen randomly, even without the base file. Shared media replaces the selected pack's variants for that key.

GUI, TUI, local output and browser caller use the same recorded sounds and events. TTS fallback requires enabled TTS and local output; synthesized speech is not sent as a clip to the browser. Missing optional effects or ambient files are silent. Pack preview plays a sample, not every event.

## Output controls

- Enable Caller and local or browser output.
- `CallEveryDart`: 0 = no ordinary individual calls; 1 = physical dart score; 2 = segment; 3 = effect. `CallBlindSupport = 1` replaces ordinary individual modes.
- `EnableScoreCalls` enables numeric calls and Cricket visit announcements. `CallEveryDartTotalScore` adds visit calls in modes 1–3; mode 0 requests them regardless of this switch.
- `CallCurrentPlayer`: 0 = off; 1 = start, checkout and win; 2 = also player/new visit. `CallBotActions` controls bot announcements.
- `AmbientSounds > 0` enables the independent background channel. `AmbientSoundsAfterCalls` controls ordering. A new ambient effect replaces the previous one.
- Enabled incoming dart calls can interrupt ordinary announcements. With individual calls disabled, a dart alone does not interrupt speech. Visit totals follow dart 3 and remain interruptible. Bust and winning announcements retain their priority.

## Start, finish and names

| Key or family | Trigger and fallback |
| --- | --- |
| `matchon` | Match start, falling back to `gameon`. The actual game after bull-off is recognized. |
| `gameon` | Leg start and match-start fallback. |
| `s<Set>_l<Leg>_n` | X01 start with `CallerRealLife = 1`, e.g. `s1_l2_n`; falls back to `gameon`. Record the set/leg phrase. |
| `first_to_throw` | After the start and player phrase in X01 Real-Life mode. |
| `bulling_start` | Bull-off begins. |
| `bulling_end` | Bull-off decided, optionally after the winning player's name. |
| `gameshot` | Leg won; also the fallback for a missing match-win clip. |
| `gameshot_l<Leg>_n` | Leg won in Real-Life mode; falls back to `gameshot`. |
| `matchshot` | Match won; falls back to `gameshot`. The winner reported by Autodarts is authoritative. |
| `matchcancel` | Match deleted/cancelled; TTS fallback, otherwise silent. Leaving a finished match is not cancellation. |
| `busted` | Bust; TTS fallback, otherwise silent. |
| `<playername>` | Trimmed display name in lowercase, including bot names. Falls back to `player<N>`, then TTS. |
| `player<N>` | Current player position plus one; positions can change between legs. |

## Numbers, darts and checkout

| Key or family | Trigger and fallback |
| --- | --- |
| `<number>`, e.g. `0`, `60`, `180` | Numeric dart, visit or checkout call. Looks up the actual number, not individual digits. For missing values at least 100: `100plus` when special sounds are enabled; then TTS, otherwise silent. |
| `100plus` | Missing-number fallback for values at least 100 with `EnableSpecialSounds`. |
| `reaction_<number>` | Additional reaction after numeric calls at least 100 with `EnableSpecialSounds`, if present. |
| `s<field>`, `d<field>`, `t<field>` | Segment mode 2: single/double/triple on 1–20. TTS phrase fallback. |
| `m<field>` | Mode 2 physical miss, using the reported field including `m0`. TTS “Miss” fallback. |
| `bull`, `bullseye` | Single/double bull in mode 2 and blind support. Ordinary segment mode also accepts `s25`/`d25` as fallbacks. |
| `effect_s<field>`, `effect_d<field>`, `effect_t<field>`, `effect_m<field>` | Mode 3 effects; general fallback `effect_single`, `effect_double`, `effect_triple`, `effect_miss`. No TTS. Cricket first uses the keys below. |
| `effect_bull`, `effect_bullseye` | Bull effects in mode 3; fallback `effect_s25`/`effect_d25`, then general single/double effect. |
| `effect_single`, `effect_double`, `effect_triple`, `effect_miss` | General fallback for missing segment effects. |
| `yr_<remaining>` | Complete X01 checkout phrase, e.g. “You require forty”. Highest priority. |
| `you_require` | X01 checkout introduction when the complete phrase is missing; TTS fallback. |
| `c_<remaining>` | Checkout number after the introduction; falls back to the ordinary number/TTS. |

Checkout calls are X01-only for remaining scores 2–170, subject to configured repetition and own-board limits. Bogey numbers 159, 162, 163, 165, 166, 168 and 169 do not produce an ordinary checkout announcement.

## Cricket, Tactics and Hidden Cricket

Cricket uses 15–20 and bull; Tactics uses 10–20 and bull. Hidden Cricket only uses fields actually revealed by Autodarts. Server marks, segment states, points and winners are authoritative. At least three marks close a field for a player; values above three still mean closed.

With `CallEveryDart = 3`, exactly one of the four hit effects is chosen: scoring takes precedence over closing, followed by a mark or no counting hit. A dart that closes and also scores uses only the scoring effect.

| Key | Exact trigger |
| --- | --- |
| `effect_cricket_mark` | Counting marks, without closing or scoring. |
| `effect_cricket_closed` | This dart reaches the player's third mark or more, without scoring points. |
| `effect_cricket_scored` | Actual points scored: for the throwing player in Standard, for open opponents in Cut Throat. Never in No Score. |
| `effect_cricket_no_mark` | Zero counting marks: non-target, physical miss or field already closed by everyone. |
| `cricket_marks_0` … `cricket_marks_9` | Completed visit: complete phrase such as “No marks” or “Six marks”, with TTS fallback, then an existing numeric marks clip without the suffix phrase. Winning announcements take precedence. Also used in No Score. |
| `cricket_points` | Optional Standard scoring suffix after marks and the numeric points, e.g. “points”. Presence of the file opts into this additional phrase. |
| `cricket_penalty_points` | Optional Cut-Throat suffix, e.g. “penalty points”. No Score never announces points. |
| `cricket_field_opened` | Optional after a segment call in mode 2 or blind support: first mark on an untouched field. Immediate closure uses the closure phrase instead. |
| `cricket_field_closed` | Optional after segment call: field closed for the throwing player. |
| `cricket_field_closed_all` | Optional after segment call: field now closed by everyone; takes precedence over the ordinary closure phrase. |
| `cricket_field_revealed` | Optional after segment call: a Hidden-Cricket target is revealed for the first time. May precede a closure phrase. |
| `ambient_cricket_marks_0` … `ambient_cricket_marks_9` | Background effect for the marks in a completed non-winning visit. Exact mark key precedes general fallback effects. |

Missing Cricket hit effects fall back to the existing segment effect for counting marks, or only `effect_miss` for zero marks. Missing optional field phrases are silent. Corrected darts and visits changed by undo are evaluated again; identical snapshots do not repeat calls.

Cricket ambient fallback: 9 marks → `ambient_180`; 7–8 → `ambient_150more`; 6 → `ambient_120more`; 5 → `ambient_100more`; 4 → `ambient_50more`; 0 → `ambient_noscore`. There is no general fallback for 1–3 marks. These legacy filenames identify effects here, not actual points scored.

## Blind support

| Key or family | Trigger |
| --- | --- |
| `bs_target_is` | Introduction before a known target from the game state. |
| `bs_any_double`, `bs_any_triple` | Any-double/any-triple target. |
| `bs_<target bed>` | Reported target bed in lowercase, unless empty/`Full`; followed by the field number. |
| `bs_single_inner` | Before an inner single with bed `SingleInner` or `Inner Single`. |
| `d<field>`, `t<field>`, `m<field>` | Complete hit phrase; singles use the field number directly. |
| `bs_double`, `bs_triple`, `bs_outside` | Fallback prefix before the field number when the complete hit phrase is absent. |
| `bull`, `bullseye`, `<field number>` | Bull/field target or hit; TTS fallback. |

All blind phrases have TTS fallback. Cricket additionally uses the optional field phrases. Undisclosed Hidden-Cricket targets are not announced in advance.

## Ambient families

| Key or family | Trigger and selection |
| --- | --- |
| `ambient_<combination>` | Completed non-winning X01/Shanghai visit with points: original lowercase segment names in throwing order, e.g. `ambient_t20t20t20`. Precedes exact score and range. |
| `ambient_<total>` | X01/Shanghai fallback for a missing combination. |
| `ambient_180` | Exactly 180 in Count-up/Gotcha; nine hit values in RTW; nine-mark fallback in Cricket. |
| `ambient_150more`, `ambient_120more`, `ambient_100more`, `ambient_50more`, `ambient_1more` | Highest matching X01/Shanghai/Bermuda range from 150/120/100/50/1. Count-up/Gotcha use 153/120/100/50, no 1more selection. RTW uses hit values from 7/6/5/4. Cricket uses mark fallback above. |
| `ambient_noscore` | Zero points/bust in applicable modes; zero counting marks in Cricket. |
| `ambient_group_legendary`, `ambient_group_perfect`, `ambient_group_very_nice`, `ambient_group_good`, `ambient_group_normal` | Additional grouping with three coordinates in X01/Shanghai/Bermuda; existing calculation thresholds 98/95/92/89/86. |
| `ambient_matchon`, `ambient_gameon` | Match/leg start; match-on falls back to game-on. |
| `ambient_matchshot`, `ambient_setshot`, `ambient_gameshot` | Match/set/leg win; match/set-shot fall back to game-shot. |
| `ambient_playerchange` | Next player/visit if no checkout call is spoken. |
| `ambient_<event>_<playername>` | Named variants for match/game-on, match/set/game-shot and playerchange; precede general keys. |
| `ambient_lobby_in`, `ambient_lobby_out` | Player enters/leaves a tracked lobby. |
| `ambient_bogey_number_<remaining>`, `ambient_bogey_number` | X01 bogey number; exact number before general clip. |
| `ambient_checkout_call_limit` | Checkout repetition limit reached when another hint is requested. |
| `ambient_matchcancel` | Match cancelled; replaces the running ambient effect. |

ATC has no visit-score ambient selection. Cricket uses counting marks rather than physical dart scores. Unlisted arbitrary names are not automatically looked up as events; a file can still be selected explicitly for preview.

## Extension events and terminal controls

WLED, PixelIt, Awtrix and GIF expose `CricketMark`, `CricketClosed`, `CricketScored`, `CricketNoMark`, `CricketOpened`, `CricketClosedAll`, `CricketRevealed`. The first four are mutually exclusive hit results; the others are additional transitions. Winning events retain priority. WLED uses the same expert access requirement as its other detailed dart rules.

GUI: extension → add event rule → select Cricket trigger → configure effects/media/display steps → save. TUI: extension → rules → add/edit rule → select the same trigger → save. Existing JSON rules retain their triggers through persistence and legacy import. Old general score rules are not silently converted into new Cricket rules.

PixelIt/Awtrix placeholders: `cricket-scoring-mode`, `cricket-field`, `cricket-marks`, `cricket-turn-marks`. For Cricket hit events `score` contains points scored by that dart; `dart-score` remains its physical value. `game-mode-extra` identifies Cricket/Tactics/Hidden Cricket. Marks are not automatically points or newly closed fields.
