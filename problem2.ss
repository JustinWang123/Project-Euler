(define (even? n) (= (remainder n 2) 0))

(define (fib n)
  (define (fib-it n cur a b sum)
    (if (> a n)
	sum
	(fib-it n (+ cur 1) (+ a b) a (if (even? a)
					  (+ sum a)
					  sum))))
  (fib-it n 2 2 1 0))

(fib 4000000)