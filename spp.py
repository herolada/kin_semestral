class SpacePacketProtocol():

    _APIDS = {'ground_station':'00000000000',
        'satellite':'00000000001'}

    _HEADER_LEN = 6
    
    def __init__(self,
                version_num='000',
                packet_type='0',
                sec_header_flag='0',
                apids=None,
                is_unsegmented = False,
                ):

        self.version_num = version_num
        self.packet_type = packet_type
        self.sec_header_flag = sec_header_flag
        self.is_unsegmented = is_unsegmented

        if apids is None:
            self.apids = self._APIDS
        else:
            self.apids = apids

    def set_header_vars(self,
                version_num='000',
                packet_type='0',
                sec_header_flag='0',
                apids=None,
                is_unsegmented = False,
                ):

        self.version_num = version_num
        self.packet_type = packet_type
        self.sec_header_flag = sec_header_flag
        self.is_unsegmented = is_unsegmented

        APIDS = {'ground_station':'00000000000',
        'satellite':'00000000001'}
        if apids is None:
            self.apids = APIDS
        else:
            self.apids = apids

    def data2packets(self,data):

        if isinstance(data,str):
            data = data.encode("utf8")
        elif isinstance(data,bytes):
            pass
        else:
            raise(Exception("wrong data type to send {}".format(type(data))))
        self.header = None

        packets = []
        self.seq_count = 0
        while len(data) > 0:
            if len(data) > 65536:
                packet_data = data[:65536]
                data = data[65536:]
            else:
                packet_data = data[:]
                data = b''
            self.data_len = bin((len(packet_data)-1)).lstrip('0b')
            self.data_len = self.data_len.rjust(16, '0')
            self.seq_count_bitstr = format(self.seq_count, '014b')

            if self.is_unsegmented:
                self.seq_flags = '11'
            elif not packets:    # TODO fix for multiple uses
                self.seq_flags = '01'
            elif not data:
                self.seq_flags = '10'
            else:
                self.seq_flags = '00'
            
            self.header = self._get_header()
            self.header_bytes = int(self.header, 2).to_bytes(len(self.header) // 8, byteorder='big')  # HEADER LENGTH HAS TO BE MULTIPLICATIVE OF 8
            self.packet = self.header_bytes + packet_data

            packets.append(self.packet)

            self.seq_count += 1
            self.seq_count %= 16384

        return packets

    def packets2data(self,packets):
        data = bytearray()
        for packet in packets:
            header = packet[:self._HEADER_LEN]
            packet_data = packet[self._HEADER_LEN:]
            data.extend(packet_data)

        #header_params = self.parse_header(header)

        return data#header_params,data


    def parse_header(self,header):
        header_ints = [x for x in header]
        header_strings = [format(x, '08b') for x in header_ints]
        header_str = ''.join(header_strings)

        header_params = {}

        header_params['version_num'] =      header_str[0:3]
        header_params['packet_type'] =      header_str[3:4]
        header_params['sec_header_flag'] =  header_str[4:5]
        header_params['apid'] =             header_str[5:16]
        header_params['seq_flags'] =        header_str[16:18]
        header_params['seq_count_bitstr'] = header_str[18:32]
        header_params['data_len'] =         header_str[32:48]

        return header_params

    def _get_header(self):
        version_num = self.version_num
        identification = self.packet_type + self.sec_header_flag + self.apids['ground_station']
        seq_control = self.seq_flags + self.seq_count_bitstr
        data_len = self.data_len

        header = version_num + identification + seq_control + data_len
        return header




if __name__ == "__main__":

    with open("image.jpg","rb") as f:
        data = f.read()

    spp = SpacePacketProtocol()
    packets = spp.data2packets(data)

    received_data = spp.packets2data(packets)
    
    with open("received_image.jpg", "wb") as binary_file:
        binary_file.write(received_data)









""" class SpacePacketProtocol():

    _APIDS = {'ground_station':'00000000000',
        'satellite':'00000000001'}

    _HEADER_LEN = 6
    
    def __init__(self,
                version_num='000',
                packet_type='0',
                sec_header_flag='0',
                apids=None,
                is_unsegmented = False,
                ):

        self.version_num = version_num
        self.packet_type = packet_type
        self.sec_header_flag = sec_header_flag
        self.is_unsegmented = is_unsegmented

        if apids is None:
            self.apids = self._APIDS
        else:
            self.apids = apids

    def set_header_vars(self,
                version_num='000',
                packet_type='0',
                sec_header_flag='0',
                apids=None,
                is_unsegmented = False,
                ):

        self.version_num = version_num
        self.packet_type = packet_type
        self.sec_header_flag = sec_header_flag
        self.is_unsegmented = is_unsegmented

        APIDS = {'ground_station':'00000000000',
        'satellite':'00000000001'}
        if apids is None:
            self.apids = APIDS
        else:
            self.apids = apids

    def data2packets(self,data):

        if isinstance(data,str):
            data = data.encode("utf8")
        elif isinstance(data,bytes):
            pass
        else:
            raise(Exception("wrong data type to send {}".format(type(data))))
        self.header = None

        packets = []
        self.seq_count = 0
        while len(data) > 0:
            if len(data) > 65536:
                self.packet_data = data[:65536]
                data = data[65536:]
            else:
                self.packet_data = data[:]
                data = b''
            self.data_len = bin((len(self.packet_data)-1)).lstrip('0b')
            self.data_len = self.data_len.rjust(16, '0')
            self.seq_count_bitstr = format(self.seq_count, '014b')

            if self.is_unsegmented:
                self.seq_flags = '11'
            elif not packets:    # TODO fix for multiple uses
                self.seq_flags = '01'
            elif not data:
                self.seq_flags = '10'
            else:
                self.seq_flags = '00'
            
            self.header = self._get_header()
            self.header_bytes = int(self.header, 2).to_bytes(len(self.header) // 8, byteorder='big')  # HEADER LENGTH HAS TO BE MULTIPLICATIVE OF 8
            self.packet = self.header_bytes + data

            packets.append(self.packet)

            self.seq_count += 1
            self.seq_count %= 16384

        return packets

    def _get_header(self):
        version_num = self.version_num
        identification = self.packet_type + self.sec_header_flag + self.apids['ground_station']
        seq_control = self.seq_flags + self.seq_count_bitstr
        data_len = self.data_len

        header = version_num + identification + seq_control + data_len
        return header """