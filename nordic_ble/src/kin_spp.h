/* @file kin_spp.h
 * @brief Header file of Space Packet Protocol implementation for KIN.
 *
 * @author Adam Herold
 * @author Daniel Stanc
 *
 */

#ifndef KIN_SPP_H
#define KIN_SPP_H

#include <stdint.h>

/* SPP Buffer Lengths*/

#define SPP_DATA_LEN_MAX    65535
#define SPP_DATA_LEN        4
#define SPP_HEADER_LEN      6
#define SPP_PACKET_LEN_MAX  (SPP_HEADER_LEN + SPP_DATA_LEN_MAX)
#define SPP_PACKET_LEN      (SPP_HEADER_LEN + SPP_DATA_LEN)

/* SPP Bits Manipulation */

#define SPP_ONES_MASK(n)                                ((1 << (n)) - 1)
#define SPP_CHANGE_BITS(value, bits, length, position)  ((value & ~(SPP_ONES_MASK(length) << (position + 1 - length))) | (bits << (position + 1 - length)))
#define SPP_EXTRACT_BITS(value, length, position)       (SPP_ONES_MASK(length) & (value >> (position + 1 - length)))

#define SPP_SPLIT_16_TO_8_U(value)      ((uint8_t)((value >> 8) & 0xFF))
#define SPP_SPLIT_16_TO_8_L(value)      ((uint8_t)((value) & 0xFF))
#define SPP_JOIN_8_TO_16(upper, lower)  ((uint16_t)(((upper << 8) & 0xff00) | (lower & 0xff)))

/* SPP Packet Header Constants */

#define SPP_VERSION_NUMBER 0x0

#define SPP_TYPE_TM 0x0 // Telemetry
#define SPP_TYPE_TC 0x1 // Telecommand

#define SPP_SEC_HDR_F_F 0x0 // Secondary header absent
#define SPP_SEC_HDR_F_T 0x1 // Secondary header present

#define SPP_APID_GS     0x0 // Ground Station ID
#define SPP_APID_CS     0x1 // CubeSat ID
#define SPP_APID_PING   0x0 // Ping packet
#define SPP_APID_PONG   0x2 // Pong packet

#define SPP_SEQ_CTRL_F_CS 0x0 // Continuous segment
#define SPP_SEQ_CTRL_F_FS 0x1 // First segment
#define SPP_SEQ_CTRL_F_LS 0x2 // Last segment
#define SPP_SEQ_CTRL_F_US 0x3 // Unsegmented

/* SPP Structs */

typedef struct spp_packet_id_s {

    uint8_t type;
    uint8_t sec_hdr_f;
    uint16_t apid;

} spp_packet_id_t;


typedef struct spp_packet_seq_control_s {

    uint8_t seq_f;
    uint16_t seq_count; 

} spp_packet_seq_ctrl_t;


typedef struct spp_header_s {

    uint8_t                 version_number;
    spp_packet_id_t         id;
    spp_packet_seq_ctrl_t   seq_ctrl;
    uint16_t                data_len;

} spp_header_t;


typedef struct spp_packet_s { 

    spp_header_t   header;
    uint8_t*       data;

} spp_packet_t;

/* SPP Functions */

void spp_init_packet(spp_packet_t *packet);

void spp_set_header(spp_packet_t *packet, uint8_t version_number, uint8_t type, uint8_t sec_hdr_f, uint16_t apid, uint8_t seq_f, uint16_t seq_count); 

void spp_set_data(spp_packet_t *packet, uint16_t data_len, uint8_t *data);

void spp_packet_to_buffer(spp_packet_t *packet, uint8_t *buf);

void spp_buffer_to_packet(spp_packet_t *packet, uint8_t *buf);

void spp_print_packet_as_buffer(spp_packet_t *packet);

void spp_pretty_print_packet(spp_packet_t *packet);

#endif // KIN_SPP_H

