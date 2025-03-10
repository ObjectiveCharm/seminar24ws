
from typing import List
import dpkt

from pcap_analyse import PcapAnalyse

class PcapFingerprintAnalyse(PcapAnalyse):
    def __init__(self, pcap_file_name):
        super().__init__(pcap_file_name)

    @property
    def cipher_suite(self):
        return self._handshake_determined_cipher_suite(self.tcp_payload_with_timestamp)
    # NOTE: We should inspect the cipher suits as it is a significant characteristic of browser or other http client(e.g. curl)
    @staticmethod
    def _retrieve_client_cipher_suit_bytes(client_hello):
        # Since data and header are two component of data, we can use it to retrieve the cipher suit used by the client
        # The developer had retried the cipher suites, but not store it, so I copy the code here
        # See https://dpkt.readthedocs.io/en/latest/_modules/dpkt/ssl.html#TLSServerHello.unpack
        _, pointer = dpkt.ssl.parse_variable_array(client_hello.pack(), 1)
        cipher_suites, _ = dpkt.ssl.parse_variable_array(client_hello.data[pointer:], 2)
        return [cipher_suites[i:i + 4] for i in range(0, len(cipher_suites), 4)]
    @staticmethod
    def retrieve_client_cipher_suite(client_hello):
        codes = PcapFingerprintAnalyse._retrieve_client_cipher_suit_bytes(client_hello)
        cipher_suites = []
        for code in codes:
            cipher_suite = dpkt.ssl.ssl_ciphersuites.BY_CODE.get(code, None)
            if cipher_suite is not None:
                cipher_suites.append(cipher_suite)
        return cipher_suites

    @staticmethod
    def retrieve_server_cipher_suite(server_hello):
        cipher_suite = dpkt.ssl.ssl_ciphersuites.BY_CODE.get(server_hello.cipher_suite, None)
        return cipher_suite
    @staticmethod
    def retrieve_handshake(tcp_pkt):
        # Check for SSL packet
        hs = dpkt.ssl.TLSHandshake(tcp_pkt.data)
        if not isinstance(hs, dpkt.ssl.TLSHandshake):
            return None
        return hs

    """
        Source code for reference:
    
    
            [docs]
            class TLSUnknownHandshake(dpkt.Packet):
                __hdr__ = tuple()
    
    
    
            TLSServerKeyExchange = TLSUnknownHandshake
            TLSCertificateRequest = TLSUnknownHandshake
            TLSServerHelloDone = TLSUnknownHandshake
            TLSCertificateVerify = TLSUnknownHandshake
            TLSClientKeyExchange = TLSUnknownHandshake
            TLSFinished = TLSUnknownHandshake
    
    
            # mapping of handshake type ids to their names
            # and the classes that implement them
            HANDSHAKE_TYPES = {
                0: ('HelloRequest', TLSHelloRequest),
                1: ('ClientHello', TLSClientHello),
                2: ('ServerHello', TLSServerHello),
                11: ('Certificate', TLSCertificate),
                12: ('ServerKeyExchange', TLSServerKeyExchange),
                13: ('CertificateRequest', TLSCertificateRequest),
                14: ('ServerHelloDone', TLSServerHelloDone),
                15: ('CertificateVerify', TLSCertificateVerify),
                16: ('ClientKeyExchange', TLSClientKeyExchange),
                20: ('Finished', TLSFinished),
            }
        See https://dpkt.readthedocs.io/en/latest/_modules/dpkt/ssl.html#TLSUnknownHandshake
    """
    # Determine the cipher suit finally  used in the session
    @staticmethod
    def _handshake_determined_cipher_suite(payload_pkts):
        for _, pkt in payload_pkts:
            hs = dpkt.ssl.TLSHandshake(pkt)
            if not isinstance(hs, dpkt.ssl.TLSHandshake):
                print("Not a handshake packet")
                continue
            available_cipher_suites: List[dpkt.ssl.ssl_ciphersuites.CipherSuite] = []
            if hs.type == 1:
                available_cipher_suites = PcapFingerprintAnalyse.retrieve_client_cipher_suite(
                    dpkt.ssl.TLSClientHello(hs.pack()))
            elif hs.type == 2:
                server_choice = PcapFingerprintAnalyse.retrieve_server_cipher_suite(dpkt.ssl.TLSServerHello(hs.pack()))
                if server_choice in available_cipher_suites:
                    return server_choice
            else:
                # TODO: Better use __header__ attribute to get the type description. Currently, I don't know how to do it.
                hs_description = dpkt.ssl.HANDSHAKE_TYPES.get(hs.type, None)[0]
                print(f"Other handshake type {hs_description}")




