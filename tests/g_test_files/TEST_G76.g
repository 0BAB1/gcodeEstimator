%
o1000 (G76 THREAD CUTTING MULTIPLE PASSES) ;

(code inspiré de : http://sitemeca.free.fr/index.php?page=prog/programmation&art=1.2.2&exemple=76#codeGT)

T0808(OUTIL A FILETER PAS 1.5)
G97 M3 S1000 (rot cst 1000 1/min)
G0 X25 Z0
G76 P050029 Q50 R0.02
G76 X18.161 Z-20 P919 Q500 F1.5
M30 (End program) ;

G76 (dummy bug that should be ignored)

(temps d'execution :)
( 60sec/min * 5 passes * 20mm / (1000*1.5mm/min) = 4secs )
(+ 5 passes à vide environ 0.48 secondes pour Fmax = 12500 mm/min)
(+0.12 secs de G0 au debut)
(temps retenu oiur test : 4.6 +- 0.1 secondes)
%