# Telegram bot for TRPG COC
Still in Demo status.<!--功能中对不同身份的区别不太清晰，无法查看自己的身份，且可能不支持有空白的角色卡，有空的话可以增加适配秘密团的功能（比如用户只能show自己的角色卡，KP能看所有人角色卡）-->

## 指令列表
所有指令以 '.'开始。

#### 共用指令

- .kp: 设置自己的身份为KP，设置为KP后可以使用KP专用指令。
- .kp rm: 移除自己的KP身份。
- .reset: **Reset all thing.** (now only dy can)
- .show_skill 技能名：展示规则书中部分技能的介绍，若不写技能名则展示可解释的技能名列表。
- .rd *x*: 掷骰 [1, *x*]
  - 例子：.rd 100 ->用户名 diced 15/100
- .add_pc 网站名 角色卡号：从网站的角色卡界面导入指定角色。
  - 现在只支持从猫爷TRPG导入，即 .add_pc maoye 角色卡号
- .rm_pc 角色名: 移除指定的角色卡。
- .show_pc ：展示目前已导入的角色卡信息，展示格式为“自动编号. 角色名：性别，年龄”
- .show_pc 角色名: 展示指定角色的年龄、性别以及属性和技能的具体数值。
- .ra 属性/技能名: 属性或技能检定。
- .sc *x/y*: San check, success minus *x* and fail minus *y* (x, y can be "z+xdy" format)
- .set 角色名 属性/技能名 （+/-)数值: 用于设置角色的属性/技能数值, 括号内为可选内容。
  - 例子1：把A的力量设置为50->.set A 力量 50
  - 例子2：把B的理智减少2->.set B san -2
- .bind 角色名: 将指定角色绑定给自己，成功绑定后的掷骰将不再显示telegram用户名，而是显示角色名。
- .unbind : 解绑自己当前绑定的角色。
- .show_bind: 查看当前自己绑定的PC。

#### KP专用指令（可选）

用于导入模组文件及判定战斗顺序。
KP暗骰可以私聊bot。
导入npc功能待定。

- load_mod *xx*: Load mod from file *mod_{xx}.yml*
- tell *xx*: Tell a piece of story labeled *xx* in mod['story']
- intro *xx*: Introduce sth/sb labeled *xx* in mod['npc']
- battle *a* *b* ...: Start battle with *a*, *b* ..., used to calculate action order

## 模组文件（可选）（暂停支持）
File name should be *mod_{xxx}.yml*.

It is only a Yaml file, having "story" for *tell* and "npc" for *intro*. It also has "enermy" for KP to refer, an enermy should have "dex" for *battle*.

## Tips
- 使用telegram自带的 'pin' 指令方便地记录线索。