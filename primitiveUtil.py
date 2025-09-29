import maya.cmds as cmds

def createobj(name,item):
	if item == "cone":
		cmds.polyCone(
			name = '{name}_geo'.format(name = name)
		)

	elif item == "cube":
		cmds.polyCube(
			name = '{name}_geo'.format(name = name)
		)

	elif item == "sphere":
		cmds.polySphere(
			name = '{name}_geo'.format(name = name)
		)

	elif item == "torus":
		cmds.polyTorus(
			name = '{name}_geo'.format(name = name)
		)
		
	else :
		return