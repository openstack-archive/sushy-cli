# -*- coding: utf-8 -*-

# Copyright 2010-2020 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sushy

from cliff import command
from cliff import lister


class BaseParserMixIn(object):

    def _add_options(self, parser):

        parser.add_argument(
            '--username',
            help='Redfish BMC username')

        parser.add_argument(
            '--password',
            help='Redfish BMC user password')

        parser.add_argument(
            '--service-endpoint',
            required=True,
            help='Redfish BMC service endpoint URL e.g. '
                 'http://localhost:8000')

        return parser

    def take_action(self, args):
        """Common command action"""

        root = sushy.Sushy(
            args.service_endpoint, username=args.username,
            password=args.password)

        return root


class BaseCommand(BaseParserMixIn, command.Command):
    """Common base for all sushycli commands"""

    def get_parser(self, prog_name):
        """Common command parser"""
        parser = super(BaseCommand, self).get_parser(prog_name)

        return self._add_options(parser)


class BaseLister(BaseParserMixIn, lister.Lister):
    """Common base for all sushycli listers"""

    def get_parser(self, prog_name):
        """Common lister parser"""
        parser = super(BaseLister, self).get_parser(prog_name)

        return self._add_options(parser)
