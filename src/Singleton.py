class Singleton(object):
    _instance = None
    matrix = None
    matrix2 = None
    gameboard = None
    gameboard2 = None
    soundState = False
    mode = None
    turno = 0
    aux = 0
    aux2 = 0
    winner = 0
    msg = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls.matrix = [[0 for x in range(0,10)] for y in range (0,10)]
            cls.matrix2 = [[0 for x in range(0,10)] for y in range (0,10)]
        return cls._instance

