# -*- coding: utf-8 -*-

# Copyright 2020 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

import sushy

from sushycli.cmd.sushycli import main
from sushycli.tests.unit import base


@mock.patch.object(sushy, 'Sushy', autospec=True)
class SuchyCliTestCase(base.TestCase):

    @mock.patch('sys.stdout.write', autospec=True)
    def test_version(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_root.redfish_version = '1.2.3'

        main(['version', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calls = [
            mock.call('+---------+\n'
                      '| Version |'
                      '\n+---------+\n'
                      '| 1.2.3   |\n'
                      '+---------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calls)

    @mock.patch('sys.stdout.write', autospec=True)
    def test_chassis_inventory_show(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_one_chassis = mock_root.get_chassis.return_value

        mock_one_chassis.identity = 'A'
        mock_one_chassis.name = 'B'
        mock_one_chassis.description = 'C'
        mock_one_chassis.manufacturer = 'D'
        mock_one_chassis.part_number = 'E'
        mock_one_chassis.serial_number = 'F'
        mock_one_chassis.sku = 'G'
        mock_one_chassis.asset_tag = 'H'
        mock_one_chassis.oem_vendors = ['I', 'J']

        main(['chassis', 'inventory', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--chassis-id', '/redfish/v1/Chassis/1U'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calls = [
            mock.call('+----------+------+-------------+--------------+-----'
                      '--------+---------------+-----+-----------+----------'
                      '---+\n| Identity | Name | Description | Manufacturer '
                      '| Part Number | Serial Number | SKU | Asset Tag | OEM'
                      ' Vendors |\n+----------+------+-------------+--------'
                      '------+-------------+---------------+-----+----------'
                      '-+-------------+\n| A        | B    | C           | D'
                      '            | E           | F             | G   | H  '
                      '       | I, J        |\n+----------+------+----------'
                      '---+--------------+-------------+---------------+----'
                      '-+-----------+-------------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calls)

    @mock.patch('sys.stdout.write', autospec=True)
    def test_manager_inventory_show(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_manager = mock_root.get_manager.return_value

        mock_manager.identity = 'A'
        mock_manager.name = 'B'
        mock_manager.description = 'C'
        mock_manager.manufacturer = 'D'
        mock_manager.part_number = 'E'
        mock_manager.serial_number = 'F'
        mock_manager.sku = 'G'
        mock_manager.asset_tag = 'H'
        mock_manager.oem_vendors = ['I', 'J']

        main(['manager', 'inventory', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--manager-id', '/redfish/v1/Mnagers/BMC'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calls = [

            mock.call('+----------+------+-------------+-------------+\n| Id'
                      'entity | Name | Description | OEM Vendors |\n+-------'
                      '---+------+-------------+-------------+\n| A        |'
                      ' B    | C           | I, J        |\n+----------+----'
                      '--+-------------+-------------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calls)

    @mock.patch('sys.stdout.write', autospec=True)
    def test_system_inventory_show(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_system = mock_root.get_system.return_value

        mock_system.identity = 'A'
        mock_system.name = 'B'
        mock_system.description = 'C'
        mock_system.manufacturer = 'D'
        mock_system.part_number = 'E'
        mock_system.serial_number = 'F'
        mock_system.sku = 'G'
        mock_system.asset_tag = 'H'
        mock_system.oem_vendors = ['I', 'J']

        main(['system', 'inventory', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calls = [
            mock.call('+----------+------+-------------+--------------+-----'
                      '--------+---------------+-----+-----------+----------'
                      '---+\n| Identity | Name | Description | Manufacturer '
                      '| Part Number | Serial Number | SKU | Asset Tag | OEM'
                      ' Vendors |\n+----------+------+-------------+--------'
                      '------+-------------+---------------+-----+----------'
                      '-+-------------+\n| A        | B    | C           | D'
                      '            | E           | F             | G   | H  '
                      '       | I, J        |\n+----------+------+----------'
                      '---+--------------+-------------+---------------+----'
                      '-+-----------+-------------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calls)

    @mock.patch('sys.stdout.write', autospec=True)
    def test_system_power_show(self, mock_write, mock_sushy):

        mock_root = mock_sushy.return_value

        mock_system = mock_root.get_system.return_value

        mock_system.power_state = 'on'

        main(['system', 'power', 'show',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        expected_calls = [
            mock.call('+-------------+\n'
                      '| Power state |\n'
                      '+-------------+\n'
                      '| on          |\n'
                      '+-------------+'),
            mock.call('\n')
        ]

        mock_write.assert_has_calls(expected_calls)

    def test_system_power_on(self, mock_sushy):

        main(['system', 'power',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1',
              'on'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        mock_root = mock_sushy.return_value

        mock_root.get_system.assert_called_once_with(
            '/redfish/v1/Systems/1')

        mock_system = mock_root.get_system.return_value

        mock_system.reset_system.assert_called_once_with('on')

    def test_system_power_off(self, mock_sushy):

        main(['system', 'power',
              '--username', 'jelly', '--password', 'fish',
              '--service-endpoint', 'http://fish.me',
              '--system-id', '/redfish/v1/Systems/1',
              'Off'])

        mock_sushy.assert_called_once_with(
            'http://fish.me', password='fish', username='jelly')

        mock_root = mock_sushy.return_value

        mock_root.get_system.assert_called_once_with(
            '/redfish/v1/Systems/1')

        mock_system = mock_root.get_system.return_value

        mock_system.reset_system.assert_called_once_with('force off')
