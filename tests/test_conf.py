#!/usr/bin/env python
# -*- coding: utf-8 -*-
from click.testing import CliRunner
import click
from click_conf import conf
from functools import partial
import yaml

runner = CliRunner()
invoke = partial(runner.invoke, catch_exceptions=False)


def test_click_no_conf():
    @click.command()
    @click.option('--arg')
    def cli(arg):
        print(arg)

    assert invoke(cli, ['--arg=argument1']).output == 'argument1\n'


def test_click_default_conf():
    @click.command()
    @click.option('--arg')
    @conf()
    def cli(arg):
        print(arg)

    assert invoke(cli, ['--arg=argument1']).output == 'argument1\n'


def test_click_with_default():
    @click.command()
    @click.option('--arg')
    @conf(default='click.yml')
    def cli(arg):
        print(arg)

    with runner.isolated_filesystem():
        with open('click.yml', 'w') as f:
            yaml.dump({"arg": "argument2"}, f)
        assert invoke(cli).output == 'argument2\n'
        assert invoke(cli, ['--arg=argument1']).output == 'argument1\n'
