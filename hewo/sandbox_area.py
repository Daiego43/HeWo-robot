from hewo.game.scenes.sandbox import SandBox
from hewo.game.characters.hewo.eye import Eye
from hewo.game.characters.hewo.mouth import Mouth
from hewo.game.characters.hewo.face import Face
from hewo.settings.settings_loader import SettingsLoader

display = SettingsLoader().load_settings('settings.display')
FULLSCREEN = display['fullscreen']
FOLLOW_MOUSE = False
TRACKING = False




if __name__ == '__main__':
    elements = [
        Face()
    ]
    sandbox = SandBox(elements, fullscreen=FULLSCREEN)
    sandbox.run()
