# Match ended and left / Match beendet und verlassen

`MatchExited` is available in WLED, PixelIt and AwtrixNG. It fires when Autodarts removes the current match from the board, including cancellation, completion/forfeit followed by leaving, an explicit empty board match, or replacement by another match. Winning a match while its result screen is still active does not fire this trigger. A network disconnection alone does not fire it either. Repeated removal messages do not repeat the trigger because the current match subscription has already been cleared.

In WLED, an enabled matching rule overrides OffAfterGame for its targeted devices. Devices without a matching rule still follow automatic switch-off. Pending off-after-win actions are cleared when leaving, and late takeout events cannot overwrite the exit effect. A subsequent match starts its normal idle/start rules.

GUI: add an event rule and select **Match ended and left** in each module’s trigger list, choose the effect/screen and target devices, then save. TUI: open the corresponding module settings, edit/add a rule, select the same trigger from the shared catalog, configure steps/effects, then save. Existing JSON settings round-trip the native `MatchExited` trigger; legacy imports preserve it. It has no legacy command-line alias because old Darts-Hub did not provide this distinct lifecycle event.
