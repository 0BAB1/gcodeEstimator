% 
O3426(TBOSS LONG 4135526 IND C +2MM) 
(DECALAGE PRG B1)
G10L2P1Z139(G54 BROCHE)
 
G28B0
G28V0
G28U0
G53Z-250 
M1 
 
(MISE EN PLACE BRUT) 
(M98P3000) 
 
(USINAGE BROCHE PRINCIPAL DEBUT G54) 
 
 
N1(DRESSAGE FACE ET EFFACEMENT BALOUR) 
(DWLNR2020K08) 
(P WNMG 08 04 SM H13A) 
G92S2500 
M64
G95
T0101G96S200M3 
G0Y0 
M8(ARROSAGE-ON)
G0X150Z5.0Y0 
M7(ARROSAGE HP-ON) 
(CYCLE EBAUCHE AXIAL)
G71U3R0.5
G71P102Q103U0.4W0.15F0.3 
N102G1X81.803F0.15 
Z0 
G3X91.715Z-1.407R10.5
G1X133.75Z-13.541
G3X135.75Z-15.3R2
N103G1Z-28.0(P C)
 
G0X200Z5 
G0X85Z1.4
G1X-2F0.25 
G0Z2 
G0X85
G1Z0.2F0.25
G1X-2
G0Z5 
 
G28U0V0
G53Z-250 
M09
M01
 
N2(FORET PLAQ DIA 32)
(MVX3200X5F40) 
(SOMX094506-US VP15TF) 
G92S2000 
 
T0202G97M3S1200P11 
G0Y0 
G0Z5.0 
X0.3 
M8(ARROSAGE BROCHE-ON) 
/M58(CTRL EFFORT OT-ON)
(PERCAGE EBAUCHE)
M7(ARROSAGE HP-ON) 
G74R0.1
G74Z-142Q1000F0.1
 
M59(CTRL EFFORT OT-OFF)
G80
G28U0V0
G53Z-250 
M09
M01
 
N111(DRESSAGE FACE EBAUCHE ET FINITION PROFIL EXT) 
(DWLNR2020K08) 
(P WNMG 08 04 SM H13A) 
G28U0V0
G92S2500 
M64(SELECTION BROCHE 1)
G95(AVANCE EN MM/TR) 
T0101G96S150M3 
G0Y0Z5.0 
X93Y0
M8(ARROSAGE-ON)
M7(ARROSAGE HP-ON) 
(CYCLE DRESSAGE FACE)
N101(FINITION PROFIL AVANT BROCHE 1) 
X30
G42Z0
N102(P B)
G1X81.215F0.15(P16)
G3X91.715Z-1.407R10.5(P17) 
G1X133.75Z-13.541(P18) 
G3X135.75Z-15.273R2
G1Z-28.0(P C)
G0X140 
G40Z10.0 
M9 
G28U0V0
G53Z-250 
M1 
 
N4(FRAISAGE DEGAGEMENT)
(WNT 5097210100/DIA10K0.2) 
(LG SORTIE 15MM) 
G28U0V0
M5 
T404 
M10(ACTIVATION AXE C)
G28C0(REF AXE C) 
G0C0(POINT DE DEPART)
G97S3500M74
G0Z5Y0 
G0X48.5
M8 
M7 
G1Z0.5G94F1000 
G1Z-12.3H360F800 
H360F1000
X58.7F800
H360F1000
X67.7F800
H360F1000
Z3 
G0X150 
G0G95Z10 
M75(ARRET OUTIL ROTATIF) 
M11(ANNULATION AXE C)
G28U0V0
G53Z-250 
M1 
 
N12(EB GORGE FRONTALE) 
(S QFT-RFG25C2525-035B)
(P QFT-G-0300-02-GF H10F)
G92S2500 
M64
G95
T1212G96S100M4 
G0Z10.Y-5
M8(ARROSAGE BROCHE-ON) 
M7(ARROSAGE HP-ON) 
G0X50.25 
G0Z-10 
G74R0
G74X44.35Z-14.9P2000Q1800F0.08 
 
G0X50.25 
Z0.5 
G1Z-14F0.5 
G74R0
G74X44.35Z-17.2P2000Q3000F0.08 
G0Z5.0 
 
G0X50.25 
Z0.5 
G1Z-16.5F0.5 
G74R0
G74X44.35Z-19.3P2000Q3000F0.08 
G0Z5.0 
 
 
(EB ZONE 4)
G0Z2 
X46.35 
Z0.5 
G74R2
G74X44.25Z-21.4P2000Q3000F0.08 
G0Z5.0 
 
 
(EB ZONE 4)
G0Z2 
X46.35 
G1Z-21F0.5 
G74R2
G74X44.25Z-23.4P2000Q3000F0.08 
G0Z5.0 
 
 
 
(FINITION GORGE FRONTALE)
(FINITION PROFIL 1)
M64
G95
G92S2500 
T1212G96S120M4 
M8 
M7 
G0X80.7Z2
G1Z0.05F0.10 
G1G41X80.5Z0.03F0.08(P 1)
X78Z-2(P 2)
Z-12.6(P 3)
X50.5,R0.5(P 4/5)
Z-19.5,R0.5(P 6/7) 
X46.69,R0.5(P8/9)
Z-23.6,R0.5(P10/11)
X45.0(P 11)
G0Z5 
G40X40 
 
N32(FINITION PROFIL 2) 
T1232
M8 
M7 
G0X30Z2
G1G42X35Z0.03F0.08(P1.1) 
X38,R1(P2.1) 
Z-23.6,R0.5(P3.1/4.1)
X39.3(P 5.1) 
G0Z5 
G40X40 
M9 
G28U0V0
G53Z-250 
M1 
 
N9(ALESAGE B= FINITION ET FINITION)
(FSDQC2520R-11A) 
(DCGT11T304-AZ HTI10)
T0909G96S180M3 
G0Z5Y0 
G0X34.5
M8 
M7 
(1/2 FINITION) 
G1Z0.5F.12 
G1G41Z0.05F0.12
G2X32.8Z-1R1 
G1Z-81 
X30
G0Z18
G40X36 
(FINITION) 
G1G41Z0.05F0.5 
X33.32,R1F0.08 
Z-81F0.09
X30
G0Z2 
G40X31Z5 
M9 
G28U0V0
G53Z-250 
M1 
 
N3(FILETAGE M80*2) 
(WNT GZD.17.HB.16.30,0.IK) 
(GZD.17.M2,0.IR/IL.Z9 TI500) 
M64
T0303G97S1000M3(S1800) 
G0Z5Y0 
M8 
M7 
G0X77.56 
G1Z5.0F0.2 
G76P010060Q100R0.05
G76X80.0Z-12.5P1200Q400F2.0
 
GOTO76 
G76P010060Q100R.05 
G76X80Z-12.5P1200Q400F2
 
N76G0Z10M9 
M5 
G28U0V0
G53Z-250 
G28B0
G53Z-350 
M0 
GOTO2000 
 
(FIN USINAGE BROCHE PRINCIPAL )
N1000
(TRANSFERT PIECE BROCHE/CONTRE BROCHE) 
 
M64(CODEUR SP1)
G97S0M3(S200)
M63(ANNULATION M62)
G4U.5
M62(SYNCHRO PHASE BROCHES) 
 
G28V0
G28U0
G53Z-350 
M115(ACTIVE CTRL POUSSEE AXE B AVEC VALEUR #1133)
M53(OUVERTURE PINCE C-B) 
M89(ANNULATION M87 ET M88) 
M86(EJECTEUR C-B OFF)
#1133=80(80-VALEUR INDICATIVE DE POUSSEE)
G0B-405.7(APPROCHE RAPIDE) 
M78(ACTIVE CTRL EFFORT AXE B)
G1G94B-438.70F2000(POSITION A 2MM DE LA BUTEE) 
M79(DESACTIVE CONTROLE EFFORT AXE B) 
#1133=50(50-VALEUR INDICATIVE POUSSEE CB)
M72(ACTIVE REDUCTION POUSSEE POUR APPUI EN BUTEE)
G1G31P98B-442.70F500(+2MM PAR RAPPORT A LA BUTEE)
G4U0.5 
M29(ANNULATION MENOIRE)
B[#5065+0.03](DETENTE AXE B) 
M54(FERMETURE PINCE C-B) 
G4U1 
M79(ANNULATION CTRL EFFORT)
M24(OUVERTURE MANDRIN PRINCIPAL) 
G4U1.0 
G28B0
M63
M1 
 
(------------------) 
N2000
(USINAGE CONTRE-BROCHE DEBUT G55)
(ORIGINE PRG B2) 
N41G10L2P2Z378.97(G55)(375.92) 
G28U0V0
G53Z-250 
 
(EB FACE)
 
(DWLNL2020K08) 
(WNMG080408-MA MP9015) 
M65(SELECTION B2)
G92S3000 
G18G40G80G95G97
T0141G96S200M3 
G0Y0B0 
G55
G0Z-10.0 
X85
M8 
M7 
G0Z-8
G79Z-7.5X30F0.25 
Z-7
Z-6
Z-5
Z-4
Z-3
Z-2
Z-1
Z-0.15 
G0X140.Z-10. 
(EBAUCHE PROFIL EXTERIEUR) 
G0Z-5
G0X135.0 
G73U10W-0.5R6(R20) 
G73P281Q283U0.4W-0.15F0.25 
N281G0X75.97,C0.35F0.2 
G1X76.002Z8.5
G1X61.9Z18 
Z61.2
X78Z63.2 
Z65.5
X64.258Z83.5(P10 + RAYON PLAQ EN Z)
G3X64Z83.581R2(G2)(P 11) 
G1Z84.581(P 12)
G3X81.697Z96.90R13(G2)(P 13) 
G2X134.228Z111.13R87.541(G3)(P 14) 
N283G2X135.75Z112.7R2(P 20)
G0X200Z5 
G28U0V0
G53Z-250 
M01
 
N25(FINITION EXTER)
(SVJCR2020K16) 
(VCGT160404-AZ HTI10)
G28U0V0
G53Z-250 
G92S3000 
M65
T0525
G55
G0Y0B0 
G96S300M3
G0Z-5
X80. 
M8 
M7 
Z0 
G1G95X30.0F0.15
Z-1
G0X75
G1G41Z-0.05F0.25 
G1X75.97,C0.35F0.035 
Z9F0.1 
Z62F1
X73.0Z63.45F0.1(P7)
X76.002(P8)
G2X77.871Z64.853R1(P9) 
G1X64.258Z82.874(P10)
G3X64Z83.581R2(P 11) 
G1Z84.581(P 12)
G3X81.697Z96.9R13(P 13)
G2X134.228Z111.13R87.541(P 14) 
G2X135.75Z112.7R2(P20) 
G2X134.394Z114.6R3(P21)
G1G40X140
G0Z-5
M9 
G28U0V0
G53Z-250 
M01
 
N34(GORGE EXTER) 
(GYQL2020K00-F06)
(GY2G0300F005N-GL RT9010)
G92S3000 
G28U0V0
G53Z-250 
M65
T0334G96S120M4 
G55
G0Z-5Y0B0
G0X82
M8 
M7 
Z17.5
G1X62.4F0.12 
G0X78
Z15
G1X62.4F0.12 
G0X80
Z13
G1X62.4F0.12 
G0X80
Z11
G1X62.4F0.12 
G0X80
Z9.8 
G1X62.4F0.12 
G0X82
 
T0323
G0X82
G0Z-4
G1G41X76.47F.25
Z3.
Z6.5,R0.55F0.03
X61.975,R0.7F0.07
Z59.0F.10
G0X82
G40X85 
T0334
G1G42X80Z63.5F0.10 
X61.975,R0.7F0.07
Z58F0.1
G0X140.0 
G0G40Z-5 
M9 
G28U0V0
G53Z-250 
M1 
 
N28(ALESAGE INT) 
G28U0V0
G53Z-250 
(FSDQC2520R-11A) 
(DCGT11T304-AZ HTI10)
G92S3000 
M65
T0828G96S200M3 
G55
G0Z-15.0Y0B0 
M8 
M7 
G0X32Z-10.0
G71U1R0.5
G71P251Q252U-0.6W-0.15F0.2 
N251G1Z-0.1X41 
G1X38.55,C1.1F0.1
G1Z4.95
G1A-45X36.05 
G1Z42.66 
A-15,R3
N252A0X33.20Z48.373
G0X160 
M01
 
(FINITION PROFIL INTER)
(FSDQC2520R-11A) 
(DCGT11T304-AZ HTI10)
G0X42.0
G1G42Z-0.5 
G1Z-0.1X41 
G1X38.55,C1.1F0.1
G1Z4.95
G1A-45X35.9(X36.05)
Z42.52 
X33.404Z47.457 
G3X33.29Z48.233R3F0.08 
(A-15,R3)
(A0X33.20Z48.233)
G1X33.1Z49.229 
G1X30.0
G0Z-20.0 
G40
M9 
G28U0V0
G53Z-250 
M1 
 
N26(FILETAGE 1 1/2 12 UNF) 
(MMTIR2925AAS16-C) 
(MMT16IR120UN VP10MF)
M65
T0626G97S1000M3
G0G55Z-10.0B0
G0X35Y0
M8 
M7 
G76P010055Q120R0.05
G76X38.1Z41.2P1375Q500F2.116 
M9 
G28U0V0
G53Z-250.
M01
 
N24(FRAISAGE MEPLATS 32.5*2) 
G28U0V0
G28B0
G53Z-250 
(FRAISE DIA 10)
(LG SORTIE 10MM) 
(#100=DIA FRAISE)
#100=10.0
T0424M65 
G55
M10
G28C0
G0C0(POINT DE DEPART)
G97S3500M73
G0Z-5
(EBAUCHE)
X[69+#100]Y-25 
G0Z7 
M8 
M7 
G1G94Y25F500(1)
G0Z-5
G0H180Y-25 
Z7 
G1G94Y25(2)
G0Z-5
G0H180Y-28 
(FINITION) 
X[65+#100]Y-28 
G0Z7 
G1G94Y28F500 
G0Z-5
G0H180Y-28 
Z7 
G1G94Y28 
G0Z-5
M9 
M75
M11
G28U0V0
G53Z-250 
M01
 
N27(FRAISAGE PETITS MEPLATS 65)
G28U0V0
G28B0
G53Z-250 
(FRAISE DIA 10)
(LG SORTIE ) 
(#100=RAYON FRAISE)
#100=5.0 
T0727M65 
G55
M10
G28C0
G0C0(POINT DE DEPART)
G97S3500M73
G0Z-5
X85Y-15
G0Z[76.5+#100] 
X65
M8 
M7 
G1G94Y15F400 
G0X85
G0H180Y-15 
X65
G1G94Y15 
G0X120 
M9 
M75
M11
G28U0V0
G53Z-250 
M01
 
N300 
M30
%