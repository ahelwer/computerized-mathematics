(declare-datatypes () ((Suite Red Black)))
(declare-fun t1 (Suite) Suite)
(declare-fun t2 (Suite) Suite)

(assert 
    (forall ((c1 Suite) (c2 Suite))
        (or
            (= c1 (t1 c2))
            (= c2 (t2 c1))
        )
    )
)

(check-sat)
(get-value (t1 t2))
