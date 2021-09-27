from coldtype import *
from coldtype.fx.skia import phototype


@animation((1080, 270),
    bg=hsl(0.45, 0.65, 0.4),
    timeline=Timeline(30, 18),
    storyboard=[0, 15])
def understroke(f):
    return (StSt("TYPOGRAPHY", Font.MutatorSans(),
        ro=1,
        font_size=150,
        rotate=f.e("ceio", 1, rng=(-10, 0)),
        wght=f.e("eeio", 1),
        wdth=f.e("eeio", 1),
        tu=f.e("eeio", 1, rng=(150, -855)))
        .align(f.a.r)
        .reverse_pens()
        .f(1)
        .understroke(sw=25)
        .ch(phototype(f.a.r, blur=2, cut=160, cutw=30, fill=hsl(0.17, 1))))