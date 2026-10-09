# Player-specific event rules

WLED, PixelIt and Awtrix use player names without case sensitivity. Backend matching trims surrounding spaces and uses invariant lowercase; the original spelling remains available in saved settings.

For each target device, matching enabled named rules suppress general rules of the same rule type. Other names, disabled rules and rules whose event conditions do not match do not suppress a general rule. Different event types retain their existing priority. Existing rule order resolves ties between equally specific rules.

In the GUI, set the player-name field on an extension event rule and save. In the TUI, edit the same extension rule and its player-name field, then save. Both use the same runtime selection, including imported settings. No new legacy parameter is required.
