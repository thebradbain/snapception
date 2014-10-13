import os
import click
from subprocess import call

@click.command()
@click.option('--verbose', '-v', default=False, is_flag=True, help='Enable logging')
@click.option('--very-verbose', '-vv', default=False, is_flag=True, help='Include mitmdump in logging')
@click.option('--output', '-o', default='~/snaps', help='Specify output directory')
def main(verbose, very_verbose, output):
	moduleDir = os.path.dirname(os.path.realpath(__file__)) + '/mitmdump_input.py'

	scriptArg = '-s %s "%s %s"' % (moduleDir, '--verbose' if(verbose or very_verbose) else '', output)
	command = ['mitmdump', scriptArg, '-q']
	if(very_verbose):
		command.remove('-q')

	call(command)