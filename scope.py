from typing import NewType
from enum import Enum, auto

maxNestLevel = 64

## Kind defines a kind
Kind = NewType('Kind', int)
Alias = NewType('Alias', int)

## Type defines the alias object type
Type = NewType('Type', Alias)

## Kinds of Kind
# Creating enumerations using class
class Kinds(Enum):
    KindVar = auto()
    KindParam = auto()  
    KindFunction = auto()
    KindField = auto()  
    KindArrayType = auto()
    KindStructType = auto()  
    KindAliasType = auto()
    KindScalarType = auto()  
    KindUniversal = auto()  
    KindUndefined = -1


def IsType(k):
	return k == Kinds.KindArrayType or k == Kinds.KindStructType or k == Kinds.KindAliasType or k == Kinds.KindScalarType


IntObj  = Object{-1, None, Kinds.KindScalarType, None}
PIntObj = &IntObj

CharObj  = Object{-1, None, Kinds.KindScalarType, None}
PCharObj = &CharObj

BoolObj  = Object{-1, None, Kinds.KindScalarType, None}
PBoolObj = &BoolObj

StringObj  = Object{-1, None, Kinds.KindScalarType, None}
PStringObj = &StringObj

UniversalObj  = Object{-1, None, Kinds.KindScalarType, None}
PUniversalObj = &UniversalObj


## Object defines a scope object
class Object:
	Name = None
	Next = None
	Kind = None

	## we use this to mimic the polymorphism the professor uses
	## on his compiler. shrug
	T = None

## Alias defines the alias object type
class Alias:
	BaseType = None
	Size = None

## Array defines the array object type
class Array:
	ElemType = None
	NumElements = None
	Size = None

## Struct defines the struct object type
class Struct:
	Fields = None
	Size = None

## Function defines the function object type
class Function:
	PRetType = None
	PParams = None
	Index = None
	Params = None
	Vars = None

## Var defines the var object type
class Var:
	PType = None
	Index = None
	Size = None

## Param defines the var object type
class Param:
    pass

## Field defines the var object type
class Field:
	PType  = None
	Index  = None
	Size  = None

## Analyser is the scope analyser
class Analyser:
	symbolTable = None
	level = None

## NewBlock opens a new block
def NewBlock(a):
	a.level+=1
	a.symbolTable[a.level] = None
	return a.level

## EndBlock ends a block
def EndBlock(a):
	a.level-=1
	return a.level

##// DefineSymbol defines a symbol given its name
def DefineSymbol(a, name):
	obj = &Object{}

	obj.Name = name
	obj.Kind = Kinds.KindUndefined
	obj.Next = a.symbolTable[a.level]
	a.symbolTable[a.level] = obj

	return obj

## SearchLocalSymbol searches for a symbol locally
def SearchLocalSymbol(a, name):
	obj = a.symbolTable[a.level]

	if obj != None:
		if obj.Name == name:
			return obj

		obj = obj.Next

	return obj

## SearchGlobalSymbol searches for a symbol globally
def SearchGlobalSymbol(a, name):
	for i in range (a.level,-1):
		obj = a.symbolTable[i]

		if obj != None:
			if obj.Name == name:
				return obj
			obj = obj.Next

	return obj

## CheckTypes returns true if objects are of same type
def CheckTypes(p1, p2):
	if p1 == p2:
		return true
	elif p1 == PUniversalObj or p2 == PUniversalObj:
		return true
	elif: p1.Kind == Kinds.KindUniversal or p2.Kind == Kinds.KindUniversal:
    	return true
	elif p1.Kind == Kinds.KindAliasType and p2.Kind != Kinds.KindAliasType:
		alias = p1.T
		return a.CheckTypes(alias.BaseType, p2)
	else if p1 Kind != Kinds.KindAliasType and p2.Kind == Kinds.KindAliasType:
		alias = p2.T
		return a.CheckTypes(p1, alias.BaseType)
	elif p1.Kind == p1.Kind:
		if p1.Kind == Kinds.KindAliasType:
			a1 = p1.T.(Alias)
			a2 = p2.T.(Alias)
			return a.CheckTypes(a1.BaseType, a2.BaseType)
		elif p1.Kind == Kinds.KindArrayType:
			a1 = p1.T.(Array)
			a2 = p2.T.(Array)
			if a1.NumElements == a2.NumElements:
				return a.CheckTypes(a1.ElemType, a2.ElemType)
        elif p1.Kind == Kinds.KindStructType:
			s1 = p1.T.(Struct)
			s2 = p2.T.(Struct)

			f1 = s1.Fields
			f2 = s2.Fields
			##if f1 != None and f2 != None {
			##	// TODO
			##}

	return false

def String(o):
	sb = ''
	sb += "Kind: {} Name: {} Type: ".format(o.Kind, o.Name)

	if type(o) == Alias:
		sb += 'Alias'
	elif type(o) == Type:
		sb += 'Type'
	elif type(o) == Array:
		sb += 'Array'
	elif type(o) == Struct:
		sb += 'Struct'
	elif type(o) == Function:
		sb += 'Function'
	elif type(o) == Var:
		sb += 'Var'
	elif type(o) == Param:
		sb += 'Param'
	elif type(o) == Field:
		sb += 'Field'
	default:
		sb += 'INVALID'
	}

	return sb
}
