# Telegram bot for TRPG COC
Still in Demo status.

## Run
`python index.py`

 Tmp deployed on Heroku, local deployment is removed.

## API
Commands start with '.'
- kp: Become KP
- kp rm: Remove current KP
- reset: **Reset all thing.** (now only dy can)
- rd *x*: Roll [1, *x*]
- add_pc *f* *x*, case *f*:
  - *Note that each pc should at least has "sex", "san" and "age", etc.*
  - 'maoye': *x* is the pc id in maoye
  - 'str': *x* is formatted as "{name}:{attr1},{value1};{attr2},{value2};..."
- rm_pc *x*: Remove PC named *x*
- show_pc *x*: Show PC named *x* in detail. If *x* is not given, show pc list
- set *pc* *attr* *x*: Change pc[attr] to/by *x*, *x* can start with '+' or '-' if it is "by" else "to".
- bind *pc*: Bind your account to *pc*
- unbind: Unbind
- show_bind: Check self's bind
- ra *attr*: Check your *attr*
- sc *x*: San check, success minus *x* and fail minus *y* (x, y can be "z+xdy" format)
- show_skill *x*: Show the desc of skill *x*

#### only for kp
- load_mod *xx*: Load mod from file *mod_{xx}.yml*
- tell *xx*: Tell a piece of story labeled *xx* in mod['story']
- intro *xx*: Introduce sth/sb labeled *xx* in mod['npc']
- battle *a* *b* ...: Start battle with *a*, *b* ..., used to calculate action order

## Mod file (tmp stop supported)
File name should be *mod_{xxx}.yml*.

It is only a Yaml file, having "story" for *tell* and "npc" for *intro*. It also has "enermy" for KP to refer, an enermy should have "dex" for *battle*.

## Tips
- Use 'pin' of telegram to store clues/maps