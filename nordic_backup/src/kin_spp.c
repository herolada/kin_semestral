/* @file kin_spp.c
 * @brief Source file of Space Packet Protocol implementation for KIN.
 *
 * @author Adam Herold
 * @author Daniel Stanc
 */

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#include "kin_spp.h"

void spp_set_header(spp_packet_t *packet, uint8_t version_number, uint8_t type, uint8_t sec_hdr_f, uint16_t apid, uint8_t seq_f, uint16_t seq_count) {

    packet->header.version_number = version_number;
    packet->header.id.type = type;
    packet->header.id.sec_hdr_f = sec_hdr_f;
    packet->header.id.apid = apid;
    packet->header.seq_ctrl.seq_f = seq_f;
    packet->header.seq_ctrl.seq_count = seq_count;

}

void spp_set_data(spp_packet_t *packet, uint16_t data_len, uint8_t *data) {

    packet->header.data_len = data_len;
    packet->data = data;

}

void spp_packet_to_buffer(spp_packet_t *packet, uint8_t *buf) {

    uint16_t packet_vn_id = 0;
    packet_vn_id = SPP_CHANGE_BITS(packet_vn_id, packet->header.version_number, 3, 15);
    packet_vn_id = SPP_CHANGE_BITS(packet_vn_id, packet->header.id.type, 1, 12);
    packet_vn_id = SPP_CHANGE_BITS(packet_vn_id, packet->header.id.sec_hdr_f, 1, 11);
    packet_vn_id = SPP_CHANGE_BITS(packet_vn_id, packet->header.id.apid, 11, 10);

    uint16_t packet_seq_ctrl = 0;
    packet_seq_ctrl = SPP_CHANGE_BITS(packet_seq_ctrl, packet->header.seq_ctrl.seq_f, 2, 15);
    packet_seq_ctrl = SPP_CHANGE_BITS(packet_seq_ctrl, packet->header.seq_ctrl.seq_count, 14, 13);

    uint16_t packet_data_len = packet->header.data_len;

    buf[0] = SPP_SPLIT_16_TO_8_U(packet_vn_id);
    buf[1] = SPP_SPLIT_16_TO_8_L(packet_vn_id);
    buf[2] = SPP_SPLIT_16_TO_8_U(packet_seq_ctrl);
    buf[3] = SPP_SPLIT_16_TO_8_U(packet_seq_ctrl);
    buf[4] = SPP_SPLIT_16_TO_8_U(packet_data_len);
    buf[5] = SPP_SPLIT_16_TO_8_U(packet_data_len);

    for (uint16_t i = 0; i < packet_data_len; i++) {

        buf[i+6] = packet->data[i];

    }

}

void spp_buffer_to_packet(spp_packet_t *packet, uint8_t *buf) {

    uint16_t packet_vn_id = SPP_JOIN_8_TO_16(buf[0], buf[1]);
    uint16_t packet_seq_ctrl = SPP_JOIN_8_TO_16(buf[2], buf[3]);
    uint16_t packet_data_len = SPP_JOIN_8_TO_16(buf[4], buf[5]);

    packet->header.version_number = SPP_EXTRACT_BITS(packet_vn_id, 3, 15);
    packet->header.id.type = SPP_EXTRACT_BITS(packet_vn_id, 1, 12);
    packet->header.id.sec_hdr_f = SPP_EXTRACT_BITS(packet_vn_id, 1, 11);
    packet->header.id.apid = SPP_EXTRACT_BITS(packet_vn_id, 11, 10);

    packet->header.seq_ctrl.seq_f = SPP_EXTRACT_BITS(packet_seq_ctrl, 2, 15);
    packet->header.seq_ctrl.seq_count = SPP_EXTRACT_BITS(packet_seq_ctrl, 14, 13);

    packet->header.data_len = packet_data_len;

    for (uint16_t i = 0; i < packet_data_len; i++) {

        packet->data[i] = buf[i+6];

    }

}

void spp_print_packet_as_buffer(spp_packet_t *packet) {

    uint8_t buf[SPP_PACKET_LEN];
    
    spp_packet_to_buffer(packet, &buf[0]);

    for (int i = 0; i < (packet->header.data_len + SPP_HEADER_LEN); i++) {
    
        printf("%x ", buf[i]);

    }

    printf("\n");

}

void spp_pretty_print_packet(spp_packet_t *packet){

    printf("Packet Header:\n\
            Packet Version Number: %x\n\
            Packet Identification:\n\
            \tPacket Type: %x\n\
            \tSecondary Header Flag: %x\n\
            \tApplication Process Identifier: %x\n\
            Packet Sequence Control:\n\
            \tSequence Flags: %x\n\
            \tPacket Sequence Count/Name: %x\n\
            Packet Data Length: %d\n\
            \rPacket Data:\n\t\t",
            packet->header.version_number, packet->header.id.type, 
            packet->header.id.sec_hdr_f, packet->header.id.apid,
            packet->header.seq_ctrl.seq_f, packet->header.seq_ctrl.seq_count,
            packet->header.data_len);

    for (int i = 0; i < (packet->header.data_len); i++) {
    
        printf("%x ", packet->data[i]);

    }

    printf("\n");

}
