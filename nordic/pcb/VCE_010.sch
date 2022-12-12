EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "VCE - Breakout Board"
Date "25-11-2020"
Rev "3"
Comp "Araciv Technologies Pvt. Ltd."
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:C C1
U 1 1 5F7C8CB2
P 1000 1000
F 0 "C1" H 1100 950 50 0000 L CNN
F 1 "100nF" H 1100 1050 50 0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1000 1000 50 0001 C CNN
F 3 "~" H 1000 1000 50 0001 C CNN
    1   1000 1000
    1   0   0   -1
$EndComp
Connection ~ 1000 850
Wire Wire Line
    1000 850 1000 800
Wire Wire Line
    1000 800 1200 800
Text Label 1000 800 0 50 ~ 0
VDD
Connection ~ 1000 1150
Wire Wire Line
    1000 1150 1000 1200
Wire Wire Line
    1000 1200 1200 1200
Text Label 1000 1200 0 50 ~ 0
GND
$Comp
L Device:C C2
U 1 1 5F7C8CB2
P 1000 1500
F 0 "C2" H 1100 1450 50 0000 L CNN
F 1 "100nF" H 1100 1550 50 0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1000 1500 50 0001 C CNN
F 3 "~" H 1000 1500 50 0001 C CNN
    1   1000 1500
    1   0   0   -1
$EndComp
Connection ~ 1000 1350
Wire Wire Line
    1000 1350 1000 1300
Wire Wire Line
    1000 1300 1200 1300
Text Label 1000 1300 0 50 ~ 0
VDD
Connection ~ 1000 1650
Wire Wire Line
    1000 1650 1000 1700
Wire Wire Line
    1000 1700 1200 1700
Text Label 1000 1700 0 50 ~ 0
GND
$Comp
L Sensor_Motion:BMI160 U1
U 1 1 5F7C8CB2
P 3000 1500
F 0 "U1" H 3000 1000 50 0000 C CNN
F 1 "BMI160" H 3000 2050 50 0000 C CNN
F 2 "Package_LGA:Bosch_LGA-14_3x2.5mm_P0.5mm" H 3000 1500 50 0001 C CNN
F 3 "~" H 3000 1500 50 0001 C CNN
    1   3000 1500
    1   0   0   -1
$EndComp
Connection ~ 2900 1100
Wire Wire Line
    2900 1100 2900 1000
Connection ~ 3000 1100
Wire Wire Line
    3000 1100 3000 1000
Wire Wire Line
    2900 1000 3200 1000
Connection ~ 2900 1000
Connection ~ 3000 1000
Text Label 3000 1000 0 50 ~ 0
VDD
Connection ~ 2900 2000
Wire Wire Line
    2900 2000 2900 2100
Connection ~ 3000 2000
Wire Wire Line
    3000 2000 3000 2100
Wire Wire Line
    2900 2100 3200 2100
Connection ~ 2900 2100
Connection ~ 3000 2100
Text Label 3000 2100 0 50 ~ 0
GND
Wire Wire Line
    3400 1400 3600 1400
Text Label 3450 1400 0 50 ~ 0
GND
Wire Wire Line
    3400 1500 3600 1500
Text Label 3450 1500 0 50 ~ 0
GND
Wire Wire Line
    3400 1600 3600 1600
Text Label 3450 1600 0 50 ~ 0
GND
Wire Wire Line
    3400 1700 3600 1700
Text Label 3450 1700 0 50 ~ 0
GND
Wire Wire Line
    2500 1300 2300 1300
Text Label 2350 1300 0 50 ~ 0
SDO
Wire Wire Line
    2500 1400 2300 1400
Text Label 2350 1400 0 50 ~ 0
SDA
Wire Wire Line
    2500 1500 2300 1500
Text Label 2350 1500 0 50 ~ 0
SCL
Wire Wire Line
    2500 1600 2300 1600
Text Label 2350 1600 0 50 ~ 0
VDD
Wire Wire Line
    2500 1700 2300 1700
Text Label 2350 1700 0 50 ~ 0
INT1
Wire Wire Line
    2500 1800 2300 1800
Text Label 2350 1800 0 50 ~ 0
INT2
$Comp
L MS50SFA_VCE:MS50SFA_NRF52 U2
U 1 1 5F7C8CB2
P 7500 4500
F 0 "U2" H 7500 5500 50 0000 C CNN
F 1 "MS50SFA_NRF52" H 7500 5550 50 0000 C CNN
F 2 "MS50SFA_NRF52:MS50SFA_NRF52_Module" H 7500 4500 50 0001 C CNN
F 3 "~" H 7500 4500 50 0001 C CNN
    1   7500 4500
    1   0   0   -1
$EndComp
Wire Wire Line
    6500 4500 6300 4500
Text Label 6450 4500 0 50 ~ 0
INT1
Wire Wire Line
    6500 4000 6300 4000
Text Label 6450 4000 0 50 ~ 0
3
Wire Wire Line
    6500 3500 6300 3500
Text Label 6450 3500 0 50 ~ 0
9
Wire Wire Line
    6500 3000 6300 3000
Text Label 6450 3000 0 50 ~ 0
10
Wire Wire Line
    6500 2500 6300 2500
Text Label 6450 2500 0 50 ~ 0
30
Wire Wire Line
    6500 2000 6300 2000
Text Label 6450 2000 0 50 ~ 0
29
Wire Wire Line
    6500 1500 6300 1500
Text Label 6450 1500 0 50 ~ 0
28
Wire Wire Line
    6500 1000 6300 1000
Text Label 6450 1000 0 50 ~ 0
27
NoConn ~ 6500 500
Wire Wire Line
    8500 4500 8700 4500
Text Label 8550 4500 0 50 ~ 0
VDD
Wire Wire Line
    8500 4000 8700 4000
Text Label 8550 4000 0 50 ~ 0
GND
Wire Wire Line
    8500 3500 8700 3500
Text Label 8550 3500 0 50 ~ 0
INT2
Wire Wire Line
    8500 3000 8700 3000
Text Label 8550 3000 0 50 ~ 0
12
Wire Wire Line
    8500 2500 8700 2500
Text Label 8550 2500 0 50 ~ 0
SCL
Wire Wire Line
    8500 2000 8700 2000
Text Label 8550 2000 0 50 ~ 0
SDA
Wire Wire Line
    8500 1500 8700 1500
Text Label 8550 1500 0 50 ~ 0
SWDIO
Wire Wire Line
    8500 1000 8700 1000
Text Label 8550 1000 0 50 ~ 0
SWCLK
Wire Wire Line
    8500 500 8700 500
Text Label 8550 500 0 50 ~ 0
RST
$Comp
L Connector:Conn_01x05_Male J1
U 1 1 5F7C8CB2
P 1000 4500
F 0 "J1" V 800 4450 50 0000 C CNN
F 1 "Conn_01x05_Male" V 800 4550 50 0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 1000 4500 50 0001 C CNN
F 3 "~" H 1000 4500 50 0001 C CNN
    1   1000 4500
    1   0   0   -1
$EndComp
Connection ~ 1200 4300
Wire Wire Line
    1200 4300 1400 4300
Text Label 1250 4300 0 50 ~ 0
10
Connection ~ 1200 4400
Wire Wire Line
    1200 4400 1400 4400
Text Label 1250 4400 0 50 ~ 0
9
Connection ~ 1200 4500
Wire Wire Line
    1200 4500 1400 4500
Text Label 1250 4500 0 50 ~ 0
GND
Connection ~ 1200 4600
Wire Wire Line
    1200 4600 1400 4600
Text Label 1250 4600 0 50 ~ 0
VDD
Connection ~ 1200 4700
Wire Wire Line
    1200 4700 1400 4700
Text Label 1250 4700 0 50 ~ 0
SDO
$Comp
L Connector:Conn_01x05_Male J2
U 1 1 5F7C8CB2
P 1000 6000
F 0 "J2" V 800 5950 50 0000 C CNN
F 1 "Conn_01x05_Male" V 800 6050 50 0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 1000 6000 50 0001 C CNN
F 3 "~" H 1000 6000 50 0001 C CNN
    1   1000 6000
    1   0   0   -1
$EndComp
Connection ~ 1200 5800
Wire Wire Line
    1200 5800 1400 5800
Text Label 1250 5800 0 50 ~ 0
27
Connection ~ 1200 5900
Wire Wire Line
    1200 5900 1400 5900
Text Label 1250 5900 0 50 ~ 0
28
Connection ~ 1200 6000
Wire Wire Line
    1200 6000 1400 6000
Text Label 1250 6000 0 50 ~ 0
29
Connection ~ 1200 6100
Wire Wire Line
    1200 6100 1400 6100
Text Label 1250 6100 0 50 ~ 0
30
Connection ~ 1200 6200
Wire Wire Line
    1200 6200 1400 6200
Text Label 1250 6200 0 50 ~ 0
3
$Comp
L Connector:Conn_01x05_Male J3
U 1 1 5F7C8CB2
P 2500 4500
F 0 "J3" V 2300 4450 50 0000 C CNN
F 1 "Conn_01x05_Male" V 2300 4550 50 0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 2500 4500 50 0001 C CNN
F 3 "~" H 2500 4500 50 0001 C CNN
    1   2500 4500
    1   0   0   -1
$EndComp
Connection ~ 2700 4300
Wire Wire Line
    2700 4300 2900 4300
Text Label 2750 4300 0 50 ~ 0
RST
Connection ~ 2700 4400
Wire Wire Line
    2700 4400 2900 4400
Text Label 2750 4400 0 50 ~ 0
SWCLK
Connection ~ 2700 4500
Wire Wire Line
    2700 4500 2900 4500
Text Label 2750 4500 0 50 ~ 0
SWDIO
Connection ~ 2700 4600
Wire Wire Line
    2700 4600 2900 4600
Text Label 2750 4600 0 50 ~ 0
GND
Connection ~ 2700 4700
Wire Wire Line
    2700 4700 2900 4700
Text Label 2750 4700 0 50 ~ 0
VDD
$Comp
L Connector:Conn_01x05_Male J4
U 1 1 5F7C8CB2
P 2500 6000
F 0 "J4" V 2300 5950 50 0000 C CNN
F 1 "Conn_01x05_Male" V 2300 6050 50 0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 2500 6000 50 0001 C CNN
F 3 "~" H 2500 6000 50 0001 C CNN
    1   2500 6000
    1   0   0   -1
$EndComp
Connection ~ 2700 5800
Wire Wire Line
    2700 5800 2900 5800
Text Label 2750 5800 0 50 ~ 0
12
Connection ~ 2700 5900
Wire Wire Line
    2700 5900 2900 5900
Text Label 2750 5900 0 50 ~ 0
GND
Connection ~ 2700 6000
Wire Wire Line
    2700 6000 2900 6000
Text Label 2750 6000 0 50 ~ 0
GND
Connection ~ 2700 6100
Wire Wire Line
    2700 6100 2900 6100
Text Label 2750 6100 0 50 ~ 0
VDD
Connection ~ 2700 6200
Wire Wire Line
    2700 6200 2900 6200
Text Label 2750 6200 0 50 ~ 0
V_BAT
$Comp
L Device:C C3
U 1 1 5F7C8CB2
P 6000 6000
F 0 "C3" H 6100 5950 50 0000 L CNN
F 1 "1uF" H 6100 6050 50 0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 6000 6000 50 0001 C CNN
F 3 "~" H 6000 6000 50 0001 C CNN
    1   6000 6000
    1   0   0   -1
$EndComp
Connection ~ 6000 5850
Wire Wire Line
    6000 5850 6000 5800
Wire Wire Line
    6000 5800 6200 5800
Text Label 6000 5800 0 50 ~ 0
VDD
Connection ~ 6000 6150
Wire Wire Line
    6000 6150 6000 6200
Wire Wire Line
    6000 6200 6200 6200
Text Label 6000 6200 0 50 ~ 0
GND
$Comp
L Device:C C4
U 1 1 5F7C8CB2
P 6000 6500
F 0 "C4" H 6100 6450 50 0000 L CNN
F 1 "1uF" H 6100 6550 50 0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 6000 6500 50 0001 C CNN
F 3 "~" H 6000 6500 50 0001 C CNN
    1   6000 6500
    1   0   0   -1
$EndComp
Connection ~ 6000 6350
Wire Wire Line
    6000 6350 6000 6300
Wire Wire Line
    6000 6300 6200 6300
Text Label 6000 6300 0 50 ~ 0
V_BAT
Connection ~ 6000 6650
Wire Wire Line
    6000 6650 6000 6700
Wire Wire Line
    6000 6700 6200 6700
Text Label 6000 6700 0 50 ~ 0
GND
$Comp
L Device:C C4
U 1 1 5F7C8CB2
P 6000 8000
F 0 "C4" H 6000 7800 50 0000 L CNN
F 1 "1uF" H 6000 7800 50 0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 6000 8000 50 0001 C CNN
F 3 "~" H 6000 8000 50 0001 C CNN
    1   6000 8000
    1   0   0   -1
$EndComp
Wire Wire Line
    6000 8300 6000 8500
Text Label 6000 8350 1 50 ~ 0
GND
Wire Wire Line
    6300 8000 6500 8000
Text Label 6350 8000 0 50 ~ 0
VDD
Wire Wire Line
    5700 8000 5500 8000
Text Label 5550 8000 0 50 ~ 0
V_BAT
$EndSCHEMATC
