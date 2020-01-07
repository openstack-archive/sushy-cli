import logging

import sushy

from cliff.command import Command


class Version (Command):
    "A simple command that render the Redfish version."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Get the redfish version ..')
        self.log.debug('debugging')
        s = sushy.Sushy('http://localhost:8000/redfish/v1',
                username='foo', password='bar')
    
        return s.redfish_version