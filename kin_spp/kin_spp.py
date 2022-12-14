from enum import IntFlag

class VersionNumber(IntFlag):
    DEFAULT = 0

class PacketType(IntFlag):
    TM = 0
    TC = 1

class SecondaryHeaderFlag(IntFlag):
    F = 0 
    T = 1

class ApplicationProcessIdentifier(IntFlag):
    GS = 0
    CS = 1
    PING = 2
    PONG = 0

class SequenceFlag(IntFlag):
    CS = 0
    FS = 1
    LS = 2
    US = 3

class SpacePacketProtocol(object):

    def __init__(self) -> None:

        self.header = self.Header()
        self.data = bytearray()

    class Header(object):

        def __init__(self,
                     versionNumber: VersionNumber = VersionNumber(0),
                     packetType: PacketType = PacketType(0),
                     secondaryHeaderFlag: SecondaryHeaderFlag = SecondaryHeaderFlag(0),
                     applicationProcessIdentifier: ApplicationProcessIdentifier = ApplicationProcessIdentifier(0),
                     sequenceFlag: SequenceFlag = SequenceFlag(0),
                     packetSequenceCount: int = 0,
                     packetDataLength: int = 0,
                     ) -> None:
        
            self.versionNumber = versionNumber
            self.packetIdentification = self.PacketIdentification(packetType, secondaryHeaderFlag, applicationProcessIdentifier)
            self.packetSequenceControl = self.PacketSequenceControl(sequenceFlag, packetSequenceCount)
            self.packetDataLength = packetDataLength

        class PacketIdentification(object):
            
            def __init__(self,
                         packetType: PacketType = PacketType(0),
                         secondaryHeaderFlag: SecondaryHeaderFlag = SecondaryHeaderFlag(0),
                         applicationProcessIdentifier: ApplicationProcessIdentifier = ApplicationProcessIdentifier(0),
                         ) -> None:

                self.packetType = packetType
                self.secondaryHeaderFlag = secondaryHeaderFlag
                self.applicationProcessIdentifier = applicationProcessIdentifier

        class PacketSequenceControl(object):

            def __init__(self,
                         sequenceFlag: SequenceFlag = SequenceFlag(0),
                         packetSequenceCount: int = 0,
                         ) -> None:

                self.sequenceFlag = sequenceFlag
                self.packetSequenceCount = packetSequenceCount

    def setHeader(self,
                  versionNumber: VersionNumber = VersionNumber(0),
                  packetType: PacketType = PacketType(0),
                  secondaryHeaderFlag: SecondaryHeaderFlag = SecondaryHeaderFlag(0),
                  applicationProcessIdentifier: ApplicationProcessIdentifier = ApplicationProcessIdentifier(0),
                  sequenceFlag: SequenceFlag = SequenceFlag(0),
                  packetSequenceCount: int = 0
                  ) -> None:

        self.header.versionNumber = versionNumber
        self.header.packetIdentification.packetType = packetType
        self.header.packetIdentification.secondaryHeaderFlag = secondaryHeaderFlag
        self.header.packetIdentification.applicationProcessIdentifier = applicationProcessIdentifier
        self.header.packetSequenceControl.sequenceFlag = sequenceFlag
        self.header.packetSequenceControl.packetSequenceCount = packetSequenceCount

    def setData(self, data) -> None:
        
        self.header.packetDataLength = len(data)
        self.data = data

    def toBuffer(self) -> bytearray:
        
        packetId = self.header.packetIdentification
        packetSC = self.header.packetSequenceControl

        headerPart1 = (self.header.versionNumber << 13 | packetId.packetType << 12 | packetId.secondaryHeaderFlag << 11 | packetId.applicationProcessIdentifier).to_bytes(2, 'big')
        headerPart2 = (packetSC.sequenceFlag << 14 | packetSC.packetSequenceCount).to_bytes(2, 'big')
        print(headerPart2)
        headerPart3 = packet.header.packetDataLength.to_bytes(2, 'big') 
        headerParts = bytearray(headerPart1) + bytearray(headerPart2) + bytearray(headerPart3)

        return headerParts + self.data

    def fromBuffer(self, buffer: bytearray) -> None:
        pass



if __name__ == "__main__":
    packet = SpacePacketProtocol()
    packet.setHeader(VersionNumber.DEFAULT, PacketType.TC, SecondaryHeaderFlag.F, ApplicationProcessIdentifier.GS | ApplicationProcessIdentifier.PONG, SequenceFlag.US, 0)
    packet.setData(b'pong')
    print(packet.toBuffer())
