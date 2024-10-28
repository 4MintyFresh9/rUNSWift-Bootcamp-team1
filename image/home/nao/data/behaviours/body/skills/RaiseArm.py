from util.actioncommand import raiseArm
from BehaviourTask import BehaviourTask

# credit to runswift website

class RaiseArm(BehaviourTask):
    def _tick(self):
        self.world.b_request.actions.body = raiseArm()
