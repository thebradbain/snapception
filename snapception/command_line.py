import os
import json
import click
from subprocess import call

@click.command()
@click.option('--verbose', '-v', default=False, is_flag=True, help='Enable logging')
@click.option('--very-verbose', '-vv', default=False, is_flag=True, help='Include mitmdump in logging')
@click.option('--output', '-o', default='~/snaps', help='Specify output directory (Default is ~/snaps)')
@click.option('--port', '-p', default=8080, help='Specify port snapception runs on (Default is 8080)')
def launch(verbose, very_verbose, output, port):
	moduleDir = os.path.dirname(os.path.realpath(__file__)) + '/mitmdump_input.py'

	scriptArgs = dict(verbose=verbose or very_verbose, snapsDir=output, port=port)
	scriptFlag = '-s %s "%s"' % (moduleDir, scriptArgs)
	command = ['mitmdump', scriptFlag, '-q']

	if(very_verbose):
		command.remove('-q')
	if (port):
		command.append('-p ' + str(port))

	call(command)

if __name__ == '__main__':
	launch()