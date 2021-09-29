from coldtype import *

@animation((540, 540/2), timeline=20)
def giftest(f):
    return PS([
        (P(f.a.r)
            .f(hsl(f.e("eeio", 1, rng=(0.6, 0.8)), 0.8, 0.6))),
        (StSt("COLDTYPE",
            Font.ColdtypeObviously(),
            font_size=f.e("eeio", 1, rng=(90, 250)),
            wdth=f.e("eeio", 1, rng=(1, 0)))
            .align(f.a.r)
            .f(1))])

release = giftest.export(fmt="gif")