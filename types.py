class Attribute:
	Type = None
	Size = None
	Attribute = None

def String(a):
	if type(a) is ID:
		return 'ID'
	elif type(a) is T:
		return 'T'
	elif type(a) is E:
		return 'E'
	elif type(a) is L:
		return 'L'
	elif type(a) is R:
		return 'R'
	elif type(a) is Y:
		return 'Y'
	elif type(a) is F:
		return 'F'
	elif type(a) is LV:
		return 'LV'
	elif type(a) is MC:
		return 'MC'
	elif type(a) is MT:
		return 'MT'
	elif type(a) is ME:
		return 'ME'
	elif type(a) is MW:
		return 'MW'
	elif type(a) is MA:
		return 'MA'
	elif type(a) is LE:
		return 'LE'
	elif type(a) is LI:
		return 'LI'
	elif type(a) is DC:
		return 'DC'
	elif type(a) is LP:
		return 'LP'
	elif type(a) is TRUE:
		return 'TRUE'
	elif type(a) is FALSE:
		return 'FALSE'
	elif type(a) is CHR:
		return 'CHR'
	elif type(a) is STR:
		return 'STR'
	elif type(a) is NUM:
		return 'NUM'

	return ''

class ID:
    Object = None
    Name = None

class T:
    Type = None

class E:
    Type = None

class L:
	Type = None

class R:
	Type = None

class Y:
	Type = None

class F:
   	Type = None

class LV:
	Type = None

class MC:
    Type = None
    Param = None
    Err = None

class MT:
	Label = None

class ME:
	Label = None

class MW:
	Label = None

class MA:
	Label = None

class LE:
	Type = None
	Param = None
	Err = None
	N = None

class LI:
	List = None

class DC:
	List = None

class LP:
   	List = None

class TRUE:
	Type = None
	Val = None

class FALSE:
	Type = None
	Val = None

class CHR:
    Type = None
    Pos = None
    Val = None

class STR:
	Type = None
	Pos = None
	Val = None

class NUM:
	Type = None
	Pos = None
	Val = None

IDDStatic = Attribute()
IDUStatic = Attribute()
IDStatic = Attribute()
TStatic = Attribute()
LIStatic = Attribute()
LI0Static = Attribute()
LI1Static = Attribute()
TRUStatic = Attribute()
FALSStatic = Attribute()
STRStatic = Attribute()
CHRStatic = Attribute()
NUMStatic = Attribute()
DCStatic = Attribute()
DC0Static = Attribute()
DC1Static = Attribute()
LPStatic = Attribute()
LP0Static = Attribute()
LP1Static = Attribute()
EStatic = Attribute()
E0Static = Attribute()
E1Static = Attribute()
LStatic = Attribute()
L0Static = Attribute()
L1Static = Attribute()
RStatic = Attribute()
R0Static = Attribute()
R1Static = Attribute()
YStatic = Attribute()
Y0Static = Attribute()
Y1Static = Attribute()
FStatic = Attribute()
F0Static = Attribute()
F1Static = Attribute()
LVStatic = Attribute()
LV0Static = Attribute()
LV1Static = Attribute()
MCStatic = Attribute()
LEStatic = Attribute()
LE0Static = Attribute()
LE1Static = Attribute()
MTStatic = Attribute()
MEStatic = Attribute()
MWStatic = Attribute()
NBStatic = Attribute()

IDDStatic.Attribute = ID()
IDUStatic.Attribute = ID()
IDStatic.Attribute = ID()
TStatic.Attribute = T()
LIStatic.Attribute = LI()
LI0Static.Attribute = LI()
LI1Static.Attribute = LI()
TRUStatic.Attribute = TRUE()
FALSStatic.Attribute = FALSE()
STRStatic.Attribute = STR()
CHRStatic.Attribute = CHR()
NUMStatic.Attribute = NUM()
DCStatic.Attribute = DC()
DC0Static.Attribute = DC()
DC1Static.Attribute = DC()
LPStatic.Attribute = LP()
LP0Static.Attribute = LP()
LP1Static.Attribute = LP()
EStatic.Attribute = E()
E0Static.Attribute = E()
E1Static.Attribute = E()
LStatic.Attribute = L()
L0Static.Attribute = L()
L1Static.Attribute = L()
RStatic.Attribute = R()
R0Static.Attribute = R()
R1Static.Attribute = R()
YStatic.Attribute = Y()
Y0Static.Attribute = Y()
Y1Static.Attribute = Y()
FStatic.Attribute = F()
F0Static.Attribute = F()
F1Static.Attribute = F()
LVStatic.Attribute = LV()
LV0Static.Attribute = LV()
LV1Static.Attribute = LV()
MCStatic.Attribute = MC()
LEStatic.Attribute = LE()
LE0Static.Attribute = LE()
LE1Static.Attribute = LE()
MTStatic.Attribute = MT()
MEStatic.Attribute = ME()
MWStatic.Attribute = MW()
