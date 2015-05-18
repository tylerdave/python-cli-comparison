import argparse_cli
import click_cli
import docopt_cli
import sys
from mock import Mock, patch
from nose.tools import assert_equal
from nose.plugins.skip import SkipTest

try:
    import builtins
except ImportError:
    import __builtin__
    builtins = __builtin__


class BaseCLITest(object):
    cli_module = Mock()

    @patch.object(builtins, 'print')
    @patch.object(sys, 'argv', ['__main__', 'pos_arg', '--optional-arg', 'optional_arg', '--flag'])
    def test_parses_all_arguments(self, mock_print):
        try:
            self.cli_module.cli()
        except SystemExit as e:
            if e.code != 0:
                raise
        call =  mock_print.call_args[0][0]

        assert_equal(call['positional'], 'pos_arg')
        assert_equal(call['optional'], 'optional_arg')
        assert_equal(call['flag'], True)

    @patch.object(sys, 'argv', ['__main__', '--help'])
    def test_prints_help(self):
        #self.cli_module.cli()
        raise SkipTest('TODO')

    @patch.object(sys, 'argv', ['__main__', '--version'])
    def test_prints_version(self):
        #self.cli_module.cli()
        raise SkipTest('TODO')



class TestArgparseCLI(BaseCLITest):
    cli_module = argparse_cli

class TestClickCLI(BaseCLITest):
    cli_module = click_cli

class TestDocoptCLI(BaseCLITest):
    cli_module = docopt_cli
