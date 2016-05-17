FloatLayout:
    Button:
        size_hint: None, None   # absolute size
        size: 40, 20
        pos: 0, 0
        text: 'one'
    Button:
        size_hint: None, None
        size: 20, 40
        pos: 30, 30
        text: 'two'
    Button:
        size_hint: 0.5, 0.2  # relative size of 50% width and 20 % height
        pos_hint: {'x': 0.5, 'y': 0.5}  # relative position from (0,0)
        text: 'three'