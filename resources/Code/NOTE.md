## find active interface cmd
```
    networksetup -listallhardwareports
```
## tcpdump cmds

```
    tcpdump -G 60 -W 1 -w <protocolname>.pacp -i en0 -n dst host <ip> and dst port <port> and tcp --print
```
1. -G: rotate dump files in given x seconds.specify timeinterval of capture process
2. -W: limit of dump files
3. -i: specify interface
2.  -n:no reverse dns resolve to avoid disturbing information
3. filters:
    * dst host: specify destination host
    * dst port: specify destination port
    * tcp: only catch tcp data

4. --print: display realtime catch result
5. -w file: save caught packet to file for analyse

List of captured files
* obfsdump.pcap 
* shadowsocksdump.pcap
* naiveproxydump.pcap
* httpsdump.pcap


## Capture SSL Client Hello with tcpdump
To collection TLS Cipher Suite and other fingerprints, we should analyze the plaintext when negotiation happens.
```
    sudo tcpdump "tcp port <port> and (tcp[((tcp[12] & 0xf0) >>2)] = 0x16) && (tcp[((tcp[12] & 0xf0) >>2)+5] = 0x01)" -w client-hello.pcap
```
explanation see [here](https://www.baeldung.com/linux/tcpdump-capture-ssl-handshake)

in wireshark we can use such filter to display client hello
```
    ssl.handshake.type == 1
```

to capture Cipher Suite, we can use such filter
```
    ssl.handshake.ciphersuite
```
after that, we should process these data, since TLS is built upon TCP, we should retrieve tcp payload.
