-- Write your query below
select e.student_id, e.exam_id, e.score 
from exam_results e join
    (select a.student_id, min(a.exam_id) exam_id
        from exam_results a join
            (select student_id, max(score) max_score
            from exam_results
            group by student_id) b
        on a.student_id = b.student_id and a.score = b.max_score
    group by a.student_id) c
on e.student_id = c.student_id and e.exam_id = c.exam_id