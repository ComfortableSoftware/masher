# pylint: disable

import libevdev as LD


def IDB():
  _HotBeefInjector_ = LD.Device()
  _HotBeefInjector_.name = "HBI hot beef injector"

  _HotBeefInjector_.enable(LD.EV_KEY.BTN_LEFT)  # ability to send MSEBTNLT
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_MIDDLE)  # ability to send MSEBTNMID
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_RIGHT)  # ability to send MSEBTNRT
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_EXTRA)  # ability to send MSEBTNXTRA
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_SIDE)  # ability to send MSEBTNSIDE
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_FORWARD)  # ability to send MSEBTNFWD
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_BACK)  # ability to send MSEBTNBAK
  _HotBeefInjector_.enable(LD.EV_KEY.BTN_TASK)  # ability to send MSEBTNTASK

  _HotBeefInjector_.enable(LD.EV_KEY.KEY_0)  # ability to send KEY_0
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_1)  # make KEY_1 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_102ND)  # make KEY_102ND available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_2)  # make KEY_2 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_3)  # make KEY_3 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_4)  # make KEY_4 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_5)  # make KEY_5 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_6)  # make KEY_6 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_7)  # make KEY_7 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_8)  # make KEY_8 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_9)  # make KEY_9 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_A)  # make KEY_A available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_AGAIN)  # make KEY_AGAIN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_APOSTROPHE)  # make KEY_APOSTROPHE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_B)  # make KEY_B available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_BACK)  # make KEY_BACK available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_BACKSLASH)  # make KEY_BACKSLASH available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_BACKSPACE)  # make KEY_BACKSPACE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_C)  # make KEY_C available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_CALC)  # make KEY_CALC available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_CAPSLOCK)  # make KEY_CAPSLOCK available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_COFFEE)  # make KEY_COFFEE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_COMMA)  # make KEY_COMMA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_COMPOSE)  # make KEY_COMPOSE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_COPY)  # make KEY_COPY available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_CUT)  # make KEY_CUT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_D)  # make KEY_D available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_DELETE)  # make KEY_DELETE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_DOT)  # make KEY_DOT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_DOWN)  # make KEY_DOWN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_E)  # make KEY_E available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_EDIT)  # make KEY_EDIT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_EJECTCD)  # make KEY_EJECTCD available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_END)  # make KEY_END available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_ENTER)  # make KEY_ENTER available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_EQUAL)  # make KEY_EQUAL available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_ESC)  # make KEY_ESC available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F)  # make KEY_F available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F1)  # make KEY_F1 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F10)  # make KEY_F10 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F11)  # make KEY_F11 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F12)  # make KEY_F12 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F13)  # make KEY_F13 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F14)  # make KEY_F14 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F15)  # make KEY_F15 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F16)  # make KEY_F16 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F17)  # make KEY_F17 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F18)  # make KEY_F18 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F19)  # make KEY_F19 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F2)  # make KEY_F2 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F20)  # make KEY_F20 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F21)  # make KEY_F21 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F22)  # make KEY_F22 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F23)  # make KEY_F23 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F24)  # make KEY_F24 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F3)  # make KEY_F3 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F4)  # make KEY_F4 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F5)  # make KEY_F5 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F6)  # make KEY_F6 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F7)  # make KEY_F7 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F8)  # make KEY_F8 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_F9)  # make KEY_F9 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_FIND)  # make KEY_FIND available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_FORWARD)  # make KEY_FORWARD available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_FRONT)  # make KEY_FRONT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_G)  # make KEY_G available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_GRAVE)  # make KEY_GRAVE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_H)  # make KEY_H available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HANGEUL)  # make KEY_HANGEUL available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HANJA)  # make KEY_HANJA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HELP)  # make KEY_HELP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HENKAN)  # make KEY_HENKAN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HIRAGANA)  # make KEY_HIRAGANA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_HOME)  # make KEY_HOME available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_I)  # make KEY_I available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_INSERT)  # make KEY_INSERT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_J)  # make KEY_J available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_K)  # make KEY_K available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KATAKANA)  # make KEY_KATAKANA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KATAKANAHIRAGANA)  # make KEY_KATAKANAHIRAGANA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP0)  # make KEY_KP0 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP1)  # make KEY_KP1 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP2)  # make KEY_KP2 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP3)  # make KEY_KP3 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP4)  # make KEY_KP4 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP5)  # make KEY_KP5 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP6)  # make KEY_KP6 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP7)  # make KEY_KP7 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP8)  # make KEY_KP8 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KP9)  # make KEY_KP9 available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPASTERISK)  # make KEY_KPASTERISK available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPCOMMA)  # make KEY_KPCOMMA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPDOT)  # make KEY_KPDOT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPENTER)  # make KEY_KPENTER available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPEQUAL)  # make KEY_KPEQUAL available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPJPCOMMA)  # make KEY_KPJPCOMMA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPLEFTPAREN)  # make KEY_KPLEFTPAREN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPMINUS)  # make KEY_KPMINUS available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPPLUS)  # make KEY_KPPLUS available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPRIGHTPAREN)  # make KEY_KPRIGHTPAREN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_KPSLASH)  # make KEY_KPSLASH available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_L)  # make KEY_L available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFT)  # make KEY_LEFT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFTALT)  # make KEY_LEFTALT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFTBRACE)  # make KEY_LEFTBRACE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFTCTRL)  # make KEY_LEFTCTRL available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFTMETA)  # make KEY_LEFTMETA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_LEFTSHIFT)  # make KEY_LEFTSHIFT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_M)  # make KEY_M available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_MINUS)  # make KEY_MINUS available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_MUHENKAN)  # make KEY_MUHENKAN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_MUTE)  # make KEY_MUTE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_N)  # make KEY_N available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_NEXTSONG)  # make KEY_NEXTSONG available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_NUMLOCK)  # make KEY_NUMLOCK available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_O)  # make KEY_O available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_OPEN)  # make KEY_OPEN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_P)  # make KEY_P available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PAGEDOWN)  # make KEY_PAGEDOWN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PAGEUP)  # make KEY_PAGEUP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PASTE)  # make KEY_PASTE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PAUSE)  # make KEY_PAUSE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PLAYPAUSE)  # make KEY_PLAYPAUSE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_POWER)  # make KEY_POWER available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PREVIOUSSONG)  # make KEY_PREVIOUSSONG available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_PROPS)  # make KEY_PROPS available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_Q)  # make KEY_Q available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_R)  # make KEY_R available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_REFRESH)  # make KEY_REFRESH available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHT)  # make KEY_RIGHT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHTALT)  # make KEY_RIGHTALT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHTBRACE)  # make KEY_RIGHTBRACE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHTCTRL)  # make KEY_RIGHTCTRL available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHTMETA)  # make KEY_RIGHTMETA available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RIGHTSHIFT)  # make KEY_RIGHTSHIFT available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_RO)  # make KEY_RO available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_S)  # make KEY_S available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SCROLLDOWN)  # make KEY_SCROLLDOWN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SCROLLLOCK)  # make KEY_SCROLLLOCK available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SCROLLUP)  # make KEY_SCROLLUP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SEMICOLON)  # make KEY_SEMICOLON available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SLASH)  # make KEY_SLASH available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SLEEP)  # make KEY_SLEEP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SPACE)  # make KEY_SPACE available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_STOP)  # make KEY_STOP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_STOPCD)  # make KEY_STOPCD available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_SYSRQ)  # make KEY_SYSRQ available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_T)  # make KEY_T available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_TAB)  # make KEY_TAB available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_U)  # make KEY_U available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_UNDO)  # make KEY_UNDO available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_UNKNOWN)  # make KEY_UNKNOWN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_UP)  # make KEY_UP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_V)  # make KEY_V available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_VOLUMEDOWN)  # make KEY_VOLUMEDOWN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_VOLUMEUP)  # make KEY_VOLUMEUP available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_W)  # make KEY_W available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_WWW)  # make KEY_WWW available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_X)  # make KEY_X available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_Y)  # make KEY_Y available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_YEN)  # make KEY_YEN available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_Z)  # make KEY_Z available
  _HotBeefInjector_.enable(LD.EV_KEY.KEY_ZENKAKUHANKAKU)  # make KEY_ZENKAKUHANKAKU available

  _HotBeefInjector_.enable(LD.EV_REL.REL_HWHEEL)  # make REL_HWHEEL available
  _HotBeefInjector_.enable(LD.EV_REL.REL_HWHEEL_HI_RES)  # make REL_HWHEEL_HI_RES available
  _HotBeefInjector_.enable(LD.EV_REL.REL_WHEEL)  # make REL_WHEEL available
  _HotBeefInjector_.enable(LD.EV_REL.REL_WHEEL_HI_RES)  # make REL_WHEEL_HI_RES available
  _HotBeefInjector_.enable(LD.EV_REL.REL_X)  # make REL_X available
  _HotBeefInjector_.enable(LD.EV_REL.REL_Y)  # make REL_Y available

  _HotBeefInjectorDevice_ = _HotBeefInjector_.create_uinput_device()
  #print(f"New device at {_HotBeefInjectorDevice_.devnode} ({_HotBeefInjectorDevice_.syspath})")
  return _HotBeefInjectorDevice_



#
