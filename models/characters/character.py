import bge


def main(controller):
    character = controller.owner
    keyboard = bge.logic.keyboard

    if character.getActionFrame() == 40:
        character.playAction("jump", 0, 0)
        character.applyMovement((0, 2, 0), True)

    if not character.isPlayingAction():
        if keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE:
            character.playAction("jump", 0, 40, speed=1.5)
        elif keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE:
            character.applyRotation((0, 0, 1.570797), True)
            character.playAction("jump", 0, 40, speed=1.5)
        elif keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE:
            character.applyRotation((0, 0, -1.570797), True)
            character.playAction("jump", 0, 40, speed=1.5)


def shell(controller):
    scene = bge.logic.getCurrentScene()
    shell = controller.owner
    character = shell.parent
    near = controller.sensors["Near"]

    if near.positive:
        near.hitObject.color = (0.8, 0.2, 0.2, 1)
    else:
        #character.setVisible(False, True)
        scene.restart()
