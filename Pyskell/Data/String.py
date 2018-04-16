from Pyskell.Language import C, TS, L


@TS(C / str >> [str])
def lines(string):
    return L[[]] if not string else L[string.split("\n")]


@TS(C / str >> [str])
def words(string):
    return L[[]] if string == "" else L[string.split(" ")]


@TS(C / [str] >> str)
def unlines(strings):
    return "\n".join(strings)


@TS(C / [str] >> str)
def unwords(strings):
    return " ".join(strings)
