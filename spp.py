class SpacePacketProtocolSender():

    def __init__(self,
                version_num='000',
                packet_type='0',
                sec_header_flag='0',
                apids=None,
                is_unsegmented = False,
                data=""):

        if type(data) == 'str':
            self.data = data.encode("utf8")
        elif type(data) == 'bytes':
            self.data = data
        else:
            raise(Exception("wrong data type to send {}".format(type(data))))
        self.header = None

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


    def data2packets(self):
        self.packets = []
        self.seq_count = 0
        while len(self.data) > 0:
            if len(self.data) > 65536:
                self.packet_data = self.data[:65536]
                self.data = self.data[65536:]
            else:
                self.packet_data = self.data[:]
                self.data = b''
            self.data_len = len(self.packet_data-1)
            self.seq_count_bitstr = format(self.seq_count, '014b')

            if self.is_unsegmented:
                self.seq_flags = '11'
            elif not self.packets:    # first packet
                self.seq_flags = '01'
            elif not self.data:
                self.seq_flags = '10'
            else:
                self.seq_flags = '00'
            
            self.header = self.get_header()
            self.packet = self.header + self.data

            self.packets.append(self.packet)

            self.seq_count += 1
            self.seq_count %= 16384

    def get_header(self):
        version_num = self.version_num
        identification = self.packet_type + self.sec_header_flag + self.apids['ground_station']
        seq_control = self.seq_flags + self.seq_count_bitstr
        data_len = self.data_len

        header = version_num + identification + seq_control + data_len
        return header

class SpacePacketProtocolSender():

    def __init__(self, version_num='000', packet=None, data=None):
        self.packet = packet
        self.data = data
        self.header = None

        self.version_num = list(version_num)

    def data2packet(self):
        self.header = self.generate_header()
        self.packet = self.header + self.data

    def generate_header(self):
        version_num = self.version_num
        identification = packet_type + self.second_header_flag + self.apids['ground_station']

    def packet2data(self):
