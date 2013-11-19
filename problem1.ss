(define div-3? (lambda (n) (= (remainder n 3) 0)))

(define div-5? (lambda (n) (= (remainder n 5) 0)))

(define make-list 
  (lambda (l max cur)
  (cond ((= cur max) l)
	((or (div-3? cur) (div-5? cur)) (make-list (cons cur l) max (+ cur 1)))
	(else (make-list l max (+ cur 1))))))

(define sum-list
  (lambda (l val)
    (if (null? l) 
	val
	(sum-list (cdr l) (+ val (car l))))))

(define the-list (make-list () 1000 1))
(sum-list the-list 0)

