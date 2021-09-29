from coldtype import *

@animation((1080, 540), timeline=60, storyboard=[0], render_bg=1)
def vari(f):
    return (StSt("Type\nWknd".upper(), Font.MutatorSans(),
        font_size=f.e("eeio", 1, rng=(150, 100)),
        wdth=f.e("eeio", 1),
        wght=f.e("eeio", 1),
        leading=30)
        .align(f.a.r))
