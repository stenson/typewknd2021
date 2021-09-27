from coldtype import *
from coldtype.fx.skia import phototype


def coldtype_logo():
    return (StSt("COLDTYPE", Font.ColdtypeObviously(), 200,
        wdth=1,
        tu=-100,
        kp={
            "D/T":-100,
            "T/Y":-50,
            "P/E":-210
        })
        .reverse_pens()
        .f(1)
        .understroke(sw=20))


@renderable((1080, 540))
def plain(r):
    return coldtype_logo().align(r)


@renderable((1080, 540))
def knockout(r):
    return (coldtype_logo()
        .align(r)
        .ch(lambda p: p
            .ch(phototype(
                p.ambit().inset(-10),
                blur=3,
                cut=190,
                cutw=15,
                fill=hsl(0.63, 0.7, 0.6)))))