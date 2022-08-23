# Telegram bot for TRPG COC
Still in Demo status.

## API
Commands start with '.'
- kp: Become KP
- kp rm: Remove current KP
- reset: **Reset all thing.** (now only dy can)
- rd *x*: Roll [1, *x*]
- add_pc *f* *x*:
  - now *f* can only be 'maoye', and *x* is the pc id in maoye
- rm_pc *x*: Remove PC named *x*
- show_pc *x*: Show PC named *x* in detail. If *x* is not given, show pc list
- set *pc* *attr* *x*: Change pc[attr] to/by *x*, *x* can start with '+' or '-' if it is "by" else "to".
- bind *pc*: Bind your account to *pc*
- unbind: Unbind
- ra *attr*: Check your *attr*
- sc *x*: San check, fail will minus *x* (can be "z+xdy" format)

#### only for kp`
- load_mod *xx*: Load mod from file *mod_{xx}.yml*
- tell *xx*: Tell a piece of story labeled *xx* in mod['story']
- intro *xx*: Introduce sth/sb labeled *xx* in mod['npc']
- battle *a* *b* ...: Start battle with *a*, *b* ..., used to calculate action order

## Mod file
File name should be *mod_{xxx}.yml*.

It is only a Yaml file, having "story" for *tell* and "npc" for *intro*. It also has "enermy" for KP to refer, an enermy should have "dex" for *battle*.

## Tips
- Use 'pin' of telegram to store clues/maps