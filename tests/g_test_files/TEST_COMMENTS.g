M06 T0101

G0X20Z0 ;testtest
;testtest;testtest
G71U1R0.5 (depth of cut;testtest and retract value);testtest
G71P100Q200U-0.6W-0.15G94F200 (first and last line, uX then wZ sureppaiseur + feed rate)
N100 G00 X20 (p0);testtest
G01 Z-20 (P1)
G01 X15 (p2)
G01 Z-10 (p3);;;;;
G01 X10 (p4)
G03 X5 Z-5 R5 (p5)
N200 G00 X20 Z0 (se rtirer en avance rapide)
;;;
G00X20Z0         ;test   ;;;;;;;;;;;;;
;;;;
G71U1R0.5 (depth of cut a retract value)
G71P100Q200U-0.6W-0.15G94F200 (first and last line, uX then wZ sureppaiseur + feed rate)
N100 G00 X20 (p0)
G01 Z-20 (P1)
G01 X15 (p2);testtest;testtest;testtest;;;;;;;;;;;;;
G01 Z-10 (p3)
G01 X10 (p4)
G03 X5 Z-5 R5 (p5)
N200 G00 X20 Z0 F2000 (se ;testtestrtirer en avance r;testtestapide, on garde F2000 pour que cela reste negligeable dans le temps total.  l'idée est juste d'en tester 2 a la suite)
(FORME DU PROFIL :)


( 1                               0)
( |                                )
( |                                )
( 2                                )
(-----------3                      )
(-----------|                      );testtest
(-----------|                      )
(-----------4                      )
(-----------|                      )
(------------.                     );testtest
(-------------.                    )
(-----------------.                )
(--------------------5-------------)  

(time:)
(1-2 : 5 passes af Vf 2;testtest00 mm /min 20 mm long : 30 secs)
(2-3 : 0)
(3-4 : 5 passes af Vf 200 mm /min 10 mm long : 15 secs)
(4-5 : 5 passes af Vf 200;testtestmm /min 10-5 (M : 8) mm long : 12 secs)

(total est;testtestimated time : 57 + f2000 seconds (+- 4s en gros sera suffisant pour un test convenable));testtest