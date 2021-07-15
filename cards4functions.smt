(declare-datatypes () ((Suite club spade heart diam)))
(declare-fun t1 (Suite Suite Suite) Suite)
(declare-fun t2 (Suite Suite Suite) Suite)
(declare-fun t3 (Suite Suite Suite) Suite)
(declare-fun t4 (Suite Suite Suite) Suite)

(assert 
    (forall ((c1 Suite) (c2 Suite) (c3 Suite) (c4 Suite) )
        (or
            (= c1 (t1 c2 c3 c4))
            (= c2 (t2 c1 c3 c4))
            (= c3 (t3 c2 c1 c4))
            (= c4 (t4 c2 c3 c1))
        )
    )
)

(check-sat)
(get-value (t1 t2 t3 t4))



