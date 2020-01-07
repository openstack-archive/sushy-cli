import logging

import sushy

from cliff import command

class PowerReset(command.Command):
    

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(PowerReset, self).get_parser(prog_name)

        parser.add_argument('--user',
                            dest='user',
                            default='foo',
                            help='The user or login for authentication')
        parser.add_argument('--password',
                            dest='password',
                            default='bar',
                            help='The password for authentication')
        parser.add_argument('--rhost',
                            dest='rhost',
                            default='http://localhost:8000/redfish/v1/',
                            help='The address of the Redfish service; defaults'
                                 +'to "http://localhost:8000/redfish/v1"')
        parser.add_argument('--system',
                            dest='system',
                            default='437XR1138R2',
                            help='The ID of the system')
        parser.add_argument('--type',
                            dest='power_mode',
                            default='on',
                            help='Specifying the type of action to perform'
                                 +'"reset/shutOff.."; default mode is ON')

        return parser


    def take_action(self, parsed_args):
        """Command action."""
        # Getting arguments 
        user = parsed_args.user
        password = parsed_args.password
        rhost = parsed_args.rhost
        system = parsed_args.system
        
        s = sushy.Sushy(rhost, username=user, password=password)
        # Instantiate a system object
        sys_inst = s.get_system('/redfish/v1/Systems/%s' %system)

        # Performing reset action with the specified reset type from --type argument
        sys_inst.reset_system(parsed_args.power_mode)