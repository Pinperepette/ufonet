#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
UFONet - DDoS attacks via Web Abuse - 2013/2014 - by psy (epsylon@riseup.net)

You should have received a copy of the GNU General Public License along
with UFONet; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import optparse

class UFONetOptions(optparse.OptionParser):
    def __init__(self, *args):
        optparse.OptionParser.__init__(self, 
                           description='\nUFONet - DDoS attacks via Web Abuse - 2013/2014 - by psy',
                           prog='UFONet.py',
                           version='\nUFONet v0.3 - Abduction\n')

        self.add_option("-v", "--verbose", action="store_true", dest="verbose", help="active verbose on requests")
        self.add_option("--check-tor", action="store_true", dest="checktor", help="check to see if Tor is used properly")
        self.add_option("--update", action="store_true", dest="update", help="check for latest stable version")

        group1 = optparse.OptionGroup(self, "*Configure Request(s)*")
        group1.add_option("--proxy", action="store", dest="proxy", help="Use proxy server (tor: http://localhost:8118)")
        group1.add_option("--user-agent", action="store", dest="agent", help="Use another HTTP User-Agent header (default SPOOFED)")
        group1.add_option("--referer", action="store", dest="referer", help="Use another HTTP Referer header (default SPOOFED)")
        group1.add_option("--host", action="store", dest="host", help="Use another HTTP Host header (default NONE)")
        group1.add_option("--xforw", action="store_true", dest="xforw", help="Set your HTTP X-Forwarded-For with random IP values")
        group1.add_option("--xclient", action="store_true", dest="xclient", help="Set your HTTP X-Client-IP with random IP values")
        group1.add_option("--timeout", action="store", dest="timeout", type="int", help="Select your timeout (default 30)")
        group1.add_option("--retries", action="store", dest="retries", type="int", help="Retries when the connection timeouts (default 1)")
        #group1.add_option("--threads", action="store", dest="threads", type="int", help="Maximum number of concurrent HTTP requests (default 5)") 
        group1.add_option("--delay", action="store", dest="delay", type="int", help="Delay in seconds between each HTTP request (default 0)")
        self.add_option_group(group1)

        group2 = optparse.OptionGroup(self, "*Manage Botnet*")
        group2.add_option("-s", action="store", dest="search", help="Search 'zombies' on google (ex: -s 'proxy.php?url=')")
        group2.add_option("--sn", action="store", dest="num_results", help="Set max number of result to search (default 10)")
        group2.add_option("-t", action="store", dest="test", help="Test list of web 'zombie' servers (ex: -t zombies.txt)")
        #group2.add_option("--tc", action="store", dest="testCSRF", help="Test only CSRF vulnerabilities on 'zombies'")
        #group2.add_option("--tx", action="store", dest="testXSS", help="Test only XSS vulnerabilities on 'zombies'")
        self.add_option_group(group2)

        group3 = optparse.OptionGroup(self, "*Configure Attack(s)*")
        group3.add_option("-r", action="store", dest="rounds", help="Set number of 'rounds' for the attack (default: 1)")
        group3.add_option("-b", action="store", dest="place", help="Set a place to 'bit' on target (ex: -b /path/big.jpg)")
        group3.add_option("-a", action="store", dest="target", help="Start a Web DDoS attack (ex: -a http(s)://target.com)")
        #group3.add_option("-s", action="store_true", dest="sniper", help="Set 'zombie snipers' Web DDoS attack")
        self.add_option_group(group3)

    def get_options(self, user_args=None):
        (options, args) = self.parse_args(user_args)
        if (not options.test and not options.target and not options.checktor and not options.search and not options.update):
            print '='*75, "\n"
            print "888     888 8888888888 .d88888b.  888b    888          888    "   
            print "888     888 888        d88P" "Y888b  8888b   888          888    "
            print "888     888 888       888     888 88888b  888          888    "
            print "888     888 8888888   888     888 888Y88b 888  .d88b.  888888 "
            print "888     888 888       888     888 888 Y88b888 d8P  Y8b 888    "
            print "888     888 888       888     888 888  Y88888 88888888 888    "
            print "Y88b. .d88P 888       Y88b. .d88P 888   Y8888 Y8b.     Y88b.  "
            print " 'Y88888P'  888        'Y88888P'  888    Y888  'Y8888   'Y8888"                                 
            print self.description, "\n"
            print '='*75, "\n"
            return False
        return options

