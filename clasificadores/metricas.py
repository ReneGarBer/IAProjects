def accuracy(vp: int, vn: int, fp: int, fn: int) -> float:
    return (vp+vn)/(vp+vn+fp+fn)

def precision(vp: int,fp: int) -> float:
    return (vp)/(vp+fp)

def sensitivity():
    return 1

def specificity(vn: int,fp: int) -> float:
    return (vn)/(vn+fp)

def f1score(pre: float, exh: float) -> float:
    return 2*(pre*exh/(pre+exh))