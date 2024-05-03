from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class VirtualReality(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set up the camera
        self.disableMouse()
        self.camLens.setNear(0.1)
        self.camLens.setFar(1000)
        self.camLens.setFov(60)

        # Set up the scene
        self.scene = self.loader.loadModel("models/scene.egg")
        self.scene.reparentTo(self.render)

        # Set up the task manager
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        # Update the scene
        dt = globalClock.getDt()
        self.scene.setPos(self.scene, 0, 0, -10 * math.sin(globalClock.getFrameTime()))

        return Task.cont

if __name__ == '__main__':
    app = VirtualReality()
    app.run()
