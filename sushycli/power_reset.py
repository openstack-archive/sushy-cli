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


class PowerReset(command.Command):

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(PowerReset, self).get_parser(prog_name)

        parser.add_argument(
            '--user',
            dest='user',
            default='foo',
            help='The user or login for authentication')
        parser.add_argument(
            '--password',
            dest='password',
            default='bar',
            help='The password for authentication')
        parser.add_argument(
            '--rhost',
            dest='rhost',
            default='http://localhost:8000/redfish/v1/',
            help='The address of the Redfish service; defaults'
                 'to "http://localhost:8000/redfish/v1"')
        parser.add_argument(
            '--system',
            dest='system',
            default='437XR1138R2',
            help='The ID of the system')
        parser.add_argument(
            '--type',
            dest='power_mode',
            default='on',
            help='Specifying the type of action to perform'
                 '"reset/shutOff.."; default mode is ON')

        return parser

    def take_action(self, parsed_args):
        """Command action"""
        user = parsed_args.user
        password = parsed_args.password
        rhost = parsed_args.rhost
        system = parsed_args.system

        s = sushy.Sushy(rhost, username=user, password=password)

        sys_inst = s.get_system('/redfish/v1/Systems/%s' % system)

        sys_inst.reset_system(parsed_args.power_mode)
