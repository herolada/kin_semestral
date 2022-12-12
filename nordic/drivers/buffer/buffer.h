#ifndef _BUFFER_H_
#define _BUFFER_H_

//VCE: Macro to create buffers
#define BUFFER(name, length)                \
typedef struct                              \
{                                           \
    uint8_t buffer[length];                 \
    uint8_t head;                           \
}name##_buffer_t;                           \
static name##_buffer_t name##_buffer = {    \
    .buffer = {0},                          \
    .head = 0,                              \
};

#endif /* _BUFFER_H_*/
