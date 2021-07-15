(declare-datatypes () ((Suite Red Black)))
(declare-datatypes (T1 T2) ((Pair (mk-pair (p1 T1) (p2 T2)))))
(declare-fun game () (Array (Pair Suite Suite) (Pair Suite Suite)))

(define-fun win ((input (Pair Suite Suite)) (output (Pair Suite Suite))) Bool
  (or
    (= (p1 input) (p1 output))
    (= (p2 input) (p2 output))
  )
)

(assert 
  (forall
    ((x (Pair Suite Suite)))
    (= x (select game x))
    ;(win x (select game x))
  )
)

(assert
  (forall
    ((x (Pair Suite Suite)))
    (forall
      ((y (Pair Suite Suite)))
      (and
        (=>
          (= (p1 x) (p1 y))
          (= (p2 (select game x)) (p2 (select game y)))
        )
        (=>
          (= (p2 x) (p2 y))
          (= (p1 (select game x)) (p1 (select game y)))
        )
      )
    )
  )
)

(check-sat)
(get-model)
