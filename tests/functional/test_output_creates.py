from os import path
from nose import tools

from tests.functional import single_machine_test

parent_dir = path.dirname(__file__)

output_spec    = '%s/single_machine_outputs.nix'    % (parent_dir)

class TestOutputCreates(single_machine_test.SingleMachineTest):
    _multiprocess_can_split_ = True

    def setup(self):
        super(TestOutputCreates,self).setup()
        self.depl.nix_exprs = self.depl.nix_exprs + [ output_spec ]

    def run_check(self):
        self.depl.deploy()
        assert "\"12345\"" == self.depl.machines["machine"].run_command("cat /etc/test.txt",capture_stdout=True), "Resource contents incorrect"