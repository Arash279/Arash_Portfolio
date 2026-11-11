"""Original editorial SVG covers. All geometries are conceptual, not measured data.
Run from any directory with Python 3; no third-party dependencies required.
"""
from pathlib import Path
from math import sin, cos, pi, exp
from html import escape
from xml.etree import ElementTree

OUT = Path(__file__).resolve().parents[1] / 'public' / 'images' / 'covers'
OUT.mkdir(parents=True, exist_ok=True)
NAVY, BLUE, COPPER = '#003366', '#7397b5', '#b37549'

def path(d, stroke=NAVY, width=3, fill='none', extra=''):
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{width}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'

def circle(x, y, r, fill='none', stroke=NAVY, width=2, extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" {extra}/>'

def rect(x,y,w,h,fill='none',stroke=NAVY,rx=0,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" {extra}/>'

def text(x,y,t,size=18,color=NAVY,extra=''):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" {extra}>{escape(t)}</text>'

def cover(name,title,desc,body,number,caption):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="750" viewBox="0 0 1200 750" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs>
  <linearGradient id="paper" x2="1" y2="1"><stop stop-color="#f8fafb"/><stop offset="1" stop-color="#e8eff4"/></linearGradient>
  <linearGradient id="metal" x2="1" y2=".7"><stop stop-color="#d9e5ed"/><stop offset=".5" stop-color="#f9fbfc"/><stop offset="1" stop-color="#abc1d3"/></linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#003366" stroke-opacity=".045"/></pattern>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#003366" flood-opacity=".10"/></filter>
</defs>
<rect width="1200" height="750" fill="url(#paper)"/><rect width="1200" height="750" fill="url(#grid)"/>
<circle cx="1080" cy="70" r="360" fill="#fff" opacity=".36"/>
<path d="M70 150h28m-14-14v28M1102 600h28m-14-14v28" stroke="#9fb6c7" stroke-width="1.5"/>
{body}
{text(100,606,caption,15,BLUE,'letter-spacing="3"')}
{text(1100,606,number,17,BLUE,'text-anchor="end" letter-spacing="2"')}
</svg>'''
    ElementTree.fromstring(svg)
    (OUT/name).write_text(svg, encoding='utf-8')

# 01: A machine cross-section opening into a mathematical response.
# The concentric geometry is an editorial symbol, not a winding/slot drawing.
b = '<g filter="url(#shadow)">'
b += circle(350,355,183,'url(#metal)',NAVY,2)
b += circle(350,355,158,'#f7fafc',BLUE,2)
for i in range(24):
    a=2*pi*i/24
    x,y=350+140*cos(a),355+140*sin(a)
    b += f'<rect x="{x-6:.2f}" y="{y-17:.2f}" width="12" height="34" rx="5" fill="{COPPER if i%4==0 else "#aec3d3"}" transform="rotate({i*15+90} {x:.2f} {y:.2f})"/>'
b += circle(350,355,113,'#dce7ef',NAVY,3)+circle(350,355,92,'url(#metal)',BLUE,1)
for i in range(14):
    a=2*pi*i/14
    b += circle(round(350+76*cos(a),2),round(355+76*sin(a),2),4,'#7397b5','none')
b += circle(350,355,31,'#f7fafc',NAVY,3)+circle(350,355,8,NAVY,'none')+'</g>'
b += path('M350 137v42m0 352v42M132 355h42',BLUE,1)
b += path('M473 250 566 194H765',BLUE,1.5)+text(579,182,'R · L · C',24)
b += path('M490 469 557 520H1006',BLUE,1.5)
# Response ribbon, visibly conceptual with no data axes or numerical ticks.
b += path('M455 421C520 421 539 405 567 357S599 254 624 264 638 443 684 437 736 220 786 235 794 378 842 369 891 324 954 334 1012 324 1060 296',NAVY,5)
b += path('M455 435C520 435 542 420 570 372S599 268 623 279 644 454 688 449 742 237 785 251 806 391 847 382 895 337 955 348 1014 340 1060 312',BLUE,1.5,extra='opacity=".4"')
for x,y in [(501,418),(552,382),(594,288),(625,268),(660,427),(707,406),(755,258),(786,235),(825,369),(887,338),(962,333),(1033,315)]:
    b += circle(x,y,5,'#f9fbfc',COPPER,2)
b += text(958,228,'Z(f)',38,NAVY,'font-style="italic"')
b += text(580,550,'IDENTIFY THE RESPONSE',17,NAVY,'letter-spacing="2.5"')
cover('induction-motor.svg','From machine response to an identifiable model','Concept illustration of an induction-machine cross-section and a response ribbon with sampled points. Geometry and curves are illustrative, not measured data or an exact circuit.',b,'01','WIDEBAND IDENTIFICATION')

# 02: Spectral sheets. A shared ridge makes registration visible without a flowchart.
b = ''
for k in range(6):
    x0,y0=190+k*57,500-k*38
    pts=[]
    for j in range(81):
        x=j*7
        z=130*exp(-((x-252)/47)**2)+20*exp(-((x-424)/65)**2)
        pts.append((x0+x,y0-z))
    d='M'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)
    b+=path(d+f'L{x0+560} {y0+18}L{x0} {y0+18}Z',BLUE,1.5,'#f4f8fb',extra='opacity=".92"')
    b+=path(d,COPPER if k==3 else NAVY,4 if k==3 else 2.5)
    # Faint unregistered reference peak for visual comparison.
    shift=-(k-2.5)*26
    ghost=[]
    for j in range(61):
        x=j*9
        z=120*exp(-((x-252-shift)/47)**2)
        ghost.append((x0+x,y0-z))
    b+=path('M'+' '.join(f'{x:.1f},{y:.1f}' for x,y in ghost),BLUE,1.5,extra='stroke-dasharray="5 7" opacity=".5"')
    b+=circle(x0+252,y0-130,5,'#f9fbfc',COPPER,2)
b+=path('M442 370 727 180',COPPER,2,extra='stroke-dasharray="4 6"')
b+=text(767,180,'RESONANCE',18,NAVY,'letter-spacing="3"')
b+=text(767,208,'IN REGISTER',18,NAVY,'letter-spacing="3"')
b+=path('M735 186h20',COPPER,2)
# A restrained winding motif identifies the magnetic-component context.
b+=path('M161 228h25c0-43 23-43 23 0 0-43 23-43 23 0 0-43 23-43 23 0h24M185 241h72M185 248h72',BLUE,2.5)
b+=text(173,284,'N',25,NAVY,'font-style="italic"')
cover('common-mode-choke.svg','Resonance in register','Conceptual stack of choke impedance spectra. Dashed displaced peaks contrast with an aligned ridge. Sheet heights and number of layers are illustrative, not measured devices or test results.',b,'02','RESONANCE-ALIGNED PREDICTION')

# 03: Model layers and a cutaway observation window, rather than book decoration.
b=''
for x,y in [(240,274),(208,238),(176,202)]:
    b+=f'<g transform="translate({x} {y}) skewY(-9)">'
    b+=rect(0,0,520,266,'#f5f8fb', '#b0c5d5',12, 'filter="url(#shadow)"')
    b+=path('M40 80h440M40 180h440',BLUE,2,extra='opacity=".65"')
    for i in range(5):
        cx=78+i*88
        b+=path(f'M{cx} 80v41m-12 0h24m-24 12h24m-12 0v47',BLUE,2)
    b+='</g>'
# A compact terminal representation sits above the internal layers.
b+='<g transform="translate(176 202) skewY(-9)">'
b+=rect(120,49,282,150,'#eef4f8',NAVY,3)
b+=path('M40 88h80m282 0h78M40 159h80m282 0h78',NAVY,4)
for x,y in [(40,88),(480,88),(40,159),(480,159)]: b+=circle(x,y,6,'#f5f8fb',NAVY,2)
b+=text(259,138,'Zport',36,NAVY,'text-anchor="middle" font-style="italic"')
b+='</g>'
b+=path('M631 314 752 261M642 393 752 449',BLUE,1.5,extra='stroke-dasharray="4 7"')
# Magnified internal nodes: connected conductor segments, not random graph nodes.
b+=circle(858,351,141,'#f8fafb',NAVY,3, 'filter="url(#shadow)"')
b+=circle(858,351,126,'none','#c0d1de',1)
b+=path('M753 326h29c0-26 18-26 18 0 0-26 18-26 18 0h38c0-26 18-26 18 0 0-26 18-26 18 0h69M753 398h208',NAVY,3)
for x in [782,856,930]:
    b+=path(f'M{x} 326v29m-10 0h20m-20 10h20m-10 0v33',BLUE,2)
b+=circle(856,326,8,COPPER,'#f8fafb',3)
b+=path('M856 326v-51h53',COPPER,2.5)+text(914,282,'Vi',25,COPPER,'font-style="italic"')
b+=text(725,540,'WHAT MUST THE MODEL RETAIN?',16,NAVY,'letter-spacing="1.4"')
cover('machine-modeling-review.svg','Looking beyond the terminals','Conceptual layers of terminal and internal machine models, with a window onto an internal voltage observation point. Illustrates output-specific model selection, not a new measured circuit or validated internal response.',b,'03','OUTPUT-SPECIFIC MODEL SELECTION')

# 04: Paired HDL source panels around an eight-channel pair representation.
b=''
for x,y,angle in [(150,206,-7),(747,190,7)]:
    b+=f'<g transform="translate({x} {y}) rotate({angle} 140 160)">'
    b+=rect(0,0,280,312,'#f8fafb','#91adc3',10,'filter="url(#shadow)"')
    b+=path('M0 43h280',BLUE,1)
    b+=text(20,28,'HDL',15,NAVY,'letter-spacing="3"')
    b+=circle(254,24,4,COPPER,'none')
    for i in range(8):
        start=25+([0,18,36,36,18,36,18,0][i] if x<500 else [0,18,18,36,36,18,36,0][i])
        length=[150,126,88,130,155,102,116,65][i]
        if x>500: length=[169,108,144,85,121,149,95,72][i]
        b+=path(f'M{start} {78+i*27}h{length}',COPPER if i in (2,5) else BLUE,6)
    b+='</g>'
# One vector represents a code PAIR; layers depict numerical augmentation only.
b+=path('M414 318 492 352M784 306 705 352',BLUE,1.8,extra='stroke-dasharray="4 7"')
for offset in [28,14,0]:
    b+=rect(469+offset,283-offset,244,209,'#edf3f8','#b9ccda',8)
b+=rect(469,283,244,209,'#f9fbfc',NAVY,8,'filter="url(#shadow)"')
vals=[.38,.72,.52,.88,.63,.4,.77,.57]
for i,v in enumerate(vals):
    x=491+i*26
    b+=rect(x,314,13,137,'#e7eef4','none',3)
    b+=rect(x,451-v*137,13,v*137,COPPER if i in (2,5) else NAVY,'none',3)
b+=text(591,476,'8 STATIC FEATURES',13,NAVY,'text-anchor="middle" letter-spacing="1.5"')
b+=path('M492 536h199',BLUE,1.5)+text(591,568,'CODE-PAIR REPRESENTATION',17,NAVY,'text-anchor="middle" letter-spacing="2"')
cover('verilog-code-similarity.svg','Code beyond its surface','Two stylized HDL source panels feed one eight-feature code-pair representation. Repeated vector layers suggest numerical augmentation. Bar heights are illustrative; the separate random-control channel is omitted from this conceptual cover.',b,'04','HDL SIMILARITY / FEATURE ENGINEERING')
print('Wrote four editable SVG covers to', OUT)

