def can_play(fn):
    def inner(x, y, *args, ** kwargs):
        # if args[0] <= 22:
        clock = kwargs.get('clock', 23)
        if clock <= 22:
            fn(x, y)  # 调用play_game
        else:
            print('下播')

    return inner


@can_play
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))


play_game('xx', 'Apex', clock=18)
play_game('pite', 'qq', 23)
