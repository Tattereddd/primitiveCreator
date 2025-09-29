import maya.cmds as cmds

def renameobj(name, prims):
	print(name)

	for i in range(len(prims)):
		setname = '{name}{index:0>3}'