<p>
<p align="center"><a href="https://camo.githubusercontent.com/2516ec0b94ffad5f83ab316d576e03bc5dd68fd0/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f77696669706869736865722e706e67" target="_blank"><img style="max-width: 100%;" src="https://camo.githubusercontent.com/2516ec0b94ffad5f83ab316d576e03bc5dd68fd0/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f77696669706869736865722e706e67" alt="" /></a></p>
<h2>About</h2>
<p>Wifiphisher is a security tool that mounts automated phishing attacks
 against WiFi networks in order to obtain secret passphrases or other 
credentials. It is a social engineering attack that unlike other methods
 it does not include any brute forcing. It is an easy way for obtaining 
credentials from captive portals and third party login pages or WPA/WPA2
 secret passphrases.</p>
<p>Wifiphisher works on Kali Linux and is licensed under the MIT license.</p>
<h2>How it works</h2>
<p>After achieving a man-in-the-middle position using the Evil Twin 
attack, wifiphisher redirects all HTTP requests to an 
attacker-controlled look-alike web site.</p>
<p>From the victim's perspective, the attack makes use in three phases:</p>
<ol>
<li><strong>Victim is being deauthenticated from her access point</strong>.
 Wifiphisher continuously jams all of the target access point's wifi 
devices within range by forging &ldquo;Deauthenticate&rdquo; or &ldquo;Disassociate&rdquo; 
packets to disrupt existing associations.</li>
<li><strong>Victim joins a rogue access point</strong>. Wifiphisher 
sniffs the area and copies the target access point's settings. It then 
creates a rogue wireless access point that is modeled by the target. It 
also sets up a NAT/DHCP server and forwards the right ports. 
Consequently, because of the jamming, clients will start connecting to 
the rogue access point. After this phase, the victim is MiTMed.</li>
<li><strong>Victim is being served a realistic router config-looking page</strong>.
 wifiphisher employs a minimal web server that responds to HTTP &amp; 
HTTPS requests. As soon as the victim requests a page from the Internet,
 wifiphisher will respond with a realistic fake page that asks for 
credentials. The tool supports community-built templates for different 
phishing scenarios, such as:

<ul>
<li>Router configuration pages that ask for the WPA/WPA2 passphrase due to a router firmware upgrade.</li>
<li>3rd party login pages (for example, login pages similar to those of 
popular social networking or e-mail access sites and products)</li>
<li>Captive portals, like the ones that are being used by hotels and airports.</li>
</ul>
</li>
</ol>
<p align="center"><a href="https://camo.githubusercontent.com/527bf73d81ccb73d4f02899da1958f821a5c170a/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f6469616772616d2e6a7067" target="_blank"><img style="max-width: 100%;" src="https://camo.githubusercontent.com/527bf73d81ccb73d4f02899da1958f821a5c170a/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f6469616772616d2e6a7067" alt="" width="70%" /></a><br /><em>Performing MiTM attack</em></p>
<h2>Usage</h2>
<table border="0">
<thead> 
<tr>
<th align="center">Short form</th> <th align="center">Long form</th> <th align="center">Explanation</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">-m</td>
<td align="center">maximum</td>
<td align="center">Choose the maximum number of clients to deauth. List 
of clients will be emptied and repopulated after hitting the limit. 
Example: -m 5</td>
</tr>
<tr>
<td align="center">-n</td>
<td align="center">noupdate</td>
<td align="center">Do not clear the deauth list when the maximum (-m) 
number of client/AP combos is reached. Must be used in conjunction with 
-m. Example: -m 10 -n</td>
</tr>
<tr>
<td align="center">-t</td>
<td align="center">timeinterval</td>
<td align="center">Choose the time interval between packets being sent. 
Default is as fast as possible. If you see scapy errors like 'no buffer 
space' try: -t .00001</td>
</tr>
<tr>
<td align="center">-p</td>
<td align="center">packets</td>
<td align="center">Choose the number of packets to send in each deauth 
burst. Default value is 1; 1 packet to the client and 1 packet to the 
AP. Send 2 deauth packets to the client and 2 deauth packets to the AP: 
-p 2</td>
</tr>
<tr>
<td align="center">-d</td>
<td align="center">directedonly</td>
<td align="center">Skip the deauthentication packets to the broadcast address of the access points and only send them to client/AP pairs</td>
</tr>
<tr>
<td align="center">-a</td>
<td align="center">accesspoint</td>
<td align="center">Enter the MAC address of a specific access point to target</td>
</tr>
<tr>
<td align="center">-jI</td>
<td align="center">jamminginterface</td>
<td align="center">Choose the interface for jamming. By default script will find the most powerful interface and starts monitor mode on it.</td>
</tr>
<tr>
<td align="center">-aI</td>
<td align="center">apinterface</td>
<td align="center">Choose the interface for the fake AP.  By default 
script will find the second most powerful interface and starts monitor 
mode on it.</td>
</tr>
</tbody>
</table>
<h2>Screenshots</h2>
<p align="center"><a href="https://camo.githubusercontent.com/e68dceef317be30d570addcbdff1e7235a63ef3a/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373312e706e67" target="_blank"><img style="max-width: 100%;" src="https://camo.githubusercontent.com/e68dceef317be30d570addcbdff1e7235a63ef3a/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373312e706e67" alt="" /></a><br /><em>Targeting an access point</em></p>
<p align="center"><a href="https://camo.githubusercontent.com/edac2b531e778d7c1e899743e5aecda7e322e1b5/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373322e706e67" target="_blank"><img style="max-width: 100%;" src="https://camo.githubusercontent.com/edac2b531e778d7c1e899743e5aecda7e322e1b5/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373322e706e67" alt="" /></a><br /><em>A successful attack</em></p>
<p align="center"><a href="https://camo.githubusercontent.com/ea77ec050e0f40d9de2c0766d0e790a0171f50c1/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373332e706e67" target="_blank"><img style="max-width: 100%;" src="https://camo.githubusercontent.com/ea77ec050e0f40d9de2c0766d0e790a0171f50c1/68747470733a2f2f736f7068726f6e2e6769746875622e696f2f77696669706869736865722f7373332e706e67" alt="" /></a><br /><em>Fake router configuration page</em></p>
<h2>Requirements</h2>
<ul>
<li>Kali Linux.</li>
<li>Two wireless network adapters; one capable of injection.</li>
</ul>
<h2>Help needed</h2>
<p>If you are a Python developer or a web designer you can help us 
improve wifiphisher. Feel free to take a look at the bug tracker for 
some tasks to do.</p>
<h2>Credits</h2>
<p>The script is based on an idea from <a href="https://github.com/DanMcInerney">Dan McInerney</a>. The parts for the
jamming and selecting an AP have also been taken from his scripts <a href="https://github.com/DanMcInerney/wifijammer">wifijammer</a> and <a href="https://github.com/DanMcInerney/fakeAP">fakeAP</a>.</p>
<h2>License</h2>
<p>Wifiphisher is licensed under the MIT license. See <a href="https://github.com/hacker404/WifiPhisher/LICENSE">LICENSE</a> for more information.</p>
<h2>Project Status</h2>
<p>Wifiphisher's current version is <strong>1.1</strong>.</p>
<h2>Other resources</h2>
<ul>
<li>Slides from &ldquo;Introducing wifiphisher&ldquo; talk at BsidesLondon: <a href="https://sophron.latthi.com/talks/bsideslondon15-wifiphisher.pdf">https://sophron.latthi.com/talks/bsideslondon15-wifiphisher.pdf</a></li>
<li>HowTo video by JackkTutorials: <a href="https://www.youtube.com/watch?v=tCwclyurB8I">https://www.youtube.com/watch?v=tCwclyurB8I</a></li>
</ul>
<p><a href="http://www.twitter.com/hacker404"><img style="max-width: 100%;" title="Follow me" src="https://camo.githubusercontent.com/7cf10772eb6ccebe92d678c452a971e6e2778653/687474703a2f2f692e696d6775722e636f6d2f7458536f5468462e706e67" alt="alt text" /></a></p>
</p>
